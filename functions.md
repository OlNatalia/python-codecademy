# Python functions

## Introduction to Functions

In programming, as we start to write bigger and more complex programs, one thing we will start to notice is we will often have to repeat the same set of steps in many different places in our program.

Let’s imagine we were building an application to help people plan trips! When using a trip planning application we can say a simple procedure could look like this:

 1. Establish your origin and destination
 2. Calculate the distance/route
 3. Return the best route to the user

We will perform these three steps every time users have to travel between two points using our trip application. In our programs, we could rewrite the same procedures over and over (and over) for each time we want to travel, but there’s a better way! Python gives us a useful concept called functions.

**Functions are a convenient way to group our code into reusable blocks.**    
A function contains a sequence of steps that can be performed repeatedly throughout a program without having to repeat the process of writing the same code again.


You’ll know how to:

- Write a function and return values from it.
- Allow functions to take custom input.
- Experiment with how functions access our other python code.

### Instructions

Review the visual for the function navigation_steps().

Notice how the function navigation_steps() serves as a container for the three steps in the procedure and can be reused across multiple users as they plan their trips to different locations. 

<br>

Why Functions?

Let’s come back to the trip planning application we just discussed in the previous exercise. The steps we talked about for our program were:

 1. Establish an origin and destination
 2. Calculate the distance/route
 3. Return the best route 

If we were to convert our steps into Python code, a very simple version that plans a trip between two popular New York tourist destinations might look like this:

print("Setting the Empire State Building as the starting point and Time Square as our destination.")

```py 
print("Calculating the total distance between our points.") 
 
print("The best route is by train and will take approximately 10 minutes.") 
```

Anytime we want to go between these two points we would need to run these three print statements (for now we can assume the best route and time will stay the same).

If our program now had 100 new people trying to find the best directions between the Empire State Building and Times Square, we would need to run each of our three print statements 100 times!

Now, if you’re thinking about using a loop here, your intuition would be totally right! Unfortunately, we won’t be always traveling between the same two locations which means a loop won’t be as effective when we want to customize a trip. We will address this in the upcoming sections!

For now, let’s gain an appreciation for functions.

Instructions

1.

Run the pre-written print() statements to see what they output.

2.

Write the same set of print statements three more times. Run the code again and see the output.

3.

Hopefully now you have some perspective about your life without functions!

In the next section, we will learn how we can refactor our code to utilize functions to reuse code.

Click Run your code again and then click Next to continue.
print("Setting the Empire State Building as the starting point and Time Square as our destination.")
print("Calculating the total distance between our points.") 
print("The best route is by train and will take approximately 10 minutes.") 

---

## Defining a Function

A function consists of many parts, so let’s first get familiar with its core - a function definition.

Here’s an example of a function definition:

```py
def function_name():
  # functions tasks go here
```

There are some key components we want to note here:

    The def keyword indicates the beginning of a function (also known as a function header). The function header is followed by a name in snake_case format that describes the task the function performs. It’s best practice to give your functions a descriptive yet concise name.

    Following the function name is a pair of parenthesis ( ) that can hold input values known as parameters (more on parameters later in the lesson!). In this example function, we have no parameters.

    A colon : to mark the end of the function header.

    Lastly, we have one or more valid python statements that make up the function body (where we have our python comment).

Notice we’ve indented our # function tasks go here comment. Like loops and conditionals, code inside a function must be indented to show that they are part of the function.

Here is an example of a function that greets a user for our trip planning application:

```py
def trip_welcome():
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")
```

:memo: Note: Pasting this code into the editor and clicking Run will result in an empty output terminal. The print() statements within the function will not execute since our function hasn’t been used. We will explore this further in the next exercise; for now, let’s practice defining a function.

### Instructions

1.

Two of the most common NYC attractions include the Empire State Building and Times Square.

In travel.py, we’ll write a function that prints the directions via subway from the Empire State Building to Times Square.

First, define a function, directions_to_timesSq(). Leave the body of the function empty for now.

Note: When we run the code, we will see an error: “IndentationError: expected an indented block”. This will occur when we don’t populate a function with any statements. We will populate it with code in the next step.

2.

Within the body of the function, use three print() statements to output the following directions:

Walk 4 mins to 34th St Herald Square train station
Take the Northbound N, Q, R, or W train 1 stop
Get off the Times Square 42nd Street stop

