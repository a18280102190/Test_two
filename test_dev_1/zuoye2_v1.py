

#作业二：

import random

class TongLao():
    def see_people(self,name):
        self.name = name
        if name == 'WYZ':
            print('师弟！！！！')
        elif name == 'LQS':
            print('呸，贱人')
        elif name == 'DCQ':
            print('叛徒！我杀了你')

    def ight_zms(self,my_hp,my_force_value,the_enemy_ph,the_enemy_force_value):
        self.my_hp = my_hp
        self.my_force_value = my_force_value
        self.the_enemy_ph = the_enemy_ph
        self.the_enemy_force_value = the_enemy_force_value

        while True:
            my_hp = my_hp - the_enemy_force_value
            print(f"我方血量：{my_hp},敌方伤害{the_enemy_force_value}")
            the_enemy_ph = the_enemy_ph - my_force_value
            print(f"敌方方血量：{the_enemy_ph},我方伤害{my_force_value}")
            if my_hp <= 0:
                print('敌方胜利')
                break
            elif the_enemy_ph <= 0:
                print('我方胜利')
                break

            elif my_hp and the_enemy_ph == 0:
                print(f'平局{my_hp},{the_enemy_ph}')


class XuZhu(TongLao):
    def read(self):
        print('XuZhu曰:罪过罪过!罪过罪过!罪过罪过!')

user1 = TongLao()
user1.see_people(random.choice(['WYZ','LQS','DCQ']))
user1.ight_zms(5000/2,random.randint(10,10)*10,5000,random.randint(10,20))

user2 = XuZhu()
user2.read()
print(isinstance(user2,TongLao))
