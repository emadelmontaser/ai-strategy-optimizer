import unittest
from simulation import play_rnd, COOPERATE, DEFECT, SimulationEngine
from strategies import AlwaysCooperate
from strategies import AlwaysDefect
from strategies import TitForTatStrategy


class TestSimulationEngine(unittest.TestCase):
    def test_play_round(self):
        self.assertEqual(play_rnd(COOPERATE, COOPERATE), (1, 1))
        self.assertEqual(play_rnd(COOPERATE, DEFECT), (20, 0))
        self.assertEqual(play_rnd(DEFECT, COOPERATE), (0, 20))
        self.assertEqual(play_rnd(DEFECT, DEFECT), (10, 10))
    
    def test_simulation_engine(self):
        print("\nRunning test: AlwaysCooperate vs AlwaysCooperate") 
        engine = SimulationEngine(AlwaysCooperate, AlwaysCooperate, rounds=64)
        scores, history = engine.run_game()
        print(f"Result: {scores}")   

        self.assertEqual(scores, [64, 64])
        self.assertEqual(len(history), 64)

if __name__ == "__main__":
    unittest.main()
