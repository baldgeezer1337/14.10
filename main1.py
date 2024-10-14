class Person():
    def __init__(self, name, age):
        self.name=name
        self.age=age

    def print_info(self):
        print(f'Personas vārds {self.name}, personas vecums {self.age}')

    def apsveikt(self):
        print(f'Apsveikam {self.name}')


class Skolotajs(Person):
    def __init__(self, name, age, prieksmetu_skaits):
        super().__init__(name, age)
        self.prieksmeti=[]
        for i in range(prieksmetu_skaits):
            a=input("Ievadiet prieksmetu: ")
            self.prieksmeti.append(a)


    def print_info(self):
        print(f'Skolotaja vārds {self.name}, skolotaja vecums {self.age}, skolotaja prieksmets {self.prieksmeti}')

p=Skolotajs("Herald", 32, 2)
p.print_info() 