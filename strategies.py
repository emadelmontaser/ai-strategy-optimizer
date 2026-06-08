from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def get_move(self, history, my_score, opponent_score):
        pass

class TitForTatStrategy(Strategy):
    def get_move(self, history, my_score, opponent_score):
        if not history:
            return "C"
        return history[-1][1]
        
class AlwaysCooperate(Strategy):
    def get_move(self, history, my_score, opponent_score):
        return "C"

class AlwaysDefect(Strategy):
    def get_move(self, history, my_score, opponent_score):
        return "D"