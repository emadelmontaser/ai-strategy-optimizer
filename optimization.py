# algorithms will pick a p_cooperate and adjust depending on
# how well the algorithm is scoring

import random
import math
from simulation import SimulationEngine
from strategies import AlwaysCooperate, AlwaysDefect, TitForTatStrategy
from evolvedStrategy import evolvedStrategy

def evaluateSolution(p):
    strategyCandidate = evolvedStrategy(p)
    opponents = [AlwaysCooperate, AlwaysDefect, TitForTatStrategy]
    totalScore = 0
    for Opponent in opponents:
        engine = SimulationEngine(strategyCandidate, Opponent(), 64)
        scores, history = engine.run_game()
        totalScore += scores[0]
    return totalScore / len(opponents)

def hillClimbing(p, maxIterations=100, step=0.1):
    bestCandidate = p
    bestScore = evaluateSolution(bestCandidate)
    for i in range(maxIterations):
        neighbor = bestCandidate + random.uniform(-step, step)
        neighbor = max(0, min(1, neighbor))
        neighborScore = evaluateSolution(neighbor)
        if neighborScore < bestScore:
            bestCandidate = neighbor
            bestScore = neighborScore
    return bestCandidate, bestScore

def geneticAlgorithm(popSize=20, generations=50, mutationRate=0.1, crossoverRate=0.7):
    population = [random.random() for i in range(popSize)]
    bestCandidate, bestScore = None, float('inf')
    def getScore(item):
        return item[1]
    for i in range(generations):
        scored = [(p, evaluateSolution(p)) for p in population]
        for candidate, score in scored:
            if score < bestScore:
                bestCandidate, bestScore = candidate, score
        scored.sort(key=getScore)
        parents = scored[: popSize // 2]
        newPopulation = []
        while len(newPopulation) < popSize:
            parent1, parent2 = selectTwoParents(parents)
            if random.random() < crossoverRate:
                child1, child2 = crossover(parent1, parent2)
            else:
                child1, child2 = parent1[0], parent2[0]
            if random.random() < mutationRate:
                child1 = mutate(child1)
            if random.random() < mutationRate:
                child2 = mutate(child2)
            newPopulation.append(child1)
            if len(newPopulation) < popSize:
                newPopulation.append(child2)
        population = newPopulation
    return bestCandidate, bestScore

def selectTwoParents(scored):
    half = len(scored)
    i1 = random.randint(0, half - 1)
    i2 = random.randint(0, half - 1)
    return scored[i1], scored[i2]

def crossover(a, b):
    pA, pB = a[0], b[0]
    child1 = 0.5 * (pA + pB)
    child2 = 0.5 * (pA + pB)
    return child1, child2

def mutate(val):
    val += random.uniform(-0.05, 0.05)
    return max(0, min(1, val))

def simulatedAnnealing(p, maxIterations=100, step=0.1, initialTemp=1.0, alpha=0.99):
    current = p
    currentScore = evaluateSolution(current)
    bestCandidate, bestScore = current, currentScore
    temperature = initialTemp
    for _ in range(maxIterations):
        neighbor = current + random.uniform(-step, step)
        neighbor = max(0, min(1, neighbor))
        neighborScore = evaluateSolution(neighbor)
        delta = neighborScore - currentScore
        if delta < 0:
            current, currentScore = neighbor, neighborScore
        else:
            if random.random() < math.exp(-delta / temperature):
                current, currentScore = neighbor, neighborScore
        if currentScore < bestScore:
            bestCandidate, bestScore = current, currentScore
        temperature *= alpha
    return bestCandidate, bestScore

if __name__ == "__main__":
    hSol, hScore = hillClimbing(0.5, maxIterations=10)
    print(f"[Hill Climbing] p_cooperate: {hSol:.4f} Score: {hScore:.4f}")
    gSol, gScore = geneticAlgorithm(popSize=10, generations=5)
    print(f"[Genetic Algorithm] p_cooperate: {gSol:.4f} Score: {gScore:.4f}")
    saSol, saScore = simulatedAnnealing(0.5, maxIterations=10)
    print(f"[Simulated Annealing] p_cooperate: {saSol:.4f} Score: {saScore:.4f}")