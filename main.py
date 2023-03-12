import csv
from datetime import datetime


# Create Menu.txt file
with open('Menu.txt', 'w') as f:
    f.write("* Please Choose a Pizza Base:\n"
            "1: Classic\n"
            "2: Margherita\n"
            "3: TurkPizza\n"
            "4: PlainPizza\n"
            "* and sauce of your choice:\n"
            "11: Olives\n"
            "12: Mushrooms\n"
            "13: GoatCheese\n"
            "14: Meat\n"
            "15: Onions\n"
            "16: Corn\n"
            "* Thank you!\n")


# Define superclass "Pizza"
class Pizza:
    def __init__(self, description, cost):
        self.description = description
        self.cost = cost

    def get_description(self):
        return self.description

    def get_cost(self):
        return self.cost


# Define subclasses "ClassicPizza", "MargheritaPizza", "TurkPizza", and "PlainPizza"
class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Classic pizza", 10.0)


class MargheritaPizza(Pizza):
    def __init__(self):
        super().__init__("Margherita pizza", 12.0)


class TurkPizza(Pizza):
    def __init__(self):
        super().__init__("Turk pizza", 15.0)


class PlainPizza(Pizza):
    def __init__(self):
        super().__init__("Plain pizza", 8.0)


# Define superclass "Decorator"
class Decorator(Pizza):
    def __init__(self, component):
        self.component = component

    def get_cost(self):
        return self.component.get_cost() + Pizza.get_cost(self)

    def get_description(self):
        return self.component.get_description() + ' ' + Pizza.get_description(self)


# Define subclasses for each sauce
class Olives(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "olives"
        self.cost = 2.0


class Mushrooms(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "mushrooms"
        self.cost = 1.5


class GoatCheese(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "goat cheese"
        self.cost = 3.0


class Meat(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "meat"
        self.cost = 2.5


class Onions(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "onions"
        self.cost = 1.0


class Corn(Decorator):
    def __init__(self, component):
        super().__init__(component)
        self.description = "corn"
        self.cost = 1.0


# Define main function
def main():
    # Print the menu
    with open('Menu.txt', 'r') as f:
        print(f.read())

    # Let the user choose a pizza base
    while True:
        pizza_choice = input("Please choose a pizza base (1-4): ")
        if pizza_choice in ['1', '2', '3', '4']:
            break
        else:
            print("Invalid input. Please try again.")

    # Create the pizza object based on user's choice
    if pizza_choice == '1':
        pizza = ClassicPizza()
    elif pizza_choice == '2':
        pizza = MargheritaPizza()
    elif pizza_choice == '3':
        pizza = TurkPizza()
    elif pizza_choice == '4':
        pizza = PlainPizza()

    # Ask user to choose a sauce
    print("Please choose a sauce for your pizza:")
    print("11: Olives")
    print("12: Mushrooms")
    print("13: Goat Cheese")
    print("14: Meat")
    print("15: Onions")
    print("16: Corn")
    sauce_choice = int(input("Enter the sauce number: "))

    # Create the sauce object based on user's choice
    if sauce_choice == 11:
        sauce = Olives(pizza)
    elif sauce_choice == 12:
        sauce = Mushrooms(pizza)
    elif sauce_choice == 13:
        sauce = GoatCheese(pizza)
    elif sauce_choice == 14:
        sauce = Meat(pizza)
    elif sauce_choice == 15:
        sauce = Onions(pizza)
    elif sauce_choice == 16:
        sauce = Corn(pizza)

    # Get the total cost of the pizza and sauce
    total_cost = sauce.get_cost()

    # Get user information for payment
    name = input("Please enter your name: ")
    id_number = input("Please enter your ID number: ")
    credit_card_number = input("Please enter your credit card number: ")
    credit_card_password = input("Please enter your credit card password: ")

    # Save the order information to the Orders_Database.csv file
    now = datetime.now()
    order_time = now.strftime("%Y-%m-%d %H:%M:%S")
    with open("Orders_Database.csv", mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, id_number, credit_card_number, sauce.get_description(), total_cost, order_time, credit_card_password])

    print("Thank you for your order! Your pizza will be ready soon.")
