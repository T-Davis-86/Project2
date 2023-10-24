from Line import Line 
from Customer import Customer
from Food import Food
from os import system, name # importing what the operating system is to clear the terminal screen to keep it clean
from time import sleep 

def clear():
  if name == 'nt':
    _ = system('cls')
  # Clear screen for mac and linux
  else:
     _ = system('clear')
  # Clear screen for Windows

# initializing a Line Object
line = Line()        

# Creating customer objects
order1 = Customer("Ian")
order2 = Customer('Alan')
order3 = Customer('Marsha') 
order4 = Customer('Michelle')

# Adding customers to the queue
line.addPerson(order1)
line.addPerson(order2)
line.addPerson(order3)

# Creating the food objects
meal1 = Food("Burger", 5.99)
meal2 = Food("Coca-Cola", 1.99)
meal3 = Food("Pizza", 2.99)
meal4 = Food("Ice-Cream", 3.45)
meal5 = Food("Fries", 2.50)

# Adding the food objects to the customers that are in the queue
order1.addFood(meal1)
order1.addFood(meal5)
order1.addFood(meal2)
order2.addFood(meal2)
order2.addFood(meal5)
order3.addFood(meal3)
order3.addFood(meal2)

# Displaying the queue of customers and their food orders
line.Display_Order()

# Using sleep to give the user time to see the action and then using clear to clear the console to keep things neat
sleep(5)
clear()

#removing people
line.removePerson()
sleep(5)
clear()
line.removePerson()
sleep(5)
clear()
line.addPerson(order4)
print("\n")
order4.addFood(meal4)
sleep(5)
clear()
line.Display_Order()
sleep(5)
clear()
line.removePerson()
sleep(5)
clear()
line.removePerson()
sleep(5)
clear()

