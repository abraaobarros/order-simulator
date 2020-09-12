from enum import Enum

class Action(Enum):
    START = '[START]'
    END = '[END]'


def t(entity:any, action:Action, env):
    print(action.value, env.now, entity, '\n')