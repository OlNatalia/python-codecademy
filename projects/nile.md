## project challenge - The Nile

The Nile fullfilment agency brings everything you could possibly want straight to your door! Use your knowledge of Python functions and how to manipulate arguments to help automate practices for the biggest world-changing company.

If you get stuck during this project, check out the project walkthrough video which can be found in the help menu.


Tasks: 0/23 Complete


Not Just A River In Egypt

1.

At The Nile our biggest concern is our consumers, and our biggest cost is delivering their goods to them. We want to develop a program that will help us minimize these costs so we can continue making everyone happy.

First we’ll need to calculate these costs using a function that you’re going to write called calculate_shipping_cost().

Give calculate_shipping_cost three parameters: from_coords, to_coords, and shipping_type.

2.

Both from_coords and to_coords are tuples, containing first the latitude and then the longitude. Since our get_distance() function looks for all four as separate arguments, we’ll need to separate these variables out.

Inside calculate_shipping_cost unpack those tuples into from_lat, from_long, to_lat, and to_long.

3.

Now call get_distance(from_lat, from_long, to_lat, to_long) and save the result as distance.

There’s other ways to separate those two coordinates when calling this function, how would you have done it?

4.

Next, get the shipping_rate by using the provided SHIPPING_PRICES dictionary and fetching the key passed in as shipping_type.

5.

Calculate the price by multiplying the distance by the shipping_rate.

6.

Finally, return the formatted price, created by calling the provided format_price() on the price itself.

7.

What about our shoppers who hastily purchase goods without indicating their shipping type? Let’s give our function a default argument for shipping_type. Since they’re in such a hurry let’s make the default argument 'Overnight'. They’ll be happier to get what they ordered earlier, and we’ll be happier because they paid more money for it. It’s a win-win!

8.

Want to make sure you wrote the function correctly? Try calling test_function(calculate_shipping_cost) after your function definition.
Careers At The Nile

9.

At The Nile, we have a joke. Without our fantastic drivers, who fulfill orders every day, we’d just be sitting with millions of toys, electronics, and clothing in warehouses to ourselves.

Our team is important, and we want to make sure the hardest workers find their home in our careers. In order to do that, we need to figure out who the best person is for each job.

Write a function called calculate_driver_cost() with distance as the first parmameter, and as many drivers as are available as positional arguments after that, as drivers.

10.

In order to find the best person, we need to calculate how much it would cost for any of the drivers to fulfill this order.

Create two new variables, cheapest_driver and cheapest_driver_price. Set them both to None.

11.

Now let’s iterate over every driver in drivers. Use a for loop.

12.

First calculate the driver_time for each driver by multiplying driver.speed by distance.

13.

Next calculate the price_for_driver by multiplying driver.salary by driver_time.

14.

Now we want to check if the current driver is the cheapest driver we’ve looked at.

First, we’ll check if cheapest_driver is None, this likely means this is the first driver we’ve looked at.

In that case, set cheapest_driver equal to driver and then set cheapest_driver_price equal to price_for_driver.

15.

In an elif statment, check if price_for_driver is less than cheapest_driver_price. This means that our current driver is cheaper than the driver stored in cheapest_driver.

Update cheapest_driver to be equal to driver and update cheapest_driver_price to be equal to price_for_driver.

16.

After outdenting out of our elif statement and the for loop, return cheapest_driver_price and cheapest_driver.
The Nile Exclusive

17.

Great first day, friend! Let’s try and figure out all the money you’ve saved us today.

Let’s define a function called calculate_money_made().

This function will be passed a number of Trip IDs with corresponding trip information as arguments, so let’s just take any keyword arguments passed into it. Store them all as trips!

18.

Let’s start a counter at 0. Create a variable called total_money_made that will count up for us.

19.

Iterate through every trip_id and trip in the trips dictionary.

20.

Calculate the trip revenue into the variable trip_revenue by calculating trip.cost minus trip.driver.cost.

21.

Add up that sweet revenue by incrementing total_money_made by trip_revenue.

22.

Outside your for loop, return the total!

23.

Congratulations! You’ve been a real life-saver around these parts. We broke up functions using arbitrary and default parameters! Remember you can test your function by calling test_function(calculate_money_made) afterwards!


https://www.youtube.com/watch?v=cPIxKT6li6o
(mike dane - Python Walkthrough The Nile)
 

#### Ausgangscode

```py
# script.py

from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost() here:


# Test the function by calling 
# test_function(calculate_shipping_cost)

# Define calculate_driver_cost() here


# Test the function by calling 
# test_function(calculate_driver_cost)

# Define calculate_money_made() here


# Test the function by calling 
# test_function(calculate_money_made)
```


