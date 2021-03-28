# Python Start

https://www.codecademy.com/learn/learn-python-3/modules/learn-python3-hello-world/cheatsheet


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

```py
meal = "An english muffin"

# Printing out breakfast
print("Breakfast:") 
print(meal)

# Now update meal to be lunch!
meal = "Sandwich"

# Printing out lunch
print("Lunch:") 
print(meal)

# Now update "meal" to be dinner
meal = "Chicken"

# Printing out dinner
print("Dinner:") print(meal)
```

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

an_int = 2 a_float = 2.1

print(an_int + 3)
prints 5



An integer, or int, is a whole number. It has no decimal point and contains all counting numbers (1, 2, 3, �) as well as their negative counterparts and the number 0. If you were counting the number of people in a room, the number of jellybeans in a jar, or the number of keys on a keyboard you would likely use an integer.

A floating-point number, or a float, is a decimal number. It can be used to represent fractional quantities as well as precise measurements. If you were measuring the length of your bedroom wall, calculating the average test score of a seventh-grade class, or storing a baseball player�s batting average for the 1998 season you would likely use a float.

Numbers can be assigned to variables or used literally in a program:

an_int = 2
a_float = 2.1
 
print(an_int + 3)
# Output: 5

Above we defined an integer and a float as the variables an_int and a_float. We printed out the sum of the variable an_int with the number 3. We call the number 3 here a literal, meaning it�s actually the number 3 and not a variable with the number 3 assigned to it.

Floating-point numbers can behave in some unexpected ways due to how computers store them. For more information on floating-point numbers and Python, review 



Calculations

Computers absolutely excel at performing calculations. The �compute� in their name comes from their historical association with providing answers to mathematical questions. Python performs addition, subtraction, multiplication, and division with +, -, *, and /.

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

Changing Numbers

Variables that are assigned numeric values can be treated the same as the numbers themselves. Two variables can be added together, divided by 2, and multiplied by a third variable without Python distinguishing between the variables and literals (like the number 2 in this example). Performing arithmetic on variables does not change the variable � you can only update a variable using the = sign.

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

We create two variables and assign numeric values to them. Then we perform a calculation on them. This doesn�t update the variables! When we update the coffee_price variable and perform the calculations again, they use the updated values for the variable!

Instructions

1.

You've decided to get into quilting! To calculate the number of squares you'll need for your first quilt let's create two variables: quilt_width and quilt_length. Let's make this first quilt 8 squares wide and 12 squares long.

```py
quilt_width = 8
quilt_length = 12
number_of_squares = quilt_width * quilt_length
print(number_of_squares)
quilt_length = 8
print(number_of_squares)
```

---

## Exponents

Python can also perform exponentiation. In written math, you might see an exponent as a superscript number, but typing superscript numbers isn�t always easy on modern keyboards. Since this operation is so related to multiplication, we use the notation **.

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

Using the exponent operator, print out how many squares you�ll need for a 6x6 quilt, a 7x7 quilt, and an 8x8 quilt.

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

You're trying to divide a group into four teams. All of you count off, and you get number 27.

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

output: 3
2
0
```

---

## Concatenation

The + operator doesn't just add two numbers, it can also add two strings! The process of combining two strings is called string concatenation. Performing string concatenation creates a brand new string comprised of the first string's contents followed by the second string's contents (without any added space in-between).

```py
greeting_text = "Hey there!"
question_text = "How are you doing?"
full_text = greeting_text + question_text
 
# Prints "Hey there!How are you doing?"
print(full_text)
```

In this sample of code, we create two variables that hold strings and then concatenate them. But we notice that the result was missing a space between the two, let�s add the space in-between using the same concatenation operator!

```py
full_text = greeting_text + " " + question_text
 
# Prints "Hey there! How are you doing?"
print(full_text)
```

Now the code prints the message we expected.

If you want to concatenate a string with a number you will need to make the number a string first, using the str() function. If you're trying to print() a numeric variable you can use commas to pass it as a different argument rather than converting it to a string.

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

Using str() we can convert variables that are not strings to strings and then concatenate them. But we don�t need to convert a number to a string for it to be an argument to a print statement.

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

Above, we keep a running count of the number of miles a person has gone hiking over time. Instead of recalculating from the start, we keep a grand total and update it when we've gone hiking further.

The plus-equals operator also can be used for string concatenation, like so:

hike_caption = "What an amazing time to walk through nature!"

```py 
# Almost forgot the hashtags!
hike_caption += " #nofilter"
hike_caption += " #blessed"
```

We create the social media caption for the photograph of nature we took on our hike, but then update the caption to include important social media tags we almost forgot.

Instructions

1.

We're doing a little bit of online shopping and find a pair of new sneakers. Right before we check out, we spot a nice sweater and some fun books we also want to purchase!

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

Python strings are very flexible, but if we try to create a string that occupies multiple lines we find ourselves face-to-face with a SyntaxError. Python offers a solution: multi-line strings. By using three quote-marks (""" or ''') instead of one, we tell the program that the string doesn�t end until the next triple-quote. This method is useful if the string being defined contains a lot of quotation marks and we want to be sure we don�t close it prematurely.

```py
leaves_of_grass = """
Poets to come! orators, singers, musicians to come!
Not to-day is to justify me and answer what I am for,
But you, a new brood, native, athletic, continental, greater than
  before known,
Arouse! for you must justify me.
"""
```

In the above example, we assign a famous poet�s words to a variable. Even though the quote contains multiple linebreaks, the code works!

If a multi-line string isn�t assigned a variable or used in an expression it is treated as a comment.

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

## Review

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

ASCII art is a graphic design technique that uses computers for presentation and consists of pictures pieced together from individual characters.

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

Don't forget to check off all the tasks before moving on.

Sample solutions:

    initials.py
    snowman.py

P.S. If you make something cool, share it with us!

```py
# Sonny Li
# Fun Fact: I played guitar in a band called Attica.

print("  SSS   L     ")
print(" S   S  L     ")
print(" S      L     ")
print("  SSS   L     ")
print("     S  L     ")
print(" S   S  L     ")
print("  SSS   LLLLL ")
```
