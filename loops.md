
What are Loops?

In our everyday lives, we tend to repeat a lot of processes without noticing.

For instance, if we want to cook a delicious recipe, we might have to prepare our ingredients by chopping them up. We chop and chop and chop until all of our ingredients are the right size. At this point, we stop chopping.

If we break down our chopping task into a series of three smaller steps, we have:

    An initialization: We’re ready to cook and have a collection of ingredients we want to chop. We will start at the first ingredient.

    A repetition: We’re chopping away. We are performing the action of chopping over and over on each of our ingredients, one ingredient at a time.

    An end condition: We see that we have run out of ingredients to chop and so we stop.

In programming, this process of using an initialization, repetitions, and an ending condition is called a loop. In a loop, we perform a process of iteration (repeating tasks).

Programming languages like Python implement two types of iteration:

    Indefinite iteration, where the number of times the loop is executed depends on how many times a condition is met.

    Definite iteration, where the number of times the loop will be executed is defined in advance (usually based on the collection size).

Typically we will find loops being used to iterate a collection of items. In the above example, we can think of our ingredients we want to chop as our collection. This is a form of definite iteration since we know how long our collection is in advance and thus know how many times we need to iterate over the collection of ingredients.

Some collections might be small — like a short string, while other collections might be massive like a range of numbers from 1 to 10,000,000! But don’t worry, loops give us the ability to masterfully handle both ends of the spectrum. This simple, but powerful, concept saves us a lot of time and makes it easier for us to work with large amounts of data.

In this lesson, we’ll learn how to use Python to implement both definite and indefinite iteration in our own programs.

Look over (and over) the provided diagram. Then, go to the next exercise to get looped in!


Why Loops?

Before we get to writing our own loops, let’s explore what programming would be like if we couldn’t use loops.

Let’s say we have a list of ingredients and we want to print every element in the list:

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

If we only use print(), our program might look like this:

print(ingredients[0])
print(ingredients[1])
print(ingredients[2])
print(ingredients[3])
print(ingredients[4])

The output would be:

milk
sugar
vanilla extract
dough
chocolate

That’s still manageable, We’re writing 5 print() statements (or copying and pasting a few times). Now imagine if we come back to this program and our list had 10, or 24601, or … 100,000,000 elements? It would take an extremely long time and by the end, we could still end up with inconsistencies and mistakes.

Don’t dwell too long on this tedious scenario — we’ll learn how loops can help us out in the next exercise. For now, let’s gain an appreciation for loops.
Instructions
1.

Using 10 print() statements, print out: "This can be so much easier with loops!".


For Loops: Introduction

Now that we can appreciate what loops do for us, let’s start with your first type of loop, a for loop, a type of definite iteration.

In a for loop, we will know in advance how many times the loop will need to iterate because we will be working on a collection with a predefined length. In our examples, we will be using Python lists as our collection of elements.

With for loops, on each iteration, we will be able to perform an action on each element of the collection.

Before we work with any collection, let’s examine the general structure of a for loop:

for <temporary variable> in <collection>:
  <action>

Let’s break down each of these components:

    A for keyword indicates the start of a for loop.
    A <temporary variable> that is used to represent the value of the element in the collection the loop is currently on.
    An in keyword separates the temporary variable from the collection used for iteration.
    A <collection> to loop over. In our examples, we will be using a list.
    An <action> to do anything on each iteration of the loop.

Let’s link these concepts back to our ingredients example. This for loop prints each ingredient in ingredients:

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]
 
for ingredient in ingredients:
  print(ingredient)

In this example:

    ingredient is the <temporary variable>.
    ingredients is our <collection>.
    print(ingredient) was the <action> performed on every iteration using the temporary variable of ingredient.

This code outputs:

milk
sugar
vanilla extract
dough
chocolate

