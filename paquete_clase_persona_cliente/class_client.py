from class_person import Person
import random

class Client(Person):
    def __init__(self,name,last_name,age,dni,cel,account):
        super().__init__(name,last_name,age,dni,cel)
        self.__account = account
        self.__cart = []
        self.__orders = {}

    def __str__(self):
        return f'Client: {super().__str__()}\n Account: {self.__account}'
    
    def put_in_cart(self,items):
        in_cart = self.__cart.append(items)
        return self.__cart
    
    def buy(self):
        generate_order = self.__orders.update({
            'order': random.random(),
            'client':f'{self.clear_last_name} , {self._name}',
            'items':self.__cart
        })
        return self.__orders
    
