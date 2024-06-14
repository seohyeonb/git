class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def personinfo(self):
        print(f'이름:{self.name},나이:{self.age}')

p=Person('수호',34)
p.personinfo()



class Animal():
    def __init__(self,species,age,name):
        self.species=species
        self.age=age
        self.name=name
    def eat(self):
        print(f'{self.name}이 먹이를 먹습니다')
    def eat(self):
        print(f'{self.name}이 먹이를 먹습니다')
    def makesound(self):
        print(f'{self.name}이 소리를 냅니다')

dog=Animal('개',3,'멍멍이')
cat=Animal('고양이',2,'야옹이')

print(dog.species)
print(dog.age)
