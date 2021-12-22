def my_car(car_name, car_color, mileage, owners_count, manufectur_year):
    print(f"My car name is {car_name} and its color is {car_color}.")
    print(f"the car mileage is {mileage} and {owners_count} peple ownd her befor.")
    print(f"the car manufectur year is {manufectur_year}")


favorit_color = "Dark greey"
first_owner = 1
my_car("yundai" + "I30", favorit_color, 120000 + 50000, first_owner + 1, 2009)

input("Is it corect? ")

name = input("\nCar model: ")
color = input("color you like: ")
mileage = input("Choose a mileage (thousands of kilometers) 50, 100, 150, 200: ")
owners = int(input("number of owners befor the last one: ")) + 1
year = input("year of manufacture: ")
print("")

my_car(name, color + " color" , mileage + ("0" * 3), owners, year)

