import car_screen_clear as sc
import car_cnotine as cn
from car import car
from random import randint

active = True

car1 = car(brand="Ballsmobile", color="Gamboge", amount=69)
car2 = car(brand="2001 Honda Civic Type-R", color="Gray", amount=3)
car3 = car(brand="Tesla Model Y", color="Gray", amount=759000)

car_list = [car1, car2, car3]

def main():
    global active

    while active:
        sc.cls()
        print("The Car Thing")
        if cn.cnotine("Please just press 2 right now, this one really sucks."):
            for car in car_list:
                print(f"{car.brand}, {car.color}, {car.amount} of them [ID {car.id}]")
            select = cn.multi_cnotine("Which car would you like to do something to?", len(car_list)) - 1
            type = cn.multi_cnotine("What would you like to do to this car?\n[1 - Magically change its type; 2 - Repaint; 3 - Create or remove instances]", 3)
            if type == 1:
                car_list[select].brand = input("What would you like to change it to?\n")
                input(f"Congrats, it's now {car_list[select].brand}. Wonderful.")
            elif type == 2:
                car_list[select].color = input("In what color?\n")
                input(f"What a spectacular {car_list[select].color} paint job.")
            elif type == 3:
                car_list[select].amount = input("How many do you want to have?\n")
                try:
                    if car_list[select].amount > 0:
                        input(f"You now have {car_list[select].amount}. Great.")
                    elif car_list[select].amount == 0:
                        input("They're all gone now. Too bad.")
                        car_list.pop(select)
                    else:
                        input("Negative numbers have no representation in the real world. The universe explodes and you fucking die.")
                        active = False
                except Exception:
                    input("The universe, as if to say 'fuck off' at your non-numeric input, immediately undergoes false vacuum decay.\nEverything, ever, dies.")
                    active = False
        else:
            active = False

main()