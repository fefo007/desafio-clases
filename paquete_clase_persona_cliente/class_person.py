class Person():
    def __init__(self,name,last_name,age,dni,cel):
        self._name = name
        self._last_name = last_name 
        self.__age  = age
        self.__dni  = dni
        self.__cel = cel
    
    def say_hi(self):
        return f'Hola mi nombre es {self._name} {self._last_name}'
    
    def my_age(self):
        return f'Tengo {self.__age} años'
    
    def my_dni(self):
        return f'Mi DNI es {self.__dni}'
    
    def my_cel(self):
        return f'Mi celular es {self.__cel}'

    def __str__(self):
        return f'object Person values are: \nname:{self._name}\nlast_name:{self._last_name}\n age:{self.__age}\n dni:{self.__dni}\n cel:{self.__cel}'
    

