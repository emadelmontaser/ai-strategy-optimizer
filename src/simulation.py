DEFECT = "D"
COOPERATE = "C"

YEARS_MATRIX = {
    (COOPERATE, COOPERATE): (1, 1),
    (COOPERATE, DEFECT): (20, 0),
    (DEFECT, COOPERATE): (0, 20),
    (DEFECT, DEFECT): (10, 10)
}

def play_rnd (move1, move2):
    return YEARS_MATRIX[(move1, move2)]

class SimulationEngine:
    def __init__(self, strat1, strat2, rounds=64):
        self.rounds = rounds
        
        if callable(strat1):
            self.strat1 = strat1()
        else:
            self.strat1 = strat1

        if callable(strat2):
            self.strat2 = strat2()
        else:
            self.strat2 = strat2

        self.rnd_history = []
        self.game_score = [0, 0]

    def run_game(self):
        for _ in range(self.rounds):
            move1 = self.strat1.get_move(self.rnd_history, self.game_score[0], self.game_score[1])
            move2 = self.strat2.get_move(self.rnd_history, self.game_score[1], self.game_score[0])
            years1, years2 = play_rnd(move1, move2)
            self.game_score[0] += years1
            self.game_score[1] += years2
            self.rnd_history.append((move1, move2))

        return self.game_score, self.rnd_history