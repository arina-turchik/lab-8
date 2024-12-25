# Лабораторная работа №8
### Вариант№7
## Ход работы:
1. Разобратьс в работе с замыканиями и декораторами.
2. Написать программы, выолняющие поставленные задачи.
3. Загрузить решение на `github`.
### Задача №1
Написать замыкание для отслеживания количества HP героя - HP не может подниматься больше 100 и опускаться ниже 0, герой может лечиться или получать урон.
#### Решение
```
def hero_hp():
    hp = 100

    def upd_hp(n):
        nonlocal hp
        hp += n
        if hp>100:
            hp=100
        if hp<0:
            hp=0
        return hp
    return upd_hp

hero=hero_hp()
print('Введите, сколько раз будет изменяться HP героя(целое натуральное число):')
r=int(input())
for i in range(r):
    print('Введите изменение HP героя(для получения урона используйте отрицательные числа, для лечения положительные):')
    n=int(input())
    print(hero(n))
```
### Задача №2
Написать декоратор для подавления вывода функции на консоль.
#### Решение
```
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
    print('Подавление.')
func()
```
## Источники:
[evil-teacher](https://evil-teacher.on-fleek.app/prog_pm/term1/lab08/)  
[nonlocal function](https://docs-python.ru/tutorial/opredelenie-funktsij-python/operatory-global-nonlocal/)  
[*args and **kwargs](https://habr.com/ru/companies/ruvds/articles/482464/)  