Some things to note about for loops:

    Temporary Variables:

    A temporary variable’s name is arbitrary and does not need to be defined beforehand. Both of the following code snippets do the exact same thing as our above example:

    for i in ingredients:
      print(i)

    for item in ingredients:
     print(item)

    Programming best practices suggest we make our temporary variables as descriptive as possible. Since each iteration (step) of our loop is accessing an ingredient it makes more sense to call our temporary variable ingredient rather than i or item.

    Indentation:

    Notice that in all of these examples the print statement is indented. Everything at the same level of indentation after the for loop declaration is included in the loop body and is run on every iteration of the loop.

    for ingredient in ingredients:
      # Any code at this level of indentation 
      # will run on each iteration of the loop
      print(ingredient)

    If we ever forget to indent, we’ll get an IndentationError or unexpected behavior.

    Elegant loops:

    Python loves to help us write elegant code so it allows us to write simple for loops in one-line. In order to see the below example as one line, you may need to expand your narrative window. Here is the previous example in a single line:

    for ingredient in ingredients: print(ingredient)

    Note: One-line for loops are useful for simple programs. It is not recommended you write one-line loops for any loop that has to perform multiple complex actions on each iteration. Doing so will hurt the readability of your code and may ultimately lead to buggier code.

Let’s practice writing our own for loop!
Instructions
1.

Run the code.

We should get an IndentationError because the print(game) line is not indented.
2.

Indent (2 spaces or tab) line 6 so that we don’t get an IndentationError when you run the code.

Run the code again!
3.

Write a for loop that prints each sport in the list sport_games.

board_games = ["Settlers of Catan", "Carcassone", "Power Grid", "Agricola", "Scrabble"]

sport_games = ["football", "hockey", "baseball", "cricket"]

for game in board_games:
  print(game)

  for game in sport_games:
    print(game)



For Loops: Using Range

Often we won’t be iterating through a specific list (or any collection), but rather only want to perform a certain action multiple times.

For example, if we wanted to print out a "Learning Loops!" message six times using a for loop, we would follow this structure:

for <temporary variable> in <list of length 6>:
  print("Learning Loops!")

Notice that we need to iterate through a list with a length of six, but we don’t necessarily care what is inside of the list.

To create arbitrary collections of any length, we can pair our for loops with the trusty Python built-in function range().

An example of how the range() function works, this code generates a collection of 6 integer elements from 0 to 5:

six_steps = range(6)
 
# six_steps is now a collection with 6 elements:
# 0, 1, 2, 3, 4, 5

We can then use the range directly in our for loops as the collection to perform a six-step iteration:

for temp in range(6):
  print("Learning Loops!")

Would output:

Learning Loops!
Learning Loops!
Learning Loops!
Learning Loops!
Learning Loops!
Learning Loops!

Something to note is we are not using temp anywhere inside of the loop body. If we are curious about which loop iteration (step) we are on, we can use temp to track it. Since our range starts at 0, we will add + 1 to our temp to represent how many iterations (steps) our loop takes more accurately.

for temp in range(6):
  print("Loop is on iteration number " + str(temp + 1))

Would output:

Loop is on iteration number 1
Loop is on iteration number 2
Loop is on iteration number 3
Loop is on iteration number 4
Loop is on iteration number 5
Loop is on iteration number 6


We will need to generate a list with a length of five.

What value will we need to provide to the range() function where <length> is?

for <temporary variable> in range(<length>): 
  <action>

Let’s try out using a range in a for loop!
Instructions
1.

Use the range() function in a for loop to print() out the provided promise variable five times.
promise = "I will finish the python loops module!"
for i in range(5):
    print(promise)



While Loops: Introduction

In Python, for loops are not the only type of loops we can use. Another type of loop is called a while loop and is a form of indefinite iteration.

A while loop performs a set of instructions as long as a given condition is true.

The structure follows this pattern:

while <conditional statement>:
  <action>

Let’s examine this example, where we print the integers 0 through 3:

count = 0
while count <= 3:
  # Loop Body
  print(count)
  count += 1

Let’s break the loop down:

    count is initially defined with the value of 0. The conditional statement in the while loop is count <= 3, which is true at the initial iteration of the loop, so the loop body executes.

    Inside the loop body, count is printed and then incremented by 1.

    When the first iteration of the loop has finished, Python returns to the top of the loop and checks the conditional again. After the first iteration, count would be equal to 1 so the conditional still evaluates to True and so the loop continues.

    This continues until the count variable becomes 4. At that point, when the conditional is tested it will no longer be True and the loop will stop.

