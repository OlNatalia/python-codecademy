# Python Start

https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-hello-world/cheatsheet

https://github.com/Codecademy/learn-python/blob/main/1-hello-world/block-letters/initials.py

https://github.com/Codecademy/learn-python/blob/main/1-hello-world/block-letters/snowman.py

https://github.com/Codecademy/learn-python/blob/main/2-control-flow/magic-8-ball/magic8.py


my notes from my 5 hours i spent learing python 3 on codecademy, super dope language and really fun :)
notes

coding notes from learning python on CA:

    comments

    start a line with # and anything after that the computer ignores
    these are called comments, give context or instructions
    documentation is important in programming

    print

    self explainitory, prints what you tell it
    print("ur message")
    dont forget quotation marks ""

    strings

    strings are text within the code
    can use ' or ", doesnt matter just be consistant

    variables

    bank (if you will) that can store a value
    e.g. message_string = "sup homie"

prints "sup homie"

print(message_string)
refers to the value which is storing the value (string)

    cannot include spaces, symbols, special letters BUT can include numbers but only after the first letter. for example: this_is_ok_69 = "LOL"
    if the context of the program changes, insteading of changing all the strings you just need to change the variable which is holding the value (string) since all your prints are refering to the variable
    Q&A:

We've defined the variable "meal" here to the name of the food we ate for breakfast!

meal = "An english muffin"
Printing out breakfast

print("Breakfast:") print(meal)
Now update meal to be lunch!

meal = "Sandwich"
Printing out lunch

print("Lunch:") print(meal)
Now update "meal" to be dinner

meal = "Chicken"
Printing out dinner

print("Dinner:") print(meal)

    errors

    programs will attempt to indentify, understand and explain mistakes in their code/program
    python 3 refers to these mistakes as "errors"
    they will point out where this mistake was made with a "^" symbol
    there might be unexpected errors withtin your code that was not picked up and they are called "bugs"
    the process of updating the program to get rid of the bugs is called "debugging"
    two common errors that occur when writing python 3 are "NameError" and "SyntaxError"
    a NameError happens when python sees a word that isnt intimate with the program. a bit of code that looks like a variable but was never defined. you probably misspelt the word or something
    a SyntaxError means that there is something wrong with your program due to the way it was written. much like a calculator SyntaxError its probably because you have punctuation that does not belong, missing parenthesis (this thing thats hugging this text <3) or a command where it is not expected or a missing parenthesis can all cause a SyntaxError
    Q&A:

