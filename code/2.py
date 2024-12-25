import sys, os

def supress(f):
    def wrap(*args,**kwargs):
        origin=sys.stdout
        with open(os.devnull,'w') as devnull:
            sys.stduot=devnull
            res=f(*args,**kwargs)
        sys.stdout=origin
        return res
    return wrap

@supress
def func():
    print('Подавление.') #YOU ARE POWERLESS.
func()