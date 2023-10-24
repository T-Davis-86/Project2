# creates a customer that has a name and a desired food
class Customer():
  def __init__(self,name):
    self._order = [] # The list of the customers orders
    self._name = name  # Customer's Name
    self._tot = 0.0 # Used to keep track of the amount owed by the customers


  #adds food to a customer's order
  def addFood(self,meal):   
    self._order.append(meal)  # Adds the meal to the customers order
    self._tot += meal.p_price  # Increments the total for the customer