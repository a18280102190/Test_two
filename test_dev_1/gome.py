import random


def game():
    my_hp = 1000
    my_power = random.randint(20, 100)
    you_ph = 1000
    you_power = random.randint(20, 100)
    while True:
        my_hp = my_hp - you_power
        print('我方：战斗开始 %s' % (my_hp))
        you_ph = you_ph - my_power
        print('敌方：战斗开始 %s' % (you_ph))
        if my_hp <= 0:
            print('我输了，游戏结束')
            break
        elif you_ph <= 0:
            print('敌人，你输了')
            break

if __name__ == '__main__':
    game()