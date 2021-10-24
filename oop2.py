
class CarMercedez:

    year = 2008
    make = "mercedez"
    model = "c200" 


    def start(self):
        print("Заводим двигатель")

    def stop(self):
        print("Отключаем двигатель")



car_a = CarMercedez()

car_b = CarMercedez()

car_a.start()

print('car_a.model', car_a.year)
car_a.year = 2020
print('car_a.year', car_a.year)
print('car_b.year', car_b.year)

def brabus_switch_gear(gear_number):
    print(f'switched gear - {gear_number}')
car_b.custom_switch_gear = brabus_switch_gear
car_b.custom_switch_gear(1)
car_b.custom_switch_gear(2)
car_b.custom_switch_gear(3)
print(car_b.__dict__)
print(car_a.__dict__)

car_stopped =False
def break_brambo(car_stopped):
    car_stopped = True
    print("car is stopped by brambo's breaks")
    print(car_stopped)
car_a.break_activated = break_brambo
car_a.break_activated(car_stopped)
