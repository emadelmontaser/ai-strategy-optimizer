# evolvedStrategy randomizes a value between 0 and 1 and then
# will compare it to p_cooperate. If the value is less than p_cooperate it will
# cooperate otherwise it will defect. The higher the value p_cooperate it
# the more likely the algorithm will cooperate

import random

class evolvedStrategy:
    def __init__(self, p_cooperate):
        self.p_cooperate = p_cooperate

    def get_move(self, history, my_score, opponent_score):
        if random.random() < self.p_cooperate:
            return "C"
        return "D"