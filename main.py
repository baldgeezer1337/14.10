import random
'''
def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")


def get_name():
    return input("Name: ")


def get_house():
    return input("House: ")


if __name__ == "__main__":
    main() '''


'''#Iepakojot šo kortežu tā, lai mēs varētu atgriezt abus vienumus mainīgajam ar nosaukumu student, mēs varam modificēt savu kodu šādi.

def main():
    student = get_student()
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return (name, house)


if __name__ == "__main__":
    main() '''


'''
def main():
    name, house = get_student()
    print(f"{name} from {house}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return name, house


if __name__ == "__main__":
    main() '''

'''
def main():
    student = get_student()
    if student[0] == "Padma":
        student[1] = "Ravenclaw"
    print(f"{student[0]} from {student[1]}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return [name, house]


if __name__ == "__main__":
    main() '''

'''
#Šajā īstenošanā var izmantot arī vārdnīcu. Atcerieties, ka vārdnīcas nodrošina atslēgu un vērtību pāri.
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    student = {}
    student["name"] = input("Name: ")
    student["house"] = input("House: ")
    return student


if __name__ == "__main__":
    main() '''

'''
#Tomēr mūsu kodu var vēl vairāk uzlabot. Ievērojiet, ka ir nevajadzīgs mainīgais. Mēs varam noņemt student = {}, jo mums nav jāizveido tukša vārdnīca.
def main():
    student = get_student()
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main() '''
'''
#Mēs varam nodrošināt savu īpašo gadījumu ar Padma mūsu koda vārdnīcas versijā.
def main():
    student = get_student()
    if student["name"] == "Padma":
        student["house"] = "Ravenclaw"
    print(f"{student['name']} from {student['house']}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return {"name": name, "house": house}


if __name__ == "__main__":
    main() '''
'''
class Student:
    ...
def main():
    student = get_student()
    print(f"{
student.name
} from {
student.house
}")


def get_student():
    student = Student()
    
student.name = input("Name: ")
    
student.house = input("House: ")
return student
if __name__ == "__main__":
        main() '''
'''
#Turklāt mēs varam izveidot pamatu atribūtiem, kas ir sagaidāmi objektā, kura klase ir Student. Mēs varam modificēt savu kodu šādi:

class Student:
    def __init__(self, name, house):
        self.name= name
        self.house = house


def main():
    student = get_student()
    print(f"{
student.name
} from {
student.house
}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    student = Student(name, house)
    return student


if __name__ == "__main__":
    main() '''
'''
class Student:
    def __init__(self, name, house):
        self.name= name       
        self.house= house

def main():
    student = get_student()
    print(f"{
student.name
} from {
student.house
}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main() '''
'''
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name= name
        self.house= house

def main():
    student = get_student()
    print(f"{
student.name
} from {
student.house
}")


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main() '''
'''
class Student:
    def __init__(self, name, house, patronus):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name= name
        self.house= house
        self.patronus = patronus

    def __str__(self):
        return f"{
self.name
} from {
self.house
}"


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ")
    return Student(name, house, patronus)


if __name__ == "__main__":
    main() '''
'''
class Student:
    def __init__(self, name, house, patronus=None):
        if not name:
            raise ValueError("Missing name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        if patronus and patronus not in ["Stag", "Otter", "Jack Russell terrier"]:
            raise ValueError("Invalid patronus")
        self.name= name
        self.house= house
        self.patronus = patronus

    def __str__(self):
        return f"{
self.name
} from {
self.house
}"

    def charm(self):
        match self.patronus:
            case "Stag":
                return ""
            case "Otter":
                return ""
            case "Jack Russell terrier":
                return ""
            case _:
                return ""


def main():
    student = get_student()
    print("Expecto Patronum!")
    print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    patronus = input("Patronus: ") or None
    return Student(name, house, patronus)


if __name__ == "__main__":
    main() '''
'''
#Pirms turpināt, ļaujiet mums noņemt mūsu patrona kodu. Mainiet savu kodu šādi:3
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self.name= name
        self.house= house

    def __str__(self):
        return f"{
self.name
} from {
self.house
}"


def main():
    student = get_student()
    student.house= "Number Four, Privet Drive"
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main() '''
'''
class Student:
    def __init__(self, name, house):
        if not name:
            raise ValueError("Invalid name")
        self.name= name
        self.house= house

    def __str__(self):
        return f"{
self.name
} from {
self.house
}"

    # Getter for house
    @property
    def house(self):
        return self._house

    # Setter for house
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main() '''
'''
#Papildus mājas nosaukumam mēs varam aizsargāt arī mūsu studenta vārdu. Mainiet savu kodu šādi:

class Student:
    def __init__(self, name, house):
        self.name= name
        self.house= house

    def __str__(self):
        return f"{
self.name
} from {
self.house
}"

    # Getter for name
    @property
    def name(self):
        return self._name

    # Setter for name
    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Invalid name")
        self._name = name

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main() '''


'''
class Hat:
    def __init__(self):
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    def sort(self, name):
        print(name, "is in", random.choice(self.houses))


hat = Hat()
hat.sort("Harry") 
'''
'''
class Hat:

    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


Hat.sort("Harry") '''

'''
#Atgriežoties pie students.py,mēs varam modificēt savu kodu šādi, risinot dažas neizmantotās iespējas saistībā ar @classmethod:

class Student:
    def __init__(self, name, house):
        self.name= name
        self.house= house

    def __str__(self):
        return f"{
self.name
} from {
self.house
}"

    @classmethod
    def get(cls):
        name = input("Name: ")
        house = input("House: ")
        return cls(name, house)


def main():
    student = Student.get()
    print(student)


if __name__ == "__main__":
    main() '''
'''
class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
    self.name= name
    ...


class Student(Wizard):
    def __init__(self, name, house):
        super().__init__(name)
        self.house= house

    ...


class Professor(Wizard):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    ...


wizard = Wizard("Albus")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
... '''