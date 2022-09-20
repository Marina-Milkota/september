# ДЗ на четверг:
# В классе Phone завести приватное свойство __how_many_charges, которое покажет уровень заряда телефона.
# Для изменения заряда телефона прописать метод charge(), в котором меняется значение приватного свойства.

class Phone:
    def __init__(self):
        self.__how_many_charges=0
    def charge(self,ch):
        self.__how_many_charges+=ch
        print(f'Заряд изменился на {ch}. Уровень заряда составляет {self.__how_many_charges}.')

my_phone=Phone()
my_phone.charge(44)
my_phone.charge(-15)
