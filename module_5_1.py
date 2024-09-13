class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors


    def go_to(self, new_floor: int, ):
        if self.number_of_floors < new_floor or self.number_of_floors < 1:
            print('Такого этажа не существует')
        else:
            for i in range(new_floor):
                print(i+1)

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)