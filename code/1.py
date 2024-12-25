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