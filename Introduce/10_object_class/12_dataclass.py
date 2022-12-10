from dataclasses import dataclass

@dataclass
class TeenyDataClass:
    name:str

teeny = TeenyDataClass('bitsy')
print(teeny.name)