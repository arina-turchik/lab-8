import sys
import os

def suppress(f):
    def wrap(*args, **kwargs):
        origin = sys.stdout
        with open(os.devnull, 'w') as devnull:
            sys.stdout = devnull
            res = f(*args, **kwargs)
        sys.stdout = origin
        return res
    return wrap

def hero_hp():
    hp = 100

    def update_health(n):
        nonlocal hp
        hp += n
        if hp > 100:
            hp = 100
        elif hp < 0:
            hp = 0
        print(hp)
        return hp
    print(hp)
    return update_health


hero=hero_hp()
hero(-20)
hero(-100)
suppress(hero)(80)
