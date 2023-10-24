# creates an array to store elements
class Line():
  def __init__(self):
    self._line = []  # Creates the customer queue
    self._earnings = 0.0 # Using to keep track of daily earnings for the restaurant

# inserts person into the end of the line
  def addPerson(self,person): 
    self._line.append(person) # Adds the customer to the back of the queue
    print("Serving 1!\n") # Used to indicate that a customer has been added to the queue
      
  #removes the person at the front of the line
  def removePerson(self): 
    customer = self._line[0] # initializing customer as the position that is to be removed
    print("Now serving",customer._name,":")
    for items in customer._order: # Iterating through the customers orders
      print(items.f_name)  
    print("\n")
    self._earnings += customer._tot # Incrementing the daily earnings
    self._line.pop(0) # Removes the customer from the queue
    if len(self._line) == 0:
      print("Line is empty!")  # Once the queue is empty this prints out what the final earnings
      print("Total earnings to date: ${0:.2f}".format(self._earnings,))
    else:
      print("Updated line!\n")
      self.Display_Order()  

  # Displays the customer's order 
  def Display_Order(self,x = 0): 
    if len(self._line) == x: # Setting the base case to exit the recursion
      return self._line
    customer = self._line[x]  # Setting customer to the position in the queue
    print(customer._name, "ordered:")
    print("------------")
    for item in customer._order:
      print(item.f_name,"......${0:.2f}".format(item.p_price))  # For the meals ordered by the customer it prints out what they ordered
    print("\n","Total: ${0:.2f}".format(customer._tot))
    print("------------\n")
    self.Display_Order(x + 1)  # Recalling its own function as part of recursion