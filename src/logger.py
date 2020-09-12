from enum import Enum

class Action(Enum):
    START = '[START]'
    END = '[END]'


def t(entity:any, action:Action):
    print(action.value, entity)