Remember, if you run your code, you shouldn’t see any output in the terminal at this point. Check out the hint if you want to see how to see the output (we will be doing it in the next section as well!)

```py
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station")
  print("Take the Northbound N, Q, R, or W train 1 stop")
  print("Get off the Times Square 42nd Street stop")
```


## Calling a Function

Now that we’ve practiced defining a function, let’s learn about calling a function to execute the code within its body.

The process of executing the code inside the body of a function is known as calling it (This is also known as “executing a function”). To call a function in Python, type out its name followed by parentheses ( ).

Let’s revisit our directions_to_timesSq() function :

```py
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")
```

To call our function, we must type out the function’s name followed by a pair of parentheses and no indentation:

```py
directions_to_timesSq()
```

Calling the function will execute the print statements within the body (from the top statement to the bottom statement) and result in the following output:

Walk 4 mins to 34th St Herald Square train station.
Take the Northbound N, Q, R, or W train 1 stop.
Get off the Times Square 42nd Street stop.

Now it’s your turn to call a function!

### Instructions

1.

Call the directions_to_timesSq() function.

Click Run to see it execute and print out.

2.

Add an additional print statement to our directions_to_timesSq() function.

Have the statement print "Take lots of pictures!"

Run your code again and see how your output changes.

```py
def directions_to_timesSq():
  print("Walk 4 mins to 34th St Herald Square train station.")
  print("Take the Northbound N, Q, R, or W train 1 stop.")
  print("Get off the Times Square 42nd Street stop.")
  print("Take lots of pictures!")

directions_to_timesSq()
```


## Whitespace & Execution Flow

Consider our welcome function for our trip planning application:

```py
def trip_welcome():
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")
```

The three print statements are all run together when trip_welcome() is called. This is because they have the same base level of indentation (2 spaces).

In Python, the amount of whitespace tells the computer what is part of a function and what is not part of that function.

If we wanted to write another statement outside of trip_welcome(), we would have to unindent the new line:

```py
def trip_welcome():
  # Indented code is part of the function body
  print("Welcome to Tripcademy!") 
  print("Let's get you to your destination.")
 
# Unindented code below is not part of the function body
print("Woah, look at the weather outside! Don't walk, take the train!")
 
trip_welcome()
```

Our trip_welcome() function steps will not print Woah, look at the weather outside! Don't walk, take the train! on our function call. The print() statement was unindented to show it was not a part of the function body but rather a separate statement.

We would see the following output from this program:

Woah, look at the weather outside! Don't walk, take the train!
Welcome to Tripcademy!
Let's get you to your destination.

Lastly, note that the execution of a program always begins on the first line. The code is then executed one line at a time from top to bottom. This is known as execution flow and is the order a program in python executes code.

Woah, look at the weather outside! Don't walk, take the train! was printed before the print() statements from the function trip_welcome().

Even though our function was defined before our lone print() statement, we didn’t call our function until after.

Let’s play around with indentation and the flow of execution!

### Instructions

1.

We are going to help our trip planner users figure out if they should travel today based on the weather. Let’s let our users know we can check the weather for them.

Write a print() statement that will output Checking the weather for you!.

2.

We took a look outside and see a bright sunny day. Write a function called weather_check() that will print a message to our users that it’s a great day to travel! The function should output:

Looks great outside! Enjoy your trip.

Note: Don’t call your function just yet! We will do that in the next step.

3.

Oh no! It looks like some clouds came in and it started raining. Our users shouldn’t go on a trip in the rain. In our weather_check() function add a second print() statement under the first one which prints a warning message for our travelers! It should print:

False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.

4.

Call the function weather_check().

5.

Unindent your final print statement in your weather_check() function. Run the program again.

What is different?    
Remember to unindent the front of the second print statement in your weather_check() function. You should notice a different order in your output terminal due to the change in the indentation. 

```py
# Your code below: 
print("Checking the weather for you!")
def weather_check():
  print("Looks great outside! Enjoy your trip.")
print("False Alarm, the weather changed! There is a thunderstorm approaching. Cancel your plans and stay inside.")

weather_check()
```


## Parameters & Arguments

Let’s return to our trip_welcome() function one more time! Let’s modify our function to give a welcome that is a bit more detailed.

```py
def trip_welcome():
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to Times Square today.")
 
trip_welcome()

# This will output:
Welcome to Tripcademy!
Looks like you're going to Times Square today.
```