The output would be:

0
1
2
3

Note the following about while loops before we write our own:

    Indentation:

    Notice that in our example the code under the loop declaration is indented. Similar to a for loop, everything at the same level of indentation after the while loop declaration is run on every iteration of the loop while the condition is true.

    while count <= 3:
      # Loop Body
      print(count)
      count += 1
      # Any other code at this level of indentation will
      # run on each iteration

    If we ever forget to indent, we’ll get an IndentationError or unexpected behavior.

    Elegant loops:

    Similar to for loops, Python allows us to write elegant one-line while loops. Here is our previous example in a single line:

    count = 0
    while count <= 3: print(count); count += 1

    Note: Here we separate each statement with a ; to denote a separate line of code.

Let’s practice writing a while loop!
Instructions
1.

Examine the while loop from the narrative in your code editor. There are additional print() statements to help visualize the iterations.

Run the code to see what happens on each iteration of the loop. When you are finished, comment out the example to make space for the rest of the checkpoints.

To quickly comment out the code, use your cursor or mouse to highlight all the code and press command ⌘ + / on a Mac or CTRL + / on a Windows machine.
2.

Let’s write a while loop that counts down from 10 to 0(inclusive). Once our loop is finished we will commemorate our accomplishment by printing "We have liftoff!".

As we saw in the narrative, our key components will be:

    A variable to keep track of the count, and also help our loop eventually stop.

    A condition that our while loop will check on each iteration.

    Several code statements to execute on each iteration of the loop.

Let’s tackle the first component!

Create a variable named countdown and set the value to 10.
3.

Now let’s tackle the actual while loop. Define a while loop that will run while our countdown variable is greater than or equal to zero.

On each iteration:

    We should print() the value of the countdown variable.
    We should decrease the value of the countdown variable by 1

4.

Now that we have built our loop, let’s commemorate our success by printing "We have liftoff!" after the while loop.
# While Loop Walkthrough
count = 0
print("Starting While Loop")
while count <= 3:
  # Loop Body
  # Print if the condition is still true
  print("Loop Iteration - count <= 3 is still true")
  # Print the current value of count 
  print("Count is currently " + str(count))
  # Increment count
  count += 1
  print(" ----- ")
print("While Loop ended")


# Your code below: 
countdown = 10
while countdown >= 0:
  print("count:", countdown)
  countdown -= 1
print("We have liftoff!")





While Loops: Lists

A while loop isn’t only good for counting! Similar to how we saw for loops working with lists, we can use while loops to iterate through a list as well.

Let’s return to our ingredient list:

ingredients = ["milk", "sugar", "vanilla extract", "dough", "chocolate"]

We know that while loops require some form of a variable to track the condition of the loop to start and stop.

Take some time to think about what we would use to track whether we need to start/stop the loop if we want to iterate through ingredients and print every element.
Click here to find out!

We know that a list has a predetermined length. If we use the length of the list as the basis for how long our while loop needs to run, we can iterate the exact length of the list.

We can use the built-in Python len() function to accomplish this:

# Length would be equal to 5
length = len(ingredients)


We can then use this length in addition to another variable to construct the while loop:

length = len(ingredients)
index = 0
 
while index < length:
  print(ingredients[index])
  index += 1

Let’s break this down:

# Length will be 5 in this case
length = len(ingredients)

Explanation
As mentioned, we need a way to know how many times we need our loop to iterate based on the size of the collection. This comes in the form of our variable which stores the value of the length of the list.

# Index starts at zero
index = 0

Explanation

We still need an additional variable that will be used to compare against our length.

while index < length:

Explanation

In our while loop conditional, we will compare the index variable to the length of our list stored inside of the length variable.

On the first iteration, we will be comparing the equivalent of 0 < 5 which will evaluate to True, and start the execution of our loop body.

# The first iteration will print ingredients[0]
print(ingredients[index])

 
Explanation

Inside of our loop body, we can use the index variable to access our ingredients list and print the value at the current iteration.

