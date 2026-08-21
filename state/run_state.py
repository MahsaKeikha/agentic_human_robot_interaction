from dataclasses import dataclass
@dataclass
class RunState: status:str="planned"; human_reviewed:bool=False
