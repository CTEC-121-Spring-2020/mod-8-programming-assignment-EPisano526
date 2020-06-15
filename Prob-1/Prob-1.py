# Module 8
#   Programming Assignment 11
#     Prob-1.py

# Your code below


class Car:
    def __init__(self, _make, _model, _year):
        self._make = _make
        self._model = _model
        self._year = _year

    def get_make(self):
        return self._make

    def get_model(self):
        return self._model

    def get_year(self):
        return self._year

    def set_make(self, make):
        self._make = make

    def set_model(self, model):
        self._model = model

    def set_year(self, year):
        self._year = year


def TestCar(carlot):
    for car in carLot:
        print(car.get_model(), car.get_make(), car.get_year())

    for i in range(0, len(carLot)):
        carLot[i].set_make("make_" + str(i))
        carLot[i].set_year("year_" + str(i))
        carLot[i].set_model("model_" + str(i))

    for car in carLot:
        print(car.get_model(), car.get_make(), car.get_year())


if __name__ == "__main__":
    carLot = []
    car0 = Car("Toyota", "Corolla", 2009)
    car1 = Car("Honda", "Accord", 1998)
    car2 = Car("Toyota", "Prius", 2007)
    car3 = Car("Ford", "F150", 2014)
    car4 = Car("Hyundai", "Elantra", 2004)
    carLot.append(car0)
    carLot.append(car1)
    carLot.append(car2)
    carLot.append(car3)
    carLot.append(car4)
    TestCar(carLot)