print('This message has mismatched quote marks!") print(Abracadabra) ***************************************************************************- you may ask: "whats wrong with this homie?". well, the first line is a SyntaxError because it opens and closes with different quotation marks. BE CONSISTANT HOMIE. the second line is a NameError because it doesnt even have quotation marks man.

    FIXED

print("This message has mismatched quote marks!") print("Abracadabra")

    numbers

    computers can understand more than string of text
    there are multiple ways of storing numbers, it all depends of the purpose for the number you're storing
    these consist of intergets (int) and floating-point number (float)
    an interger or int is a whole number, NO DECIMAL POINTZ.
    contains all count numbers: 1,2,3... as well as their negative halfs (negatives) and the number 0
    if u were finna count the number of books on a shelf, number of kids in a class or number of songs in my fire af playlist you would most likely use an int (interger)
    a floating-point number (LLOOOOOL THAT NAME) or a float is a decimal number
    can be used to represent fraction tingz and exact measurements
    if u were measuing the length of your room door or how tall post malone is then you would use a float (floating-point number)
    can be used in programs migos: STRAIGHT UP! or can be assigned to variables
    REFRENCE:

```py
an_int = 2 a_float = 2.1

print(an_int + 3)
prints 5
```

An integer, or int, is a whole number. It has no decimal point and contains all counting numbers (1, 2, 3, …) as well as their negative counterparts and the number 0. If you were counting the number of people in a room, the number of jellybeans in a jar, or the number of keys on a keyboard you would likely use an integer.

A floating-point number, or a float, is a decimal number. It can be used to represent fractional quantities as well as precise measurements. If you were measuring the length of your bedroom wall, calculating the average test score of a seventh-grade class, or storing a baseball player’s batting average for the 1998 season you would likely use a float.

Numbers can be assigned to variables or used literally in a program:

```py
an_int = 2
a_float = 2.1
 
print(an_int + 3)
# Output: 5
```

Above we defined an integer and a float as the variables an_int and a_float. We printed out the sum of the variable an_int with the number 3. We call the number 3 here a literal, meaning it’s actually the number 3 and not a variable with the number 3 assigned to it.

Floating-point numbers can behave in some unexpected ways due to how computers store them. For more information on floating-point numbers and Python, review 

---

## Calculations

Computers absolutely excel at performing calculations. The “compute” in their name comes from their historical association with providing answers to mathematical questions. Python performs addition, subtraction, multiplication, and division with +, -, *, and /.

```py
# Prints "500"
print(573 - 74 + 1)
 
# Prints "50"
print(25 * 2)
 
# Prints "2.0"
print(10 / 5)
```

Notice that when we perform division, the result has a decimal place. This is because Python converts all ints to floats before performing division. In older versions of Python (2.7 and earlier) this conversion did not happen, and integer division would always round down to the nearest integer.

Division can throw its own special error: ZeroDivisionError. Python will raise this error when attempting to divide by 0.

Mathematical operations in Python follow the standard mathematical order of operations.

Instructions

1.

Print out the result of this equation: 25 * 68 + 13 / 28

---

## Changing Numbers

Variables that are assigned numeric values can be treated the same as the numbers themselves. Two variables can be added together, divided by 2, and multiplied by a third variable without Python distinguishing between the variables and literals (like the number 2 in this example). Performing arithmetic on variables does not change the variable — you can only update a variable using the = sign.

```py
coffee_price = 1.50
number_of_coffees = 4
 
# Prints "6.0"
print(coffee_price * number_of_coffees)
# Prints "1.5"
print(coffee_price)
# Prints "4"
print(number_of_coffees)
 
# Updating the price 
coffee_price = 2.00
 
# Prints "8.0"
print(coffee_price * number_of_coffees)
# Prints "2.0"
print(coffee_price)
# Prints "4"
print(number_of_coffees)
```

We create two variables and assign numeric values to them. Then we perform a calculation on them. This doesn’t update the variables! When we update the coffee_price variable and perform the calculations again, they use the updated values for the variable!

Instructions

1.

You’ve decided to get into quilting! To calculate the number of squares you’ll need for your first quilt let’s create two variables: quilt_width and quilt_length. Let’s make this first quilt 8 squares wide and 12 squares long.
quilt_width = 8
quilt_length = 12
number_of_squares = quilt_width * quilt_length
print(number_of_squares)
quilt_length = 8
print(number_of_squares)


---

## Exponents

Python can also perform exponentiation. In written math, you might see an exponent as a superscript number, but typing superscript numbers isn’t always easy on modern keyboards. Since this operation is so related to multiplication, we use the notation **.

```py
# 2 to the 10th power, or 1024
print(2 ** 10)
 
# 8 squared, or 64
print(8 ** 2)
 
# 9 * 9 * 9, 9 cubed, or 729
print(9 ** 3)
 
# We can even perform fractional exponents
# 4 to the half power, or 2
print(4 ** 0.5)
```

Here, we compute some simple exponents. We calculate 2 to the 10th power, 8 to the 2nd power, 9 to the 3rd power, and 4 to the 0.5th power.

Instructions

1.

You really like how the square quilts from last exercise came out, and decide that all quilts that you make will be square from now on.

Using the exponent operator, print out how many squares you’ll need for a 6x6 quilt, a 7x7 quilt, and an 8x8 quilt.

2.

Your 6x6 quilts have taken off so well, 6 people have each requested 6 quilts. Print out how many tiles you would need to make 6 quilts apiece for 6 people.

```py
# Calculation of squares for:
# 6x6 quilt
print(6 ** 2)
# 7x7 quilt
print(7 ** 2)
# 8x8 quilt
print(8 ** 2)
# How many squares for 6 people to have 6 quilts each that are 6x6?
print(6 ** 4)
```

---

## Modulo

Python offers a companion to the division operator called the modulo operator. The modulo operator is indicated by % and gives the remainder of a division calculation. If the number is divisible, then the result of the modulo operator will be 0.

```py
# Prints 4 because 29 / 5 is 5 with a remainder of 4
print(29 % 5)
 
# Prints 2 because 32 / 3 is 10 with a remainder of 2
print(32 % 3)
 
# Modulo by 2 returns 0 for even numbers and 1 for odd numbers
# Prints 0
print(44 % 2)
```

Here, we use the modulo operator to find the remainder of division operations. We see that 29 % 5 equals 4, 32 % 3 equals 2, and 44 % 2 equals 0.

The modulo operator is useful in programming when we want to perform an action every nth-time the code is run. Can the result of a modulo operation be larger than the divisor? Why or why not?

Instructions

1.

You’re trying to divide a group into four teams. All of you count off, and you get number 27.

Find out your team by computing 27 modulo 4. Save the value to my_team.

2.

Print out my_team. What number team are you on?

3.

Food for thought: what number team are the two people next to you (26 and 28) on? What are the numbers for all 4 teams? (Optional Challenge Question)

```py
my_team = 27 % 4
print(my_team)
print(26 % 4)
print(28 % 4)

# output: 3
2
0
```

---

## Concatenation

The + operator doesn’t just add two numbers, it can also “add” two strings! The process of combining two strings is called string concatenation. Performing string concatenation creates a brand new string comprised of the first string’s contents followed by the second string’s contents (without any added space in-between).

```py
greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text
 
# Prints "Hey there!How are you doing?"
print(full_text)
```

In this sample of code, we create two variables that hold strings and then concatenate them. But we notice that the result was missing a space between the two, let’s add the space in-between using the same concatenation operator!

```py
full_text = greeting_text + " " + question_text
 
# Prints "Hey there! How are you doing?"
print(full_text)
```

Now the code prints the message we expected.

If you want to concatenate a string with a number you will need to make the number a string first, using the str() function. If you’re trying to print() a numeric variable you can use commas to pass it as a different argument rather than converting it to a string.

```py
birthday_string = "I am "
age = 10
birthday_string_2 = " years old today!"
 
# Concatenating an integer with strings is possible if we turn the integer into a string first
full_birthday_string = birthday_string + str(age) + birthday_string_2
 
# Prints "I am 10 years old today!"
print(full_birthday_string)
 
# If we just want to print an integer 
# we can pass a variable as an argument to 
# print() regardless of whether 
# it is a string.
 
# This also prints "I am 10 years old today!"
print(birthday_string, age, birthday_string_2)
```

Using str() we can convert variables that are not strings to strings and then concatenate them. But we don’t need to convert a number to a string for it to be an argument to a print statement.

Instructions

1.

Concatenate the strings and save the message they form in the variable message.

Now uncomment the print statement and run your code to see the result in the terminal!

```py
message = string1 + string2 + string3 + string4 + string5 + string6

print(message)
```

---

## Plus Equals

Python offers a shorthand for updating variables. When you have a number saved in a variable and want to add to the current value of the variable, you can use the += (plus-equals) operator.

```py
# First we have a variable with a number saved
number_of_miles_hiked = 12
 
# Then we need to update that variable
# Let's say we hike another two miles today
number_of_miles_hiked += 2
 
# The new value is the old value
# Plus the number after the plus-equals
print(number_of_miles_hiked)
# Prints 14
```

Above, we keep a running count of the number of miles a person has gone hiking over time. Instead of recalculating from the start, we keep a grand total and update it when we’ve gone hiking further.

The plus-equals operator also can be used for string concatenation, like so:

```py
hike_caption = "What an amazing time to walk through nature!"
 
# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"
```

We create the social media caption for the photograph of nature we took on our hike, but then update the caption to include important social media tags we almost forgot.

Instructions

1.

We’re doing a little bit of online shopping and find a pair of new sneakers. Right before we check out, we spot a nice sweater and some fun books we also want to purchase!

Use the += operator to update the total_price to include the prices of nice_sweater and fun_books.

The prices (also included in the workspace) are:

    new_sneakers = 50.00
    nice_sweater = 39.00
    fun_books = 20.00

```py
# Update total_price here:
total_price = new_sneakers + nice_sweater + fun_books
print("The total price is", total_price)
```

---

## Multi-line Strings

Python strings are very flexible, but if we try to create a string that occupies multiple lines we find ourselves face-to-face with a SyntaxError. Python offers a solution: multi-line strings. By using three quote-marks (""" or ''') instead of one, we tell the program that the string doesn’t end until the next triple-quote. This method is useful if the string being defined contains a lot of quotation marks and we want to be sure we don’t close it prematurely.

```py
leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""
```

In the above example, we assign a famous poet’s words to a variable. Even though the quote contains multiple linebreaks, the code works!

If a multi-line string isn’t assigned a variable or used in an expression it is treated as a comment.

Instructions

1.

Assign the string

Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?

to the variable to_you.

```py
to_you = """
Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?
"""

print(to_you)
```

---

## Review - Hello World

In this lesson, we accomplished a lot of things! We instructed our computers to print messages, we stored these messages as variables, and we learned to update those messages depending on the part of the program we were in. We performed mathematical calculations and explored some of the mathematical expressions that Python offers us. We learned about errors and other valuable skills that will continue to serve us as we develop our programming skills.

Instructions

1.

Create variables:

    my_age
    half_my_age
    greeting
    name
    greeting_with_name

Assign values to each using your knowledge of division and concatenation!

```py
my_age = 25
half_my_age = my_age / 2
greeting = "Hello"
name = "Alex"
greeting_with_name = greeting + " " + name
```

---

## Block Letters

**ASCII** art is a graphic design technique that uses computers for presentation and consists of pictures pieced together from individual characters.

Write a Python program called initials.py that displays the initials of your name in block letters as shown and dip your toes into ASCII art.

What we are building in this project:

1.

Take a look at the complete alphabet and find your initials. Notice how each block letter is 7x5 and formed by the letter itself.

My initials are S and L, so my initials.py program should output:

    SSS   L
    S   S  L
    S      L
    SSS   L
        S  L
    S   S  L
    SSS   LLLLL

Once you are ready, mark this task complete by checking off the box.

Setting up:

2.

First, write two comments with:

    Your first and last name.
    A fun fact about yourself.

3.

Output your first initial as a block letter. There are a few ways to do this!

Press Save to run your program.

4.

Output your second initial as a block letter by adding to the print() statements.

Press Save to run your program.

5.

Don’t forget to check off all the tasks before moving on.

Sample solutions:

    initials.py
    snowman.py

P.S. If you make something cool, share it with us!

# Sonny Li
# Fun Fact: I played guitar in a band called Attica.

print("  SSS   L     ")
print(" S   S  L     ")
print(" S      L     ")
print("  SSS   L     ")
print("     S  L     ")
print(" S   S  L     ")
print("  SSS   LLLLL ")


---

### Receipts for Lovely Loveseats

We’ve decided to pursue the dream of small-business ownership and open up a furniture store called Lovely Loveseats for Neat Suites on Fleet Street. With our newfound knowledge of Python programming, we’re going to build a system to help speed up the process of creating receipts for your customers.

In this project, we will be storing the names and prices of a furniture store’s catalog in variables. You will then process the total price and item list of customers, printing them to the output terminal.

Please note: Projects do not run tests against your code. This experience is more open to your interpretation and gives you the freedom to explore. Remember that all variables must be declared before they are referenced in your code.

If you get stuck during this project or would like to see an experienced developer work through it, click “Get Help“ to see a project walkthrough video.


Adding In The Catalog

1.

Let’s add in our first item, the Lovely Loveseat that is the store’s namesake. Create a variable called lovely_loveseat_description and assign to it the following string:

Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.

2.

Great, now let’s create a price for the loveseat. Create a variable lovely_loveseat_price and set it equal to 254.00.

3.

Let’s extend our inventory with another characteristic piece of furniture! Create a variable called stylish_settee_description and assign to it the following string:

Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.

4.

Now let’s set the price for our Stylish Settee. Create a variable stylish_settee_price and assign it the value of 180.50.
5.

Fantastic, we just need one more item before we’re ready for business. Create a new variable called luxurious_lamp_description and assign it the following:

Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.

6.

Let’s set the price for this item. Create a variable called luxurious_lamp_price and set it equal to 52.15.

7.

In order to be a business, we should also be calculating sales tax. Let’s store that in a variable as well.

Define the variable sales_tax and set it equal to .088. That’s 8.8%.
Our First Customer

8.

Our first customer is making their purchase! Let’s keep a running tally of their expenses by defining a variable called customer_one_total. Since they haven’t purchased anything yet, let’s set that variable equal to 0 for now.

9.

We should also keep a list of the descriptions of things they’re purchasing. Create a variable called customer_one_itemization and set that equal to the empty string "". We’ll tack on the descriptions to this as they make their purchases.

10.

Our customer has decided they are going to purchase our Lovely Loveseat! Add the price to customer_one_total.

11.

Let’s start keeping track of the items our customer purchased. Add the description of the Lovely Loveseat to customer_one_itemization.

12.

Our customer has also decided to purchase the Luxurious Lamp! Let’s add the price to the customer’s total.

13.

Let’s keep the itemization up-to-date and add the description of the Luxurious Lamp to our itemization.

14.

They’re ready to check out! Let’s begin by calculating sales tax. Create a variable called customer_one_tax and set it equal to customer_one_total times sales_tax.
15.

Add the sales tax to the customer’s total cost.
16.

Let’s start printing up their receipt! Begin by printing out the heading for their itemization. Print the phrase "Customer One Items:".
17.

Print customer_one_itemization.
18.

Now add a heading for their total cost: Print out "Customer One Total:"
19.

Now print out their total! Our first customer now has a receipt for the things they purchased.
20.

Congratulations! We created our catalog and served our first customer. We used our knowledge of strings and numbers to create and update variables. We were able to print out an itemized list and a total cost for our customer. Lovely!


lovely_loveseat_description = """
Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.
"""

lovely_loveseat_price = 254.00

stylish_settee_description = """
Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.
"""

stylish_settee_price = 180.50

luxurious_lamp_description = """
Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.
"""
luxurious_lamp_price = 52.15

sales_tax = 0.88

customer_one_total = 0
customer_one_itemization = ""

customer_one_total += lovely_loveseat_price
customer_one_itemization += lovely_loveseat_description

customer_one_total += luxurious_lamp_price
customer_one_itemization += luxurious_lamp_description

customer_one_tax = customer_one_total * sales_tax
print(customer_one_tax)

print("Customer One Items:", customer_one_total)
print(customer_one_itemization)



User Input

How to assign variables with user input.

So far, we’ve covered how to assign variables values directly in a Python file. However, we often want a user of a program to enter new information into the program.

How can we do this? As it turns out, another way to assign a value to a variable is through user input.

While we output a variable’s value using print(), we assign information to a variable using input(). The input() function requires a prompt message, which it will print out for the user before they enter the new information. For example:

likes_snakes = input("Do you like snakes? ")

In the example above, the following would occur:

    The program would print "Do you like snakes? " for the user.
    The user would enter an answer (e.g., "Yes! I have seven pythons as pets!") and press enter.
    The variable likes_snakes would be assigned a value of the user’s answer.

Try constructing a statement to collect user input on your own!

Fill in the blanks in the code to complete a statement that asks a user “What is your favorite flightless bird?” and then stores their answer in the variable favorite_flightless_bird.

 = ()

Click or drag and drop to fill in the blank




Introduction to Control Flow

Imagine waking up in the morning.

You wake up and think, “Ugh. Is it a weekday?”

If so, you have to get up and get dressed and get ready for work or school. If not, you can sleep in a bit longer and catch a couple extra Z’s. But alas, it is a weekday, so you are up and dressed and you go to look outside, “What’s the weather like? Do I need an umbrella?”

These questions and decisions control the flow of your morning, each step and result is a product of the conditions of the day and your surroundings. Your computer, just like you, goes through a similar flow every time it executes code. A program will run (wake up) and start moving through its checklists, is this condition met, is that condition met, okay let’s execute this code and return that value.

This is the control flow of your program. In Python, your script will execute from the top down, until there is nothing left to run. It is your job to include gateways, known as conditional statements, to tell the computer when it should execute certain blocks of code. If these conditions are met, then run this function.

Over the course of this lesson, you will learn how to build conditional statements using boolean expressions, and manage the control flow in your code.


Control Flow
Boolean Expressions

In order to build control flow into our program, we want to be able to check if something is true or not. A boolean expression is a statement that can either be True or False.

Let’s go back to the ‘waking up’ example. The first question, “Is today a weekday?” can be written as a boolean expression:

Today is a weekday.

This expression can be True if today is Tuesday, or it can be False if today is Saturday. There are no other options.

Consider the phrase:

Friday is the best day of the week.

Is this a boolean expression?

No, this statement is an opinion and is not objectively True or False. Someone else might say that “Wednesday is the best weekday,” and their statement would be no less True or False than the one above.

How about the phrase:

Sunday starts with the letter 'C'.

Is this a boolean expression?

Yes! This expression can only be True or False, which makes it a boolean expression. Even though the statement itself is false (Sunday starts with the letter ‘C’), it is still a boolean expression.
Instructions
1.

Determine if the following statements are boolean expressions or not. If they are, set the matching variable to the right to "Yes" and if not set the variable to "No". Here’s an example of what to do:

Example statement:

My dog is the cutest dog in the world.

This is an opinion and not a boolean expression, so you would set example_statement to "No" in the editor to the right. Okay, now it’s your turn:

Statement one:

Dogs are mammals.

Statement two:

My dog is named Pavel.

Statement three:

Dogs make the best pets.

Statement four:

Cats are female dogs.


example_statement = "No"

statement_one = "Yes"

statement_two = "Yes"

statement_three = "No"

statement_four = "Yes"






Control Flow
Relational Operators: Equals and Not Equals

Now that we understand what boolean expressions are, let’s learn to create them in Python. We can create a boolean expression by using relational operators.

Relational operators compare two items and return either True or False. For this reason, you will sometimes hear them called comparators.

The two relational operators we’ll cover first are:

    Equals: ==
    Not equals: !=

These operators compare two items and return True or False if they are equal or not.

We can create boolean expressions by comparing two values using these operators:

1 == 1     # True
 
2 != 4     # True
 
3 == 5     # False
 
'7' == 7   # False

Each of these is an example of a boolean expression.

Why is the last statement false? The '' marks in '7' make it a string, which is different from the integer value 7, so they are not equal. When using relational operators it is important to always be mindful of type.
Instructions
1.

Determine if the following boolean expressions are True or False. Input your answer as True or False in the appropriate variable to the right.

Statement one:

(5 * 2) - 1 == 8 + 1

Statement two:

13 - 6 != (3 * 2) + 1

Statement three:

3 * (2 - 1) == 4 - 1


statement_one = True

statement_two = False

statement_three = True





Control Flow
Boolean Variables

Before we go any further, let’s talk a little bit about True and False. You may notice that when you type them in the code editor (with uppercase T and F), they appear in a different color than variables or strings. This is because True and False are their own special type: bool.

True and False are the only bool types, and any variable that is assigned one of these values is called a boolean variable.

Boolean variables can be created in several ways. The easiest way is to simply assign True or False to a variable:

set_to_true = True
set_to_false = False

You can also set a variable equal to a boolean expression.

bool_one = 5 != 7 
bool_two = 1 + 1 != 2
bool_three = 3 * 3 == 9

These variables now contain boolean values, so when you reference them they will only return the True or False values of the expression they were assigned.

print(bool_one)    # True
 
print(bool_two)    # False
 
print(bool_three)  # True

Instructions
1.

Create a variable named my_baby_bool and set it equal to "true".
2.

Check the type of my_baby_bool using type(my_baby_bool).

You’ll have to print it to get the results to display in the terminal.

It’s not a boolean variable! Boolean values True and False always need to be capitalized and do not have quotation marks.

Create a variable named my_baby_bool_two and set it equal to True.
4.

Check the type of my_baby_bool_two and make sure you successfully created a boolean variable.

You’ll have to print it to get the results to display in the terminal.

my_baby_bool = "true"
print(type(my_baby_bool))
my_baby_bool_two = True
print(type(my_baby_bool_two))





Control Flow
If Statement

“Okay okay okay, boolean variables, boolean expressions, blah blah blah, I thought I was learning how to build control flow into my code!”

You are, I promise you!

Understanding boolean variables and expressions is essential because they are the building blocks of conditional statements.

Recall the waking-up example from the beginning of this lesson. The decision-making process of “Is it raining? If so, bring an umbrella” is a conditional statement.

Here it is phrased in a different way:

If it is raining, then bring an umbrella.

Can you pick out the boolean expression here?

Right, "it is raining" is the boolean expression, and this conditional statement is checking to see if it is True.

If "it is raining" == True then the rest of the conditional statement will be executed and you will bring an umbrella.

This is the form of a conditional statement:

If [it is raining], then [bring an umbrella]

In Python, it looks very similar:

if is_raining:
  print("bring an umbrella")

You’ll notice that instead of “then” we have a colon, :. That tells the computer that what’s coming next is what should be executed if the condition is met.

Let’s take a look at another conditional statement:

if 2 == 4 - 2: 
  print("apple")

Will this code print apple to the terminal?

Yes, because the condition of the if statement, 2 == 4 - 2 is True.

Let’s work through a couple more together.
Instructions
1.

In script.py, there is an if statement. I wrote this because my coworker Dave kept using my computer without permission and he is a real doofus. If the user_name is Dave, it tells him to stay off my computer.

Enter a user name in the field for user_name and try running the program.
2.

Oh no! We got a SyntaxError! This happens when we make a small error in the syntax of the conditional statement.

Read through the error message carefully and see if you can find the error. Then, fix it, and run the code again.
3.

Ugh! Dave got around my security and has been logging onto my computer using our coworker Angela’s user name, angela_catlady_87.

Set your user_name to be angela_catlady_87.

Update the program with a second if statement so it checks for Angela’s user name as well and prints

"I know it is you, Dave! Go away!"

in response. That’ll teach him!


user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")




Control Flow
Relational Operators II

Now that we’ve added conditional statements to our toolkit for building control flow, let’s explore more ways to create boolean expressions. So far we know two relational operators, equals and not equals, but there are a ton (well, four) more:

    > greater than
    >= greater than or equal to
    < less than
    <= less than or equal to

Let’s say we’re running a movie streaming platform and we want to write a program that checks if our users are over 13 when showing them a PG-13 movie. We could write something like:

if age <= 13:
  print("Sorry, parental control required")

This function will take the user’s age and compare it to the number 13. If age is less than or equal to 13, it will print out a message.

Let’s try some more!
Instructions
1.

Create an if statement that checks if x and y are equal, print the string below if so:

"These numbers are the same"

2.

The nearby college, Calvin Coolidge’s Cool College (or 4C, as the locals call it) requires students to earn 120 credits to graduate.

Write an if statement that checks if the student has enough credits to graduate. If they do, return the string:

"You have enough credits to graduate!"

Can a student with 120 credits graduate from Calvin Coolidge’s Cool College?

x = 20
y = 20

# Write the first if statement here:
if x == y:
  print("These numbers are the same")


credits = 120

# Write the second if statement here:
if credits >= 120:
  print("You have enough credits to graduate!")





Control Flow
Boolean Operators: and

Often, the conditions you want to check in your conditional statement will require more than one boolean expression to cover. In these cases, you can build larger boolean expressions using boolean operators. These operators (also known as logical operators) combine smaller boolean expressions into larger boolean expressions.

There are three boolean operators that we will cover:

    and
    or
    not

Let’s start with and.

and combines two boolean expressions and evaluates as True if both its components are True, but False otherwise.

Consider the example:

Oranges are a fruit and carrots are a vegetable.

This boolean expression is comprised of two smaller expressions, oranges are a fruit and carrots are a vegetable, both of which are True and connected by the boolean operator and, so the entire expression is True.

Let’s look at an example of some AND statements in Python:

(1 + 1 == 2) and (2 + 2 == 4)   # True
 
(1 > 9) and (5 != 6)            # False
 
(1 + 1 == 2) and (2 < 1)        # False
 
(0 == 10) and (1 + 1 == 1)      # False

Notice that in the second and third examples, even though part of the expression is True, the entire expression as a whole is False because the other statement is False. The fourth statement is also False because both components are False.
Instructions
1.

Set the variables statement_one and statement_two equal to the results of the following boolean expressions:

Statement one:

(2 + 2 + 2 >= 6) and (-1 * -1 < 0)

Statement two:

(4 * 2 <= 8) and (7 - 1 == 6)

2.

Let’s return to Calvin Coolidge’s Cool College. 120 credits aren’t the only graduation requirement, you also need to have a GPA of 2.0 or higher.

Rewrite the if statement so that it checks to see if a student meets both requirements using an and statement.

If they do, return the string:

"You meet the requirements to graduate!"

statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6)

credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")




Control Flow
Boolean Operators: or

The boolean operator or combines two expressions into a larger expression that is True if either component is True.

Consider the statement

Oranges are a fruit or apples are a vegetable.

This statement is composed of two expressions: oranges are a fruit which is True and apples are a vegetable which is False. Because the two expressions are connected by the or operator, the entire statement is True. Only one component needs to be True for an or statement to be True.

In English, or implies that if one component is True, then the other component must be False. This is not true in Python. If an or statement has two True components, it is also True.

Let’s take a look at a couple example in Python:

True or (3 + 4 == 7)    # True
(1 - 1 == 0) or False   # True
(2 < 0) or True         # True
(3 == 8) or (3 > 4)     # False

Notice that each or statement that has at least one True component is True, but the final statement has two False components, so it is False.
Instructions
1.

Set the variables statement_one and statement_two equal to the results of the following boolean expressions:

Statement one:

(2 - 1 > 3) or (-5 * 2 == -10)

Statement two:

(9 + 5 <= 15) or (7 != 4 + 3)

2.

The registrar’s office at Calvin Coolidge’s Cool College has another request. They want to send out a mailer with information on the commencement ceremonies to students who have met at least one requirement for graduation (120 credits and 2.0 GPA).

Write an if statement that checks if a student either has 120 or more credits or a GPA 2.0 or higher, and if so prints:

"You have met at least one of the requirements."


statement_one = (2 - 1 > 3) or (-5 * 2 == -10)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3)

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")




Control Flow
Boolean Operators: not

The final boolean operator we will cover is not. This operator is straightforward: when applied to any boolean expression it reverses the boolean value. So if we have a True statement and apply a not operator we get a False statement.

not True == False
not False == True

Consider the following statement:

Oranges are not a fruit.

Here, we took the True statement oranges are a fruit and added a not operator to make the False statement oranges are not a fruit.

This example in English is slightly different from the way it would appear in Python because in Python we add the not operator to the very beginning of the statement. Let’s take a look at some of those:

not 1 + 1 == 2  # False
not 7 < 0       # True

Instructions
1.

Set the variables statement_one and statement_two equal to the results of the following boolean expressions:

Statement one:

not (4 + 5 <= 9)

Statement two:

not (8 * 2) != 20 - 4

2.

The registrar’s office at Calvin Coolidge’s Cool College has been so impressed with your work so far that they have another task for you.

They want you to return to a previous if statement and add in several checks using and and not statements:

    If a student’s credits is not greater or equal to 120, it should print:

"You do not have enough credits to graduate."

    If their gpa is not greater or equal to 2.0, it should print:

"Your GPA is not high enough to graduate."

    If their credits is not greater than or equal to 120 and their gpa is not greater than or equal to 2.0, it should print:

"You do not meet either requirement to graduate!"

Make sure your return value matches those strings exactly. Capitalization, punctuation, and spaces matter!

statement_one = not (4 + 5 <= 9)

statement_two = not (8 * 2) != 20 - 4

credits = 120
gpa = 1.8

if not (credits >= 120):
  print("You do not have enough credits to graduate.")

 if not (gpa >= 2.0):
   print("Your GPA is not high enough to graduate.")

 if not (credits >= 120) and not (gpa >= 2.0):
   print("You do not meet either requirement to graduate!")






Else Statements

As you can tell from your work with Calvin Coolidge’s Cool College, once you start including lots of if statements in a function the code becomes a little cluttered and clunky. Luckily, there are other tools we can use to build control flow.

else statements allow us to elegantly describe what we want our code to do when certain conditions are not met.

else statements always appear in conjunction with if statements. Consider our waking-up example to see how this works:

if weekday:
  print("wake up at 6:30")
else:
  print("sleep in")

In this way, we can build if statements that execute different code if conditions are or are not met. This prevents us from needing to write if statements for each possible condition, we can instead write a blanket else statement for all the times the condition is not met.

Let’s return to our if statement for our movie streaming platform. Previously, all it did was check if the user’s age was over 13 and if so, print out a message. We can use an else statement to return a message in the event the user is too young to watch the movie.

if age >= 13:
  print("Access granted.")
else:
  print("Sorry, you must be 13 or older to watch this movie.")

Instructions
1.

Calvin Coolidge’s Cool College has another request for you. They want you to add an additional check to a previous if statement. If a student is failing to meet both graduation requirements, they want it to print:

"You do not meet the requirements to graduate."

Add an else statement to the existing if statement.

credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")



Else If Statements

We have if statements, we have else statements, we can also have elif statements.

Now you may be asking yourself, what the heck is an elif statement? It’s exactly what it sounds like, “else if”. An elif statement checks another condition after the previous if statements conditions aren’t met.

We can use elif statements to control the order we want our program to check each of our conditional statements. First, the if statement is checked, then each elif statement is checked from top to bottom, then finally the else code is executed if none of the previous conditions have been met.

Let’s take a look at this in practice. The following if statement will display a “thank you” message after someone donates to a charity; there will be a curated message based on how much was donated.

print("Thank you for the donation!")
 
if donation >= 1000:
  print("You've achieved platinum status")
elif donation >= 500:
  print("You've achieved gold donor status")
elif donation >= 100:
  print("You've achieved silver donor status")
else:
  print("You've achieved bronze donor status")

Take a second to think about this function. What would happen if all of the elif statements were simply if statements? If you donated $1100.00, then the first three messages would all print because each if condition had been met.

But because we used elif statements, it checks each condition sequentially and only prints one message. If I donate $600.00, the code first checks if that is over 1000, which it is not, then it checks if it’s over 500, which it is, so it prints that message, then because all of the other statements are elif and else, none of them get checked and no more messages get printed.

Try your hand at some other elif statements.
Instructions
1.

Calvin Coolidge’s Cool College has noticed that students prefer to get letter grades.

Write an if/elif/else statement that:

    If grade is 90 or higher, print "A"
    Else if grade is 80 or higher, print "B"
    Else if grade is 70 or higher, print "C"
    Else if grade is 60 or higher, print "D"
    Else, print "F"

grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
  print("B")
elif grade >= 70:
  print("C")
elif grade >= 60:
  print("D")
else:
  print("F")




Control Flow
Review

Great job! We covered a ton of material in this lesson and we’ve increased the number of tools in our Python toolkit by several-fold. Let’s review what we’ve learned this lesson:

    Boolean expressions are statements that can be either True or False
    A boolean variable is a variable that is set to either True or False.
    We can create boolean expressions using relational operators:
        ==: Equals
        !=: Not equals
        >: Greater than
        >=: Greater than or equal to
        <: Less than
        <=: Less than or equal to
    if statements can be used to create control flow in your code.
    else statements can be used to execute code when the conditions of an if statement are not met.
    elif statements can be used to build additional checks into your if statements

Let’s put these skills to the test!
Instructions
1.

Optional: Little Codey is an interplanetary space boxer, who is trying to win championship belts for various weight categories on other planets within the solar system.

Write a space.py program that helps him keep track of his target weight by:

    Checks which number planet is equal to.
    It should then compute his weight on the destination planet.

Here is the table of conversion:
# 	Planet 	Relative Gravity
1 	Venus 	0.91
2 	Mars 	0.38
3 	Jupiter 	2.34
4 	Saturn 	1.06
5 	Uranus 	0.92
6 	Neptune 	1.19

print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")
 
weight = 185
planet = 3

# Write an if statement below:
if (planet == 'Mercury'):
   print('The weight on planet Mercury is ' + weight * 0.378)
elif (planet == 'Venus'):
     print('The weight on planet Venus is ' + weight * 0.907)
elif (planet == 'Mars'):
     print('The weight on planet Mars is ' + weight * 0.377)
elif (planet == 'Jupiter'):
     print('The weight on planet Jupiter is ' + weight * 2.36)
elif (planet == 'Saturn'):
     print('The weight on planet Saturn is ' + weight * 0.916)
else:
     print('Invalid Planet Entry. Try: Mercury, Venus, Mars, Jupiter, or Saturn.')








Magic 8-Ball

The Magic 8-Ball is a popular toy developed in the 1950s for fortune-telling or advice seeking.

Write a magic8.py Python program that can answer any “Yes” or “No” question with a different fortune each time it executes.

Magic 8-Ball, should I do this project?

We’ll be using the following 9 possible answers for our Magic 8-Ball:

    Yes - definitely.
    It is decidedly so.
    Without a doubt.
    Reply hazy, try again.
    Ask again later.
    Better not tell you now.
    My sources say no.
    Outlook not so good.
    Very doubtful.

The output of the program will have the following format:

[Name] asks: [Question]
Magic 8-Ball’s answer: [Answer]

For example:

Joe asks: Is this real life?
Magic 8-Ball's answer: Better not tell you now

Let’s get started!


Setting up
1.

In magic8.py, declare a variable name and assign it to the name of the person who will be asking the Magic 8-Ball.
2.

Next, declare a variable question, and assign to a “Yes” or “No” question you’d like to ask the Magic 8-Ball.
3.

We want to store the answer of the Magic 8-Ball in another variable, which we’ll call answer. For now, assign this variable to an empty string.
Generating a random number
4.

In order for the answer to be different each time we run the program, we will utilize randomly generated values.

Note: This will be something new! But don’t worry, we will try to explain this topic thoroughly and also supply the code.

In Python, we can use the .randint() function from the random module to generate a random number from a range.

But first, let’s import this module so we can use its functions. Add this line of code to the top of magic8.py:

import random

5.

Next, we’ll create a variable to store the randomly generated value. Declare a variable called random_number, and assign it to the function call:

random.randint(1, 9)

which will generate a random number between 1 (inclusive) and 9 (inclusive).

Next, add a print() statement that outputs the value of random_number, and run the program several times to ensure random values are being generated as expected.

Once you’re sure this is working as we expected, feel free to comment out this print() statement.
Control Flow
6.

Now that we’ve declared all the variables needed, it’s time to implement the core logic of our program!

For this section, we’ll be utilizing control flow using an if/elif/else statement to assign different answers for each randomly generated value.

First, write an if statement where if the random_number is equal to 1, answer is assigned to the phrase “Yes - definitely.”
7.

Next, write an elif statement after the if statement where if the random_number is equal to 2, answer is assigned to the phrase “It is decidedly so”.

Then, continue writing elif statements for each of the remaining phrases for the values 3 to 9.

Recall that the 9 possible answers of the Magic 8-Ball are:

    Yes - definitely.

    It is decidedly so.

    Without a doubt.

    Reply hazy, try again.

    Ask again later.

    Better not tell you now.

    My sources say no.

    Outlook not so good.

    Very doubtful.

8.

Following the if/elif statements, add an else statement that will set answer to the string “Error”, if the number was accidentally assigned a value outside of our range.
Seeing the result
9.

Now, let’s see our program in action! Write a print() statement to output the asker’s name and their question, which should be in the following format:

[Name] asks: [Question]

For example, when we run the program, the output should look something like:

Joe asks: Will I win the lottery?

10.

Add a second print() statement that will output the Magic 8-Ball’s answer in the following format:

Magic 8-Ball's answer: [answer]

For example, when running the program it should look something like:

Magic 8-Ball's answer: My sources say no

11.

Great job! You’ve successfully utilized your knowledge of conditionals and previous fundamental Python concepts to create a program that generates different fortunes.

Run your program several times to see that it’s working as expected.
Optional Challenges
12.

If you’re up for some more challenges, try implementing the following features to your program.

So far, the Magic 8-Ball provides 9 possible fortunes. Try to add a few more possible answers to the program.

To do this, you will need to increase the range of randomly generated numbers and add additional elif statements for each new answer.
13.

What if the asker does not provide a name, such that the value of name is an empty string? If the name string is empty, the output of the program looks like the following:

 asks: Will I win the lottery?
Magic 8 Ball's answer: Outlook not so good

As you can see, the formatting of the output can use some improvement when there is no name provided.

We can address this by printing out just the question, such that it looks like the following:

Question: Will I win the lottery?
Magic 8-Ball's answer: Outlook not so good

You can implement this by creating an if/else statement such that:

    If the name is an empty string, it will only print the question.
    Else, the player’s name and question are both printed.

14.

What if the question string is empty? If the user does not provide any question, then the Magic 8-Ball cannot provide a fortune, otherwise, the fabric of reality is at risk!

To ensure that the fabric of reality is safe, we can create an if/else statement where:

    If the question is an empty string, print out a message to the user.
    Else, print the name and question, with the Magic 8-Ball’s answer.

Solution
15.

Don’t forget to check off all the tasks before moving on.

Sample solutions:

    magic8.py

P.S. If you make something cool, share it with us!


import random
name = "John"
question = "Yes"
answer = ""
random_number = random.randint(1, 9)
print(random_number)
if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

if name == "":
  print("Question: Will I win the lottery?")
else:
  print(name + " asks: " + " Will I win the lottery?")

if question == "":
  print("No Question")
else: 
  print("Magic 8-Ball's answer: ", answer)





Sal's Shipping

Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers. Sal wants to make sure that every single one of his customers has the best, and most affordable experience shipping their packages.

In this project, you’ll build a program that will take the weight of a package and determine the cheapest way to ship that package using Sal’s Shippers.

Sal’s Shippers has several different options for a customer to ship their package:

    Ground Shipping, which is a small flat charge plus a rate based on the weight of your package.
    Ground Shipping Premium, which is a much higher flat charge, but you aren’t charged for weight.
    Drone Shipping (new), which has no flat charge, but the rate based on weight is triple the rate of ground shipping.

Here are the prices:

Ground Shipping
Weight of Package 	Price per Pound 	Flat Charge
2 lb or less 	$1.50 	$20.00
Over 2 lb but less than or equal to 6 lb 	$3.00 	$20.00
Over 6 lb but less than or equal to 10 lb 	$4.00 	$20.00
Over 10 lb 	$4.75 	$20.00

Ground Shipping Premium

Flat charge: $125.00

Drone Shipping
Weight of Package 	Price per Pound 	Flat Charge
2 lb or less 	$4.50 	$0.00
Over 2 lb but less than or equal to 6 lb 	$9.00 	$0.00
Over 6 lb but less than or equal to 10 lb 	$12.00 	$0.00
Over 10 lb 	$14.25 	$0.00

Write a shipping.py Python program that asks the user for the weight of their package and then tells them which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.


https://www.codecademy.com/courses/learn-python-3/projects/python-sals-shipping






















