from dataclasses import dataclass

@dataclass
class Statement:
    statement: str
    occured: bool
    
    def to_file(self):
        return "{self.statement}<>{str(self.occured)}"

@dataclass
class Wager:
    holder: str
    card: list()
    won: bool = False
    
@dataclass
class Bet:
    participants: list()
    pot: int
    active: bool = False
    
    