Since our index starts at zero, our first iteration will print the value of the element at the zeroth index of our ingredients list, then the next iteration will print the value of the element at the first index, and so on.

# Increment index to access the next element in ingredients
# Each iteration gets closer to making the conditional no longer true
index += 1

Explanation
 
On each iteration of our while loop, we need to also increment the value of index to make sure our loop can stop once the index value is no longer smaller than the length value.

This increment also helps us access the next value of the ingredients list on the next iteration.

Our final output would be:

milk
sugar
vanilla extract
dough
chocolate

Let’s use a while loop to iterate through some lists!
Instructions
1.

We are going to write a while loop to iterate over the provided list python_topics.

First, we will need a variable to represent the length of the list. This will help us know how many times our while loop needs to iterate.

Create a variable length and set its value to be the length of the list of python_topics.
2.

Next, we will require a variable to compare to our length variable to make sure we are able to implement a condition that eventually allows the loop to stop.

Create a variable called index and initialize the value to be 0.
3.

Let’s now build our loop. We want our loop to iterate over the list of python_topics and on each iteration print "I am learning about <element from python_topics>". For this loop we will need the following components:

    A condition for our while loop
    A statement in the loop body to print from our condition
    A statement in the loop body to increment our index forward.

The end result should output:

I am learning about variables
I am learning about control flow
I am learning about loops
I am learning about modules
I am learning about classes


python_topics = ["variables", "control flow", "loops", "modules", "classes"]

#Your code below: 
length = len(python_topics)
index = 0
if length:
  while index < length:
    print("I am learning about", python_topics[index])
    index += 1


Infinite Loops

We’ve iterated through lists that have a discrete beginning and end. However, let’s consider this example:

my_favorite_numbers = [4, 8, 15, 16, 42]
 
for number in my_favorite_numbers:
  my_favorite_numbers.append(1)

Take some time to ponder what happens with this code.
Click to see what would happen!
  Every time we enter the loop, we add a to the end of the list that we are iterating through. As a result, we never make it to the end of the list. It keeps growing forever!

A loop that never terminates is called an infinite loop. These are very dangerous for our code because they will make our program run forever and thus consume all of your computer’s resources.

A program that hits an infinite loop often becomes completely unusable. The best course of action is to avoid writing an infinite loop.

Note: If you accidentally stumble into an infinite loop while developing on your own machine, you can end the loop by using control + c to terminate the program. If you’re writing code in our online editor, you’ll need to refresh the page to get out of an infinite loop.

Let’s fix an infinite loop to see it in action.
Instructions

Suppose we have two lists of students, students_period_A and students_period_B. We want to combine all students into students_period_B.

In your code editor, we have provided you a loop. Go ahead and uncomment line 5 and before you run the code ponder why this code would cause an infinite loop.

When you are ready, run this code. What do you notice happens? Over the run button, notice the loading circle is continuing without anything happening.

This is an infinite loop! To end this program we must refresh the page. (Note: The reason this loop is infinite is that we’re adding each student in students_period_A to students_period_A which would create a never-ending list of all the student names.) 



Loop Control: Break

Loops in Python are very versatile. Python provides a set of control statements that we can use to get even more control out of our loops.

Let’s take a look at a common scenario that we may encounter to see a use case for loop control statements.

Take the following list items_on_sale as our example:

items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]

It’s often the case that we want to search a list to check if a specific value exists. What does our loop look like if we want to search for the value of "knit dress" and print out "Found it" if it did exist?

It would look something like this:

for item in items_on_sale:
  if item == "knit dress":
    print("Found it")

This code goes through each item in items_on_sale and checks for a match. This is all fine and dandy but what’s the downside?

Once "knit_dress" is found in the list items_on_sale, we don’t need to go through the rest of the items_on_sale list. Unfortunately, our loop will keep running until we reach the end of the list.

Since it’s only 5 elements long, iterating through the entire list is not a big deal in this case but what if items_on_sale had 1000 items? What if it had 100,000 items? This would be a huge waste of time for our program!

Thankfully you can stop iteration from inside the loop by using break loop control statement.

When the program hits a break statement it immediately terminates a loop. For example:

