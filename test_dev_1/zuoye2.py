#作业一：

class Describe():
    def __init__(self,name,special,hobby):
        self.name = name
        self.special = special
        self.hobby = hobby

    def animal(self):
        print(f"名字：{self.name}, 特点：{self.special}, 爱好：{self.hobby}")


class Describes(Describe):
    def __init__(self,name,special,hobby):
        super().__init__(name,special,hobby)


user1 = Describe('猴子','灵活，聪明','吃香蕉')
user1.animal()

user2 = Describes('大象','高大，强壮','游泳,吃甘蔗')
user2.animal()

user3 = Describes('猎豹','速度与激情','吃肉')
user3.animal()

user4 = Describes('鳄鱼','水中的潜伏杀手','吃小动物')
user4.animal()

user5 = Describes('变色龙','大自然的魔术师','猎杀昆虫')
user5.animal()