Our function does a really good job of welcoming anyone who is traveling to Times Square but a really poor job if they are going anywhere else. In order for us to make our function a bit more dynamic, we are going to use the concept of function parameters.

Function parameters allow our function to accept data as an input value. We list the parameters a function takes as input between the parentheses of a function ( ).

Here is a function that defines a single parameter:

```py
def my_function(single_parameter)
  # some code
```

In the context of our trip_welcome() function, it would like this:

```py
def trip_welcome(destination):
  print("Welcome to Tripcademy!") 
  print("Looks like you're going to " + destination + " today.")
```

In the above example, we define a single parameter called destination and apply it in our function body in the second print statement. We are telling our function it should expect some data passed in for destination that it can apply to any statements in the function body.

But how do we actually use this parameter? Our parameter of destination is used by passing in an argument to the function when we call it.

```py
trip_welcome("Times Square")

# This would output:
Welcome to Tripcademy!
Looks like you're going to Times Square today. 
```

To summarize, here is a quick breakdown of the distinction between a parameter and an argument:

    The parameter is the name defined in the parenthesis of the function and can be used in the function body.

FD1

    The argument is the data that is passed in when we call the function and assigned to the parameter name.

FD2

Let’s write a function with parameters and call the function with an argument to see it all in action!

### Instructions

1.

We want to create a program that allows our users to generate the directions for their upcoming trip!

Create a function called generate_trip_instructions() that defines one parameter called location.

Note: Since we did not define any code in our function yet, we will receive an error in our output terminal. Don’t worry, we will be filling in the code in the next step.

2.

generate_trip_instructions() should print out the following:

Looks like you are planning a trip to visit `<location>`

Where `<location>` will represent the destination parameter.

3.

generate_trip_instructions() should also let our users know they can reach their location using public transit.

Let’s have generate_trip_instructions()also print out the following on a new line:

You can use the public subway system to get to <location>

Where <location> will represent the location parameter.

4.

Time for some greenery! Let’s see what happens when we call the function and input the argument "Central Park", a backyard wonder in the heart of New York City.

5.

The day trip is over and we need to get back to the train station to head home. Change the argument to "Grand Central Station" and call the function again.

What changed in the output?

```py
# Your code below:
def generate_trip_instructions(location):
  print("Looks like you are planning a trip to visit "+ location)
  print("You can use the public subway system to get to " + location)

# generate_trip_instructions("Central Park")
generate_trip_instructions("Grand Central Station")
```


## Multiple Parameters

Using a single parameter is useful but functions let us use as many parameters as we want! That way, we can pass in more than one input to our functions.

We can write a function that takes in more than one parameter by using commas:

```py
def my_function(parameter1, parameter2, parameter3)
  # Some code

When we call our function, we will need to provide arguments for each of the parameters we assgined in our function definition.

# Calling my_function
my_function(argument1, arugment2)
```

For example take our trip applications trip_welcome() function that has two parameters:

```py
def trip_welcome(origin, destination)
  print("Welcome to Tripcademy")
  print("Looks like you are traveling from " + origin)
  print("And you are heading to " + destination)
```

Our two parameters in this function are origin and destination. In order to properly call our function, we need to pass argument values for both of them.

The ordering of your parameters is important as their position will map to the position of the arguments and will determine their assigned value in the function body (more on this in the next exercise!).

Our function call could look like:

```py
trip_welcome("Propspect Park", "Atlantic Terminal")
```

In this call, the argument value of "Prospect Park" is assigned to be the origin parameter, and the argument value of"Atlantic Terminal" is assigned to the destination parameter.

```py
# The output would be:
Welcome to Tripcademy
Looks like you are traveling from Prospect Park
And you are heading to Atlantic Terminal
```

Let’s practice writing and calling a multiple parameter function!

### Instructions

1.

Our travel application users want to calculate the total expenses they may have to incur on a trip.

Write a function called calculate_expenses that will have four parameters (in exact order):

    plane_ticket_price
    car_rental_rate
    hotel_rate
    trip_time

Each of these parameters will account for a different expense that our users will incur.

Note: Like before, if we run this function now, we will get an error since there are no statements in the body.

2.

Within the body of the function, let’s start to make some calculations for our expenses. First, let’s calculate the total price for a car rental.

Create new variable called car_rental_total that is the product of car_rental_rate and trip_time.