items_on_sale = ["blue shirt", "striped socks", "knit dress", "red headband", "dinosaur onesie"]
 
print("Checking the sale list!")
 
for item in items_on_sale:
  print(item)
  if item == "knit dress":
    break
 
print("End of search!")

This would produce the output:

Checking the sale list!
blue shirt
striped socks
knit dress
End of search!

When the loop entered the if statement and saw the break it immediately ended the loop. We didn’t need to check the elements of "red headband" or "dinosaur onesie" at all.

Now let’s break some loops!
Instructions
1.

You have a list of dog breeds you can adopt, dog_breeds_available_for_adoption.

Using a for loop, iterate through the dog_breeds_available_for_adoption list and print() out each dog breed.

Use the <temporary variable> name of dog_breed in your loop decleration.
2.

Inside your for loop, after you print each dog breed, check if the current element inside dog_breed is equal to dog_breed_I_want. If so, print "They have the dog I want!"
3.

Add a break statement when your loop has found dog_breed_I_want so that the rest of the list does not need to be checked once we have found our breed.

dog_breeds_available_for_adoption = ["french_bulldog", "dalmatian", "shihtzu", "poodle", "collie"]
dog_breed_I_want = "dalmatian"

for dog_breed in dog_breeds_available_for_adoption:
  print(dog_breed)
  if dog_breed == dog_breed_I_want:
    print("They have the dog I want!")
    break



Loop Control: Continue

While the break control statement will come in handy, there are other situations where we don’t want to end the loop entirely. What if we only want to skip the current iteration of the loop?

Let’s take this list of integers as our example:

big_number_list = [1, 2, -1, 4, -5, 5, 2, -9]

What if we want to print out all of the numbers in a list, but only if they are positive integers. We can use another common loop control statement called continue.

for i in big_number_list:
  if i <= 0:
    continue
  print(i)

This would produce the output:

1
2
4
5
2

Notice a few things:

    Similar to when we were using the break control statement, our continue control statement is usually paired with some form of a conditional (if/elif/else).
    When our loop first encountered an element (-1) that met the conditions of the if statement, it checked the code inside the block and saw the continue. When the loop then encounters a continue statement it immediately skips the current iteration and moves onto the next element in the list (4).
    The output of the list only printed positive integers in the list because every time our loop entered the if statement and saw the continue statement it simply moved to the next iteration of the list and thus never reached the print statement.

Let’s continue learning about control statements with some exercises!
Instructions
1.

Your computer is the doorman at a bar in a country where the drinking age is 21.

Loop through the ages list. If an entry is less than 21, skip it and move to the next entry. Otherwise, print() the age.
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for age in ages:
  if (age <= 20):
    continue
  print(age)




Nested Loops

Loops can be nested in Python, as they can with other programming languages. We will find certain situations that require nested loops.

Suppose we are in charge of a science class, that is split into three project teams:

project_teams = [["Ava", "Samantha", "James"], ["Lucille", "Zed"], ["Edgar", "Gabriel"]]

Using a for or while loop can be useful here to get each team:

for team in project_teams:
  print(team)

Would output:

["Ava", "Samantha", "James"]
["Lucille", "Zed"]
["Edgar", "Gabriel"]

But what if we wanted to print each individual student? In this case we would actually need to nest our loops to be able loop through each sub-list. Here is what it would look like:

# Loop through each sublist
for team in project_teams:
  # Loop elements in each sublist
  for student in team:
    print(student)

This would output:

Ava
Samantha
James
Lucille
Zed
Edgar
Gabriel

Let’s practice wiriting a nested loop!
Instructions
1.

We have provided the list sales_data that shows the numbers of different flavors of ice cream sold at three different locations: Scoopcademy, Gilberts Creamery, and Manny’s Scoop Shop.

We want to sum up the total number of scoops sold. Start by defining a variable scoops_sold and set it to zero.
2.

Loop through the sales_data list using the following guidelines:

    For our temporary variable of the for loop, call it location.
    print() out each location list.

3.

Within our sales_data loop, nest a secondary loop to go through each location sublist element and add the element value to scoops_sold.