```py
# nile.py

from math import sin, cos, atan2, sqrt

def get_distance(from_lat, from_long, to_lat, to_long):
  dlon = to_long - from_long
  dlat = from_lat - to_lat
  a = (sin(dlat/2)) ** 2 + cos(from_lat) * cos(to_lat) * (sin(dlon/2)) ** 2
  c = 2 * atan2(sqrt(a), sqrt(1-a))
  distance = a * c
  return distance

SHIPPING_PRICES = {
  'Ground': 1,
  'Priority': 1.6,
  'Overnight': 2.3,
}

def format_price(price):
  return "${0:.2f}".format(price)

```


```py
# test.py

def test_function(fn):
  if fn.__name__ == "calculate_shipping_cost":
    test_shipping(fn)
  if fn.__name__ == "calculate_driver_cost":
    test_driver(fn)
  if fn.__name__ == "calculate_money_made":
    test_money(fn)

def test_shipping(f):
  try:
    costs = f((0, 0), (1, 1))
  except TypeError:
    print("calculate_shipping_cost() did not provide default argument for shipping_type")
    return
  if not type(costs) is str:
    print("calculate_shipping_cost() did not format the result in a string")
    return
  if costs != "$1.04":
    print("calculate_shipping_cost((0, 0), (1, 1)) returned {}. Expected result is {}".format(costs, "$1.04"))
    return
  print("OK! calculate_shipping_cost() passes tests")

class Driver:
  def __init__(self, speed, salary):
    self.speed = speed
    self.salary = salary

  def __repr__(self):
    return "Nile Driver speed {} salary {}".format(self.speed, self.salary)

driver1 = Driver(2, 10)
driver2 = Driver(7, 20)

def test_driver(f):
  try:
    price, driver = f(80, driver1, driver2)
  except TypeError:
    print("calculate_driver_cost() doesn't expect multiple driver arguments")
    return
  if type(driver) is not Driver:
    print("calculate_driver_cost() did not return driver")
    return
  if price != 1600:
    print("calculate_driver_cost() did not provide correct final price (expected {}, received {})".format(price,1600))
    return
  if driver is not driver1:
    print("calculate_driver_cost() did not provide least expensive driver")
    return
  print("OK! calculate_driver_cost() passes tests")

class Trip:
  def __init__(self, cost, driver, driver_cost):
    self.cost = cost
    driver.cost = driver_cost
    self.driver = driver

trip1 = Trip(200, driver1, 15)
trip2 = Trip(300, driver2, 40)

def test_money(f):
  try:
    money = f(UEXODI=trip1, DEFZXIE=trip2)
  except TypeError:
    print("calculate_money_made() doesn't expect multiple trip keyword arguments")
    return
  if type(money) not in (int, float):
    print("calculate_driver_cost() did not return a number")
    return
  if money != 445:
    print("calculate_driver_cost() did not provide correct final price (expected {}, received {})".format(money, 445))
    return
  print("OK! calculate_money_made() passes tests")
```


#### Solution

```py
from nile import get_distance, format_price, SHIPPING_PRICES
from test import test_function

# Define calculate_shipping_cost() here:
def calculate_shipping_cost(from_coords, to_coords, shipping_type='Overnight'):
  from_lat, from_long = from_coords
  to_lat, to_long = to_coords
 # distance = get_distance(from_lat, from_long, to_lat, to_long)
  distance = get_distance(*from_coords, *to_coords)
  shipping_rate = SHIPPING_PRICES[shipping_type]
  price = distance * shipping_rate
  return format_price(price)


# Test the function by calling 
test_function(calculate_shipping_cost)


# Define calculate_driver_cost() here
def calculate_driver_cost(distance, *drivers):
  cheapest_driver = None
  cheapest_driver_price = None
  for driver in drivers:
    driver_time = driver.speed * distance
    price_for_driver = driver.salary * driver_time
    if cheapest_driver is None:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver
    elif price_for_driver < cheapest_driver_price:
      cheapest_driver = driver
      cheapest_driver_price = price_for_driver

  return cheapest_driver_price, cheapest_driver

# Test the function by calling 
test_function(calculate_driver_cost)


# Define calculate_money_made() here
def calculate_money_made(**trips):
  total_money_made = 0
  for trip_id, trip in trips.items():
    trip_revenue = trip.cost - trip.driver.cost
    total_money_made = trip_revenue
  return total_money_made


# Test the function by calling 
test_function(calculate_money_made)
```