3.

Next, we want to apply the same logic but for our hotel_rate.

Create new variable called hotel_total that is the product of hotel_rate and trip_time.

We also have a coupon to give our users some cashback for their hotel visit so subtract 10 from that total in the same statement. Woohoo, coupons! 💵

4.

Lastly, let’s print a nice message for our users to see the total. Use print to output the sum of car_rental_total, hotel_total and plane_ticket_price.

5.

Call your function with the following argument values for the parameters listed:

    plane_ticket_price : 200
    car_rental_rate : 100
    hotel_rate : 100
    trip_time: 5

```py
# Write your code below: 
#car_rental_total = 0
def calculate_expenses(plane_ticket_price, car_rental_rate, hotel_rate, trip_time):
  car_rental_total = trip_time * car_rental_rate
  hotel_total = hotel_rate * trip_time - 10
  #sum = car_rental_total + hotel_total + plane_ticket_price
  print(car_rental_total + hotel_total + plane_ticket_price)

def calculate_expenses(200, 100, 100, 5)

```

## Types of Arguments

In Python, there are **3 different types of arguments** we can give a function.

- **Positional arguments**: arguments that can be called by their position in the function definition.

- **Keyword arguments**: arguments that can be called by their name.

- **Default arguments**: arguments that are given default values.

Positional Arguments are arguments we have already been using already! Their assignments depend on their positions in the function call. Let’s look at a function called calculate_taxi_price() that allows our users to see how much a taxi would cost to their destination 🚕.

```py
def calculate_taxi_price(miles_to_travel, rate, discount):
  print(miles_to_travel * rate - discount )
```

In this function, miles_to_travel is positioned as the first parameter, rate is positioned as the second parameter, and discount is the third. When we call our function, the position of the arguments will be mapped to the positions defined in the function declaration.

```py
# 100 is miles_to_travel
# 10 is rate
# 5 is discount
calculate_taxi_price(100, 10, 5)
```

Alternatively, we can use Keyword Arguments where we explicitly refer to what each argument is assigned to in the function call. Notice in the code example below that the arguments do not follow the same order as defined in the function declaration.

```py
calculate_taxi_price(rate=0.5, discount=10, miles_to_travel=100)
```

Lastly, sometimes we want to give our function arguments default values. We can provide a default value to an argument by using the assignment operator (=). This will happen in the function declaration rather than the function call.

Here is an example where the discount argument in our calculate_taxi_price function will always have a default value of 10:

```py
def calculate_taxi_price(miles_to_travel, rate, discount = 10):
  print(miles_to_travel * rate - discount )
```

When using a default argument, we can either choose to call the function without providing a value for a discount (and thus our function will use the default value assigned) or overwrite the default argument by providing our own:

```py
# Using the default value of 10 for discount.
calculate_taxi_price(10, 0.5)
 
# Overwriting the default value of 10 with 20
calculate_taxi_price(10, 0.5, 20)
```

Let’s practice using these different types of arguments!

### Instructions

1.

Tripcademy (our trusty travel app) needs to allow passengers to plan a trip (duh).

Write a function called trip_planner() that will have three parameters: first_destination, second_destination and final_destination.

Give the final_destination parameter a default value of "Codecademy HQ".

Note: Since we did not define any code in our function yet, we will receive an error in our output terminal. Don’t worry, we will be filling in the code in the next step.

2.

First, we want to introduce the trip to users. Use print() in our function to output Here is what your trip will look like!.

3.

In our function definition let’s provide an itinerary that will describe the destinations our user will visit in order. Print a statement that follows this form:

First, we will stop in `<first_destination>`, then `<second_destination>`, and lastly `<final_destination>`

An example call to our function using positional arguments:

```py
trip_planner("London", "India", "New Zealand")

# Should output:
Here is what your trip will look like!
First, we will stop in London, then India, and lastly New Zealand
```

4.

Call the function trip_planner() with the following values for the parameters:

    first_destination: "France"

    second_destination: "Germany"

    final_destination: "Denmark"

5.

Call the function trip_planner() again with the following values for the parameters:

    first_destination: "Denmark"

    second_destination: "France"

    final_destination: "Germany"

Note the difference in your output depending on the position of your arguments.

6.

Call the function trip_planner() again using keyword arguments in this exact order:

    first_destination: "Iceland"

    final_destination: "Germany"

    second_destination: "India"

