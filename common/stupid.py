import random
off = '\033[0;0m'
fun_col = '\033[48;5;236m'
def lstr(str_:str, length=10) -> str:
    str_ = str(str_)
    return str_[0:length] + " " * (length - len(str_))

def fun(letter:str) -> str:
    return f'\33[{random.randrange(0,255)};{random.randrange(0,255)};{random.randrange(0,255)}m{letter}\033[0;0m'

def fstr(str_:str):
    """a more fun type of fstring"""
    return_str = ''
    for l in str_:
        return_str += fun(l)
    return return_str
    
STUPID = "\033[48;5;236m\033[38;5;0mSu\033[23;44;44mcc\033[38;5;208mess\033[0;0m"
