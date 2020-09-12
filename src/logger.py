from enum import Enum

class Action(Enum):
    START = '[START]'
    END = '[END]',
    ADD = '[ADD]',
    REMOVE ='[REMOVE]'


def t(entity:any, action:Action, env=None, *args):
    print(action.value, env.now, entity, '\n', args)