7.

Lastly, go ahead and call the function trip_planner() using only two positional arguments to see the default argument in action:

    first_destination: "Brooklyn"

    second_destination: "Queens"

```py
# Write your code below:
def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)

#trip_planner("London", "India", "New Zealand")
trip_planner("France", "Germany", "Denmark")
trip_planner("Denmark", "France", "Germany")
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India")
#trip_planner("Brooklyn", "Queens")
```

<br>

## Built-in Functions vs User Defined Functions

There are two distinct categories for functions in the world of Python. What we have been writing so far in our exercises are called User Defined Functions - functions that are written by users (like us!).

There is another category called Built-in functions - functions that come built into Python for us to use. Remember when we were using print or str? Both of these functions are built into the language for us, which means we have been using built-in functions all along!

There are lots of different built-in functions that we can use in our programs. Take a look at this example of using len() to get the length of a string:

```py
destination_name = "Venkatanarasimharajuvaripeta"
 
# Built-in function: len()
length_of_destination = len(destination_name)
 
# Built-in function: print()
print(length_of_destination)

# Would output the length of length_of_destination:
28
```

Here we are using a total of two built-in functions in our example: print(), and len().

And yes, if your wondering that is a real railway station in India!

There are even more obscure ones like help() where Python will print a link to documentation for us and provide some details:

```py
help("string")
```

Would output (shortened for readability):

NAME
    string - A collection of string constants.
 
---

MODULE REFERENCE

https://docs.python.org/3.8/library/string
 
    The following documentation is automatically generated from the Python
    source files.  It may be incomplete, incorrect or include features that
    are considered implementation detail and may vary between Python
    implementations.  When in doubt, consult the module reference at the
    location listed above.

Check out all the latest built-in functions in the official Python docs.

---

<br>

Let’s practice using a few of them. You will need to rely on the provided Python documentation links to find your answers!

### Instructions

1.

We were provided a list of prices for some gift shop items:

    T-shirt: 9.75
    Shorts: 15.50
    Mug: 5.99
    Poster: 2.00

Create a variable called max_price and call the built-in function max() with the variables of prices to get the maximum price.

Print max_price.

2.

Using the same set of prices, create a new variable called min_price and use the built-in function min() with the variables of prices to get the minimum price.

Print min_price.

3.

Use the built-in function round() to round the price of the variable tshirt_price by one decimal place.

Save the result to a variable called rounded_price and print it.

```py
tshirt_price = 9.75
shorts_price = 15.50
mug_price = 5.99
poster_price = 2.00

# Write your code below:
max_price = max(tshirt_price, shorts_price, mug_price, poster_price)
print(max_price )

min_price = min(tshirt_price, shorts_price, mug_price, poster_price)
print(min_price )

rounded_price = round(tshirt_price, 1)
print(rounded_price )
```


## Variable Access

As we expand our programs with more functions, we might start to ponder, where exactly do we have access to our variables? To examine this, let’s revisit a modified version of the first function we built out together:

```py
def trip_welcome(destination):
  print(" Looks like you're going to the " + destination + " today. ")
```

What if we wanted to access the variable destination outside of the function? Could we use it? Take a second to think about what the following program will output, then check the result below!

```py
def trip_welcome(destination):
  print(" Looks like you're going to the " + destination + " today. ")
 
print(destination)

# Output Results
NameError: name 'destination' is not defined
```

We call the part of a program where destination can be accessed its scope. The scope of destination is only inside the trip_welcome().

Take a look at another example:

```py
budget = 1000
 
# Here we are using a default value for our parameter of `destination` 
def trip_welcome(destination="California"):
    print(" Looks like you're going to " + destination)
    print(" Your budget for this trip is " + str(budget))
 
print(budget)
trip_welcome()

# Our output would be:
1000
Looks like you're going to California 
Your budget for this trip is 1000
```

Here we are able to access the budget both inside the trip_welcome function as well as our print() statement. If a variable lives outside of any function it can be accessed anywhere in the file.

We will be exploring the concept of scope more after this entire lesson but for now, let’s play around!

Note: Working with multiple functions can be a bit overwhelming at first. Don’t hesitate to use hints or even look at the solution code if you get stuck.

### Instructions

1.

Our users want to be able to save a list of their favorite places in our travel application.

We have received a rough draft for this implementation from another coder, but there are some problems with variable scope which prevent it from working properly.

Take a second to understand what the program is doing and then hit Run the code to see the error.

2.

Looking at the error, it seems like the main issue is that favorite_locations is not defined. Why would our program not be able to see our beautiful favorite_locations variable?

Aha! It must be a scope issue. Fix the scope of favorite_locations so that both our functions can access it.

```
Traceback (most recent call last):
  File "travel.py", line 11, in <module>
    show_favorite_locations()
  File "travel.py", line 8, in show_favorite_locations
    print("Your favorite locations are: " + favorite_locations)
NameError: name 'favorite_locations' is not defined
```

of how many locations we have.

```
favorite_locations = "Paris, Norway, Iceland"

def print_count_locations():
    print("There are 3 locations")
    
# This function will print the favorite locations
def show_favorite_locations():
  print("Your favorite locations are: " + favorite_locations)

print_count_locations()
show_favorite_locations()
```


## Returns

At this point, our functions have been using print() to help us visualize the output in our interpreter. Functions can also return a value to the program so that this value can be modified or used later. We use the Python keyword return to do this.

Here’s an example of a program that will return a converted currency for a given location a user may want to visit in our trip planner application.

```py
def calculate_exchange_usd(us_dollars, exchange_rate):
  return us_dollars * exchange_rate
 
new_zealand_exchange = calculate_exchange_usd(100, 1.4)
 
print("100 dollars in US currency would give you " + str(new_zealand_exchange) + " New Zealand dollars")

# This would output:
100 dollars in US currency would give you 140 New Zealand dollars
```

Saving our values returned from a function like we did with new_zealand_exchange allows us to reuse the value (in the form of a variable) throughout the rest of the program.

When there is a result from a function that is stored in a variable, it is called a returned function value.

Let’s try to return some data in the exercises!

:memo: Note: Working with multiple functions can be a bit overwhelming at first. Don’t hesitate to use hints or even look at the solution code if you get stuck.

### Instructions

1.

Our travel application is getting really popular. Some of our users have posted on social media that it would be useful if our application could help them track their budget during trips. We want to help them track their starting budget and let them know how much they have left after an expense.

We have provided some starting code to get started. Take a second to understand the code and then click Run and take a look at the output.

2.

Let’s create a new function called deduct_expense() that will take two parameters.

The first parameter will be budget and the second parameter will be expense. Our function will be taking in a budget value as well as the expense we want to subtract.

We will want our function to return the budget minus the expense our travelers are incurring.

3.

Looks like the most common expense our travelers are incurring is a t-shirt purchase.

Let’s create a variable called shirt_expense and for now, we will give it a set value of 9 (We are not accounting for currency changes at the moment). Make sure this is defined outside of the functions in your script.

4.

Now that we have an expense to subtract, create a new variable called new_budget_after_shirt and set it to be the function call of deduct_expense().

Pass our current_budget variable as the first argument and the shirt_expense variable as the second argument.

5.

Lastly, we want our users to see the remaining budget.

Call the provided print_remaining_budget() function, passing in new_budget_after_shirt as the only argument.

6.

Great Job! This is the biggest program with functions we have built so far! Take a second to review your code and click Run one last time when you are ready to move on.

```py
current_budget = 3500.75

def print_remaining_budget(budget):
  print("Your remaining budget is: $" + str(budget))

print_remaining_budget(current_budget)

# Write your code below: 
def deduct_expense(budget,expense):
  return budget - expense

shirt_expense = 9
new_budget_after_shirt = deduct_expense(current_budget, shirt_expense)

print_remaining_budget(new_budget_after_shirt )
```


## Multiple Returns

Sometimes we may want to return more than one value from a function. We can return several values by separating them with a comma. Take a look at this example of a function that allows users in our travel application to check the upcoming weeks weather (starting on Monday):

```py
weather_data = ['Sunny', 'Sunny', 'Cloudy', 'Raining', 'Snowing']
 
def threeday_weather_report(weather):
  first_day = " Tomorrow the weather will be " + weather[0]
  second_day = " The following day it will be " + weather[1]
  third_day = " Two days from now it will be " + weather[2]
  return first_day, second_day, third_day
```

This function takes in a set of data in the form of a list for the upcoming week’s weather. We can get our returned function values by assigning them both to variables when we call the function:

```py
monday, tuesday, wednesday = threeday_weather_report(weather_data)
 
print(monday)
print(tuesday)
print(wednesday)

# This will print:
Tomorrow the weather will be Sunny
The following day it will be Sunny
Two days from now it will be Cloudy
```

Let’s practice using multiple returns by returning to our previous code example.

### Instructions

1.

Our users liked the previous functionality that we added to our travel application, but recently we have had an influx of users planning trips in Italy. We want to create a small function to output the top places to visit in Italy. Another member of our team already started on the implementation of this feature but it is still missing a few key details.

Take a second to review the code and click Run when you are ready to move on. For now, there will be no output.

2.

We want to be able to return the three most popular destinations from our function top_tourist_locations_italy().

Add a line in the function top_tourist_locations_italy() that will return the values of first, second, third in that exact order.

3.

In order to use our three returned values from top_tourist_locations_italy() we need to assign them to new variables names after we call our function.

Set the return of the function top_tourist_locations_italy() to be equal to three new variables called most_popular1, most_popular2, and most_popular3 in that exact order.

4.

Use three print() statements to output the value of most_popular1, most_popular2, and most_popular3.

```py
def top_tourist_locations_italy():
  first = "Rome"
  second = "Venice"
  third = "Florence"
  #return first, second, third
  print(most_popular1)
  print(most_popular2)
  print(most_popular3)
  return most_popular1, most_popular2, most_popular3

top_tourist_locations_italy()
```

<br>

---

## Review

Excellent work! 👏 In this lesson, you’ve covered a major fundamental programming concept used in the majority of all programs to organize code into reusable blocks. To recap, we explored:

    What problems arise in our programs without functions
    What functions are and how to write them
    How whitespace plays an important role in how a program will execute our code and more importantly distinguish function code from non-function code
    How to pass input values into our functions using parameters and arguments
    The difference between built-in and user-defined functions and some common built-in functions python offers
    How we can reuse function output with the return keyword, as well as multiple returns.
    Where variables can be accessed in our programs that use functions

Let’s practice putting all these concepts together!

### Instructions

1.

Alright, this is it. We are going to use all of our knowledge of functions to build out TripPlanner V1.0.

First, like in our previous exercises, we want to make sure to welcome our users to the application.

Create a function called trip_planner_welcome() that takes one parameter called name. The function should use print() to output a message like this:

Welcome to tripplanner v1.0 `<Name Here>`

Where `<Name Here>` represents the parameter variable of name we defined.

2.

Next, we are going to generate messages for a user’s planned trip.

Create a function called destination_setup() that will have four parameters in this exact order:

    origin
    destination
    estimated_time
    mode_of_transport

Give the parameter mode_of_transport a default value of "Car". The program will error out if we run it since we have not defined a function body yet. Don’t worry we will do that in the next step.

3.

Next, we are going to write four print() statements in our function. The output on this function call should look like this:

Your trip starts off in `<origin>`  
And you are traveling to `<destination>`  
You will be traveling by `<mode_of_transport>`  
It will take approximately `<estimated_time>` hours

Each of these print() statements use a different parameter from our function destination_setup().

:memo: Note: The estimated_time parameter will come in the form of a decimal. Make sure to use str() to convert the parameter in your print statement.

4.

Lastly, we are going to define a function called estimated_time_rounded() that will allow us to calculate a rounded time value based on a decimal for our user’s trip.

An example call for this function will look like this:

estimated_time_rounded(2.43)

Where 2 represents 2 hours and .43 represents 43 minutes.

Define the function estimated_time_rounded() with a single parameter estimated_time. The function should do two things:

    Create a variable called rounded_time that is the result of calling the round() built-in function on the parameter estimated_time.
    Return rounded_time.

5.

Great job! 👏

We have successfully finished our first version of the trip builder application. Go ahead and uncomment the provided function calls and fill in the values with whatever you like.

Once have filled in the arguments, run the program to see it all in action.

```py
# Write your code below:
def trip_planner_welcome(name):
  print("Welcome to tripplanner v1.0 " + name)

def destination_setup(origin, destination, estimated_time, mode_of_transport="Car"):
  print("Your trip starts off in " + origin)
  print("And you are traveling to " + destination)
  print("You will be traveling by " + mode_of_transport)
  print("It will take approximately " + str(estimated_time) + " hours")


def estimated_time_rounded(estimated_time):
  rounded_time = round(estimated_time, 1)
  return rounded_time
```