By the end, you should have the sum of every number in the sales_data nested list.
4.

Print out the value of scoops_sold outside of the nested loop.

sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]

scoops_sold = 0

for location in sales_data:
  print(location)
  for num in location:
    scoops_sold += num

print(scoops_sold)





List Comprehensions: Introduction

So far we have seen many of the ideas about using loops in our code. Python prides itself on allowing programmers to write clean and elegant code. We have already seen this with Python giving us the ability to write while and for loops in a single line.

In this exercise, we are going to examine another way we can write elegant loops in our programs using list comprehensions.

To start, let’s say we had a list of integers and wanted to create a list where each element is doubled. We could accomplish this using a for loop and a new list called doubled:

numbers = [2, -1, 79, 33, -45]
doubled = []
 
for number in numbers:
  doubled.append(number * 2)
 
print(doubled)

Would output:

[4, -2, 158, 66, -90]

Let’s see how we can use the power of list comprehensions to solve these types of problems in one line. Here is our same problem but now written as a list comprehension:

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 for num in numbers]
print(doubled)

Let’s break down our example in a more general way:

new_list = [<expression> for <element> in <collection>]

In our doubled example, our list comprehension:

    Takes an element in the list numbers
    Assigns that element to a variable called num (our <element>)
    Applies the <expression> on the element stored in num and adds the result to a new list called doubled
    Repeats steps 1-3 for every other element in the numbers list (our <collection>)

Our result would be the same:

[4, -2, 158, 66, -90]

Instructions
1.

We have been provided a list of grades in a physics class. Using a list comprehension, create a new list called scaled_grades that scales the class grades based on the highest score.

Since the highest score was a 90 we simply want to add 10 points to all the grades in the list.
2.

Print scaled_grades.

grades = [90, 88, 62, 76, 74, 89, 48, 57]
scaled_grades = [scope + 10 for scope in grades]
print(scaled_grades)



List Comprehensions: Conditionals

List Comprehensions are very flexible. We even can expand our examples to incorporate conditional logic.

Suppose we wanted to double only our negative numbers from our previous numbers list.

We will start by using a for loop and a list only_negative_doubled:

numbers = [2, -1, 79, 33, -45]
only_negative_doubled = []
 
for num in numbers:
  if num < 0: 
    only_negative_doubled.append(num * 2)
 
print(only_negative_doubled) 

Would output:

[-2, -90]

Now, here is what our code would look like using a list comprehension:

numbers = [2, -1, 79, 33, -45]
negative_doubled = [num * 2 for num in numbers if num < 0]
print(negative_doubled)

Would output the same result:

[-2, -90]

In our negative_doubled example, our list comprehension:

    Takes an element in the list numbers.
    Assigns that element to a variable called num.
    Checks if the condition num < 0 is met by the element stored in num. If so, it goes to step 4, otherwise it skips it and goes to the next element in the list.
    Applies the expression num * 2 on the element stored in num and adds the result to a new list called negative_doubled
    Repeats steps 1-3 (and sometimes 4) for every other element in the numbers list.

We can also use If-Else conditions directly in our comprehensions. For example, let’s say we wanted to double every negative number but triple all positive numbers. Here is what our code might look like:

numbers = [2, -1, 79, 33, -45]
doubled = [num * 2 if num < 0 else num * 3 for num in numbers ]
print(doubled)

Would output:

[6, -2, 237, 99, -90]

This is a bit different than our previous comprehension since the conditional if num < 0 else num * 3 comes after the expression num * 2 but before our for keyword.

Let’s write our own list comprehensions with conditionals!
Instructions
1.

We have defined a list heights of visitors to a theme park. In order to ride the Topsy Turvy Tumbletron roller coaster, you need to be above 161 centimeters.

Using a list comprehension, create a new list called can_ride_coaster that has every element from heights that is greater than 161.
2.

Print can_ride_coaster.
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]

can_ride_coaster = [num for num in heights if num > 161]

print(can_ride_coaster)




Review

Good job! In this lesson, you learned

    How to write a for loop.
    How to use range in a loop.
    How to write a while loop.
    What infinite loops are and how to avoid them.
    How to control loops using break and continue.
    How to write elegant loops as list comprehensions.

Let’s get some more practice with these concepts!
Instructions
1.

Create a list called single_digits that consists of the numbers 0-9 (inclusive).
2.

Create a for loop that goes through single_digits and prints out each one.
3.

Before the loop, create a list called squares. Assign it to be an empty list to begin with.
4.

Inside the loop that iterates through single_digits, append the squared value of each element of single_digits to the list squares. You can do this before or after printing the element.
5.

After the for loop, print out squares.
6.
Create the list cubes using a list comprehension on the single_digits list. Each element of cubes should be an element of single_digits taken to the third power.
7.
Print cubes.

Good job!
# Your code below:
single_digits = [0,1,2,3,4,5,6,7,8,9]
squares = []
for digit in single_digits:
  print(digit)
  squares.append(digit * digit)

print(squares)

cubes = [num ** 3 for num in single_digits]
print(cubes)


Good job!




Carly's Clippers

You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. Your job is to go through the lists of data that have been collected in the past couple of weeks. You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

You have been provided with three lists:

    hairstyles: the names of the cuts offered at Carly’s Clippers.
    prices: the price of each hairstyle in the hairstyles list.
    last_week: the number of purchases for each hairstyle type in the last week.

Each index in hairstyles corresponds to an associated index in prices and last_week.

For example, The hairstyle "bouffant" has an associated price of 30 from the prices list, and was purchased 2 times in the last week as shown in the last_week list. Each of these elements are in the first index of their respective lists.

Let’s get started!

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.
Syntax you can use for your list comprehension might look like:
new_list = [old_list[i] for i in range(len(old_list)) if different_list[i] < 0]
This makes a new list of every entry in old_list for which the index i satisfies the condition different_list[i] < 0.

Prices and Cuts:
1.
Carly wants to be able to market her low prices. We want to find out what the average price of a cut is.

First, let’s sum up all the prices of haircuts. Create a variable total_price, and set it to 0.
2.
Loop through the prices list and add each price to the variable total_price.
3.
After your loop, create a variable called average_price that is the total_price divided by the number of prices.

You can get the number of prices by using the len() function.
4.
Print the value of average_price so the output looks like:

Average Haircut Price: <average_price>

5.
That average price is more expensive than Carly thought it would be! She wants to cut all prices by 5 dollars.

Use a list comprehension to make a list called new_prices, which has each element in prices minus 5.
6.
Print new_prices.
Revenue:
7.
Carly really wants to make sure that Carly’s Clippers is a profitable endeavor. She first wants to know how much revenue was brought in last week.

Create a variable called total_revenue and set it to 0.
8.
Use a for loop to create a variable i that goes from 0 to len(hairstyles)

Hint: You can use range() to do this!
9.
Add the product of prices[i] (the price of the haircut at position i) and last_week[i] (the number of people who got the haircut at position i) to total_revenue at each step.
10.
After your loop, print the value of total_revenue, so the output looks like:
Total Revenue: <total_revenue>

11.
Find the average daily revenue by dividing total_revenue by 7. Call this number average_daily_revenue and print it out.
12.
Carly thinks she can bring in more customers by advertising all of the haircuts she has that are under 30 dollars.

Use a list comprehension to create a list called cuts_under_30 that has the entry hairstyles[i] for each i for which new_prices[i] is less than 30.

You can use range() in your list comprehension to make i go from 0 to len(new_prices) - 1.
13.
Print cuts_under_30.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
num_prices = len(prices)

for price in prices:
  total_price += price
  average_price = total_price / num_prices
  print("Average Haircut Price:", average_price)

new_prices = [price - 5 for price in prices]
print(new_prices)

total_revenue = 0

for i in range(len(hairstyles)):
  total_revenue += prices[i] * last_week[i]

print("Total Revenue:", total_revenue)

average_daily_revenue = total_revenue / 7
print(average_daily_revenue)

cuts_under_30 = [hairstyles[i] for i in range(len(new_prices) - 1) if new_prices[i] < 30 ]

print(cuts_under_30)





