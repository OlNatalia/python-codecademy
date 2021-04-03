# Python Lists

## Introduction to Lists

What is a List?

In programming, it is common to want to work with collections of data. In Python, a **list is one of the many built-in data structures that allows us to work with a collection of data in sequential order**.

Suppose we want to make a list of the heights of students in a class:

    Noelle is 61 inches tall
    Ava is 70 inches tall
    Sam is 67 inches tall
    Mia is 64 inches tall

In Python, we can create a variable called heights to store these integers into a list:

```py
heights = [61, 70, 67, 64]
```

:memo: Notice that:

    A list begins and ends with square brackets ([ and ]).

    Each item (i.e., 67 or 70) is separated by a comma (,)

    It’s considered good practice to insert a space () after each comma, but your code will run just fine if you forget the space.

Let’s write our own list!

### Exercise Instructions

1.

Examine the existing list heights in your code editor.

A new student just joined the class!

    Chloe is 65 inches tall

Add Chloe’s height to the end of the list heights.

2.

Remove the # in front of the definition of the list broken_heights. If you run this code, you’ll get an error in your terminal:

```
SyntaxError: invalid syntax

Add commas (,) to broken_heights so that it runs without errors.

heights = [61, 70, 67, 64, 65]

broken_heights = [65, 71, 59, 62]
```


What can a List contain?

Lists can contain more than just numbers.

Let’s revisit our classroom example with heights:

    Noelle is 61 inches tall
    Ava is 70 inches tall
    Sam is 67 inches tall
    Mia is 64 inches tall

Instead of storing each student’s height, we can make a list that contains their names:

```py
names = ["Noelle", "Ava", "Sam", "Mia"]
```

We can even combine multiple data types in one list. For example, this list contains both a string and an integer:

```py
mixed_list_string_number = ["Noelle", 61]
```

Lists can contain any data type in Python! For example, this list contains a string, integer, boolean, and float.

```py
mixed_list_common = ["Mia", 27, False, 0.5]
```

Let’s experiment with different data types in our own lists!

https://discuss.codecademy.com/c/get-help/1801

### Instructions

1.

Add any additional string to the end of the list ints_and_strings.

2.

Create a new list called sam_height_and_testscore that contains:

    The string "Sam" (to represent sam’s name)
    The number 67 (to represent sam’s average grade)
    The float 85.5 (to represent sam’s score)
    The boolean True (to represent sam passing the test)

Make sure to write the elements in exact order.

```py
ints_and_strings = [1, 2, 3, "four", "five", "ok"]
sam_height_and_testscore = ["Sam", 67, 85.5, True]
```

---

## Empty Lists

A list doesn’t have to contain anything. You can create an empty list like this:

```py
empty_list = []
```

Why would we create an empty list?

Usually, it’s because we’re planning on filling it up later based on some other input. We’ll talk about two ways of filling up a list in the next exercise.

Let’s practice writing an empty list!

### Instructions

1.

Create an empty list and call it my_empty_list. Don’t put anything in the list just yet.

Remember that a list begins and ends with square brackets ([ and ]) and does not have to contain any elements.

```py
my_empty_list = []
```

---

## List Methods

As we start exploring lists further in the next exercises, we will encounter the concept of a method.

In Python, for any specific data-type ( strings, booleans, lists, etc. ) there is built-in functionality that we can use to create, manipulate, and even delete our data. We call this built-in functionality a method.

For lists, methods will follow the form of list_name.method(). Some methods will require an input value that will go between the parenthesis of the method ( ).

An example of a popular list method is .append(), which allows us to add an element to the end of a list.

```py
append_example = [ 'This', 'is', 'an', 'example']
append_example.append('list')
 
print(append_example)

# output:
['This', 'is', 'an', 'example', 'list']
```

We will be exploring .append() and many other methods in the upcoming exercises but for now take a second to examine the graphic that lists a few common methods that exist in Python for lists.
Instructions

We will be exploring .append() and many other methods in the upcoming exercises but for now take a second to examine and play around with the code for two common list methods.

```py
example_list = [1, 2, 3, 4]

#Using Append
example_list.append(5)
# print(example_list)

#Using Remove
example_list.remove(5)
# print(example_list)
```


## Growing a List: Append

We can add a single element to a list using the .append() Python method.

Suppose we have an empty list called garden:

```py
garden = []
garden.append("Tomatoes")
 
print(garden)
# output:
['Tomatoes']
```

We see that garden now contains "Tomatoes"!

When we use .append() on a list that already has elements, our new element is added to the end of the list:

```py
# Create a list
garden = ["Tomatoes", "Grapes", "Cauliflower"]
 
# Append a new element
garden.append("Green Beans")
print(garden)

# output:
['Tomatoes', 'Grapes', 'Cauliflower', 'Green Beans']
```

Let’s use the .append() method to manipulate a list.

### Instructions

1.

Jiho works for a gardening store called Petal Power. Jiho keeps a record of orders in a list called orders.

Use print to inspect the orders he has received today.

2.

Jiho just received a new order for "tulips". Use append to add this string to orders.

3.

Another order has come in! Use append to add "roses" to orders.

4.

Use print to inspect the orders Jiho has received today.

```py
orders = ["daisies", "periwinkle"]
print(orders)
orders.append("tulips")
orders.append("roses")
print(orders)
```

## Growing a List: Plus (+)

When we want to add multiple items to a list, we can use + to combine two lists (this is also known as concatenation).

Below, we have a list of items sold at a bakery called items_sold:

```py
items_sold = ["cake", "cookie", "bread"]

Suppose the bakery wants to start selling "biscuit" and "tart":

items_sold_new = items_sold + ["biscuit", "tart"]
print(items_sold_new)

# output:
['cake', 'cookie', 'bread', 'biscuit', 'tart']
```

In this example, we created a new variable, items_sold_new, which contained both the original items sold, and the new items. We can inspect the original items_sold and see that it did not change:

```py
print(items_sold)

# output:
['cake', 'cookie', 'bread']
```

We can only use + with other lists. If we type in this code:

:x:

```py
my_list = [1, 2, 3]
my_list + 4

# we will get the following error:

TypeError: can only concatenate list (not "int") to list
```

If we want to add a single element using +, we have to put it into a list with brackets ([]):

:white_check_mark:

```py
my_list + [4]
```

<br>

Let’s use + to practice combining two lists!

### Instructions

1.

Jiho is updating a list of orders. He just received orders for "lilac" and "iris".

Create a list called new_orders that contains our new orders.

2.

Use + to create a new list called orders_combined that combines orders with new_orders.

3.

Remove the # and whitespace in front of the list broken_prices. If you run this code, you’ll get an error:

```
TypeError: can only concatenate list (not "int") to list
```

Fix the command by inserting brackets ([ and ]) so that it will run without errors.

```py
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]

# Create new orders here:
new_orders = ["lilac", "iris"]
orders_combined  = orders + new_orders

broken_prices = [5, 3, 4, 5, 4] + [4]
```

<br>

## Accessing List Elements

We are interviewing candidates for a job. We will call each candidate in order, represented by a Python list:

```py
calls = ["Juan", "Zofia", "Amare", "Ezio", "Ananya"]
```

First, we’ll call "Juan", then "Zofia", etc.

In Python, we call the location of an element in a list its index.

Python lists are zero-indexed. This means that the first element in a list has index 0, rather than 1.

Here are the index numbers for the list calls:

    Element 	Index
    "Juan" 	0
    "Zofia" 	1
    "Amare" 	2
    "Ezio" 	3
    "Ananya" 	4

In this example, the element with index 2 is "Amare".

We can select a single element from a list by using square brackets ([]) and the index of the list item. If we wanted to select the third element from the list, we’d use calls[2]:

```py
print(calls[2])
# Will output:
Amare
```

Note: When accessing elements of an array, you must use an int as the index. If you use a float, you will get an error. This can be especially tricky when using division. For example print(calls[4/2]) will result in an error, because 4/2 gets evaluated to the float 2.0.

To solve this problem, you can force the result of your division to be an int by using the int() function. int() takes a number and cuts off the decimal point. For example, int(5.9) and int(5.0) will both become 5. Therefore, calls[int(4/2)] will result in the same value as calls[2], whereas calls[4/2] will result in an error.

### Instructions

1.

Use square brackets ([ and ]) to select the 4th employee from the list employees. Save it to the variable employee_four.

2.

Paste the following code into script.py:
```py
print(employees[8])
```

What happens? Why?

3.

Selecting an element that does not exist produces an IndexError.

In the line of code that you pasted, change 8 to an index that exists so that you don’t get an IndexError.

Run your code again!

```py
employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
employee_four = employees[3]
print(employees[0])
```

## Accessing List Elements: Negative Index

What if we want to select the last element of a list?

We can use the index -1 to select the last item of a list, even when we don’t know how many elements are in a list.

Consider the following list with 6 elements:

```py
pancake_recipe = ["eggs", "flour", "butter", "milk", "sugar", "love"]
```

If we select the -1 index, we get the final element, "love".

```py
print(pancake_recipe[-1])
# output:
love
```

This is equivalent to selecting the element with index 5:

```py
print(pancake_recipe[5])
# output:
love
```

Here are the negative index numbers for our list:

    Element 	Index
    "eggs" 	-6
    "flour" 	-5
    "butter" 	-4
    "milk" 	-3
    "sugar" 	-2
    "love" 	-1

### Instructions

1.

Create a called variable last_element.

Assign the last element in shopping_list to the variable last_element using a negative index.

2.

Now select the element with index 5 and save it to the variable index5_element.

3.

Use print to display both element5 and last_element.

```py
Note that they are equal to "cereal"!

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = shopping_list[-1]
index5_element = shopping_list[5]
print(last_element, index5_element)
```

## Modifying List Elements

Let’s return to our garden.

```py
garden = ["Tomatoes", "Green Beans", "Cauliflower", "Grapes"]
```

Unfortunately, we forgot to water our cauliflower and we don’t think it is going to recover.

Thankfully our friend Jiho from Petal Power came to the rescue. Jiho gifted us some strawberry seeds. We will replace the cauliflower with our new seeds.

We will need to modify the list to accommodate the change to our garden list. To change a value in a list, reassign the value using the specific index.

```py
garden[2] = "Strawberries"
print(garden)
# output:
["Tomatoes", "Green Beans", "Strawberries", "Grapes"]
```

Negative indices will work as well.

```py
garden[-1] = "Raspberries"
print(garden)
# output:
["Tomatoes", "Green Beans", "Strawberries", "Raspberries"]
```

### Instructions

1.

We have decided to start selling some of our garden produce. Word around our town has spread and people are interested in getting some of our delicious vegetables and fruit.

We decided to create a waitlist to make sure we can sell to all of our new customers!

Define a list called garden_waitlist and set the value to contain our customers (in order): "Jiho", "Adam", "Sonny", and "Alisha".

2.

"Adam" decided his fridge is too full at the moment and asked us to remove him from the waitlist and make space for one of our other townsfolk.

Replace "Adam" with our other interested customer "Calla" using the index method we used in the narrative.

Print garden_waitlist to see the change!

3.

Alisha realized she was already stocked with all the items we are selling. She asked us to replace her with her friend Alex who just ran out.

Replace Alisha with Alex using a negative index.

Print garden_waitlist again to see the change!

```py
garden_waitlist = ["Jiho", "Adam", "Sonny", "Alisha"]
garden_waitlist [1] = "Calla"
print(garden_waitlist )
garden_waitlist [-1] = "Alex"
print(garden_waitlist )
```

<br>

## Shrinking a List: Remove

We can remove elements in a list using the .remove() Python method.

Suppose we have a filled list called shopping_line that represents a line at a grocery store:

```py
shopping_line = ["Cole", "Kip", "Chris", "Sylvana"]
```

We could remove "Chris" by using the .remove() method:

```py
shopping_line.remove("Chris")
print(shopping_line)
# If we examine shopping_line, we can see that it now doesn’t contain "Chris":
["Cole", "Kip", "Sylvana"]
```

We can also use .remove() on a list that has duplicate elements.

Only the first instance of the matching element is removed:

```py
# Create a list
shopping_line = ["Cole", "Kip", "Chris", "Sylvana", "Chris"]
 
# Remove a element
shopping_line.remove("Chris")
print(shopping_line)
# output:
["Cole", "Kip", "Sylvana", "Chris"]
```

Let’s practice using the .remove() method to remove elements from a list.

### Instructions

1.

We have decided to get into the grocery store business. Our manager Calla has decided to store all the inventory purchases in a list to help track what products need to be ordered.

Let’s create a list called order_list with the following values (in this particular order):

```py
"Celery", "Orange Juice", "Orange", "Flatbread"
```

Print order_list to see the current list.

2.

We are in luck! We actually found a spare case of "Flatbread" in our back storage. We won’t need to order it anymore. Let’s remove it from order_list using the .remove() method.

Print order_list to see the current list.

3.

Our store has grown to be a huge success! We decided to open a second store and require a new order list. Calla has done us the favor of putting one together.

Create a new list called new_store_order_list and assign it the following values (in order):

"Orange", "Apple", "Mango", "Broccoli", "Mango"

Note: Our second store is going to need two orders of mangos so the value is duplicated.

Print new_store_order_list to see the current list.

4.

We are in luck again! We actually found a spare case of "Mango" in our back storage.

We won’t be needing to place two orders anymore.

Let’s remove it from new_store_order_list using the .remove() method.

Print new_store_order_list to see the current list.

5.

Calla ran to tell us some important news! She asked us to remove "Onions" from our new new_store_order_list. If we double-check our list, we will notice we don’t have "Onions" on our list.

Let’s see what happens when we try to remove an item that does not exist.

Call the .remove() method with the value of "Onions" on our new_store_order_list list

```py
# Your code below: 
order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)
new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)
new_store_order_list.remove("Mango")
print(new_store_order_list)
# new_store_order_list.remove("Onions")
```

<br>

---

## Two-Dimensional (2D) Lists

We’ve seen that the items in a list can be numbers or strings. Lists can contain other lists! We will commonly refer to these as two-dimensional (2D) lists.

Once more, let’s look at a class height example:

    Noelle is 61 inches tall
    Ava is 70 inches tall
    Sam is 67 inches tall
    Mia is 64 inches tall

Previously, we saw that we could create a list representing both Noelle’s name and height:

```py
noelle = ["Noelle", 61]
```

We can put several of these lists into one list, such that each entry in the list represents a student and their height:

```py
heights = [["Noelle", 61], ["Ava", 70], ["Sam", 67], ["Mia", 64]]
```

We will often find that a two-dimensional list is a very good structure for representing grids such as games like tic-tac-toe.

#A 2d list with three lists in each of the indices. 

```py
tic_tac_toe = [
            [["X"],["O"],["X"]], 
            [["O"],["X"],["O"]], 
            [["O"],["O"],["X"]]
]
```

Let’s practice creating our own 2D list!

### Instructions

1.

A new student named "Vik" has joined our class. Vik is 68 inches tall. Add a sublist to the end of the heights list that represents Vik and his height.

2.

Create a two-dimensional list called ages where each sublist contains a student’s name and their age. Use the following data:

    "Aaron" is 15
    "Dhruti" is 16

```py
heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64], ["Vik", 68]]
ages = [["Aaron", 15], ["Dhruti", 16]]
```

## Accessing 2D Lists

Let’s return to our classroom heights example:

```py
heights = [["Noelle", 61], ["Ali", 70], ["Sam", 67]]
```

Two-dimensional lists can be accessed similar to their one-dimensional counterpart. Instead of providing a single pair of brackets [ ] we will use an additional set for each dimension past the first.

If we wanted to access "Noelle"‘s height:

```py
#Access the sublist at index 0, and then access the 1st index of that sublist. 
noelles_height = heights[0][1] 
print(noelles_height)
# output:
61
```

Here are the index numbers to access data for the list heights:

    Element 	Index
    "Noelle" 	heights[0][0]
    61 	heights[0][1]
    "Ali" 	heights[1][0]
    70 	heights[1][1]
    "Sam" 	heights[2][0]
    67 	heights[2][1]

Let’s practice accessing data in a two-dimensional list.

### Instructions

1.

We want to have a way to store all of our classroom test score data.

Using the provided table, create a two-dimensional list called class_name_test to represent the data. Each sublist in class_name_test should have one student’s name and their associated score.

    Name 	Test Score
    "Jenny" 	90
    "Alexus" 	85.5
    "Sam" 	83
    "Ellie" 	101.5

Print class_name_test to see the result.

2.

Use double square brackets ([][]) to select Sam‘s test score from the list class_name_test.

Save it to the variable sams_score.

Print the variable sams_score to see the result.

3.

Use double square brackets ([][]) to select Ellies test score from the list class_name_test. This time only use negative indices!

Save it to the variable ellies_score.

Print the variable ellies_score to see the result.

```py
#Your code below:
class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)

sams_score = class_name_test[2][0]
print(sams_score)

ellies_score = class_name_test[-1][-1]
print(ellies_score)
```
<br>

## Modifying 2D Lists

Now that we know how to access two-dimensional lists, modifying the elements should come naturally.

Let’s return to a classroom example, but now instead of heights or test scores, our list stores the student’s favorite hobby!

```py
class_name_hobbies = [["Jenny", "Breakdancing"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
```

"Jenny" changed their mind and is now more interested in "Meditation".

We will need to modify the list to accommodate the change to our class_name_hobbies list. To change a value in a two-dimensional list, reassign the value using the specific index.

```py
# The list of Jenny is at index 0. The hobby is at index 1. 
class_name_hobbies[0][1] = "Meditation"
print(class_name_hobbies)

# output:
[["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Soccer"]]
```

Negative indices will work as well.

```py
# The list of Jenny is at index 0. The hobby is at index 1. 
class_name_hobbies[-1][-1] = "Football"
print(class_name_hobbies)

# output:
[["Jenny", "Meditation"], ["Alexus", "Photography"], ["Grace", "Football"]]
```

### Instructions

1.

Our school is expanding! We are welcoming a new set of students today from all over the world.

Using the provided table, create a two-dimensional list called incoming_class to represent the data. Each sublist in incoming_class should contain the name, nationality, and grade for a single student.

    Name 	Nationality 	Grade Level
    "Kenny" 	"American" 	9
    "Tanya" 	"Russian" 	9
    "Madison" 	"Indian" 	7

Print incoming_class to see our list.

2.

"Madison" passed an exam to advance a grade. She will be pushed into 8th grade rather than her current 7th in our list.

Modify the list using double brackets [][] to make the change. Use positive inidices.

Print incoming_class to see our change.

3.

"Kenny" likes to be called by his nickname "Ken". Modify the list using double brackets [][] to accommodate the change but only using negative indices.

Print incoming_class to see our change.

```py
#Your code below:
incoming_class = [["Kenny", "American", 9], ["Tanya", "Russian", 9], ["Madison", "Indian", 7]]
print(incoming_class)
incoming_class[2][2] = 8
print(incoming_class)
incoming_class[-3][-3] = "Ken"
print(incoming_class)
```

<br>

---

## Review

So far, we have learned:

- How to create a list
- How to access, add, remove, and modify list elements
- How to create a two-dimensional list
- How to access and modify two-dimensional list elements

To combine two lists using +, define a new variable and set it to the two lists we want to combine with + in between.

Here is an example:

```py
1_to_3 = [1, 2, 3]
 
1_to_5 = 1_to_3 + [4, 5]
print(1_to_5)

# output:
[1, 2, 3, 4, 5]
```

To use the .remove() method on a two-dimensional list, call it on the sublist you are modifying and pass the value you want to remove in between the parenthesis ( ).

```py
practice_list = [["a"], ["b"], ["c"]]
practice_list[1].remove("b")
 
print(practice_list)
```

Let’s practice these skills.

### Instructions

1.

Maria is entering customer data for her web store business. We’re going to help her organize her data.

Start by turning this list of customer first names into a list called first_names. Make sure to enter the names in this order:

    Ainsley
    Ben
    Chani
    Depak

2.

Maria wants to track all customer’s preferred sizes for her clothing. Create a list called preferred_size.

Fill our new list preferred_size with the following data, containing the preferred sizes for Ainsley, Ben, and Chani:

```
["Small", "Large", "Medium"]
```

3.

On no! We forgot to add Depak’s size.

Depak’s size is "Medium". Use .append() to add "Medium" to the preferred_size list.

Print preferred_size to see our change.

4.

Maria is having a hard time visualizing which customer is associated with each size. Let’s restructure our two lists into a two-dimensional list to help Maria.

In addition to our already available data, Maria is adding a third value for each customer that reflects if they want expedited shipping on their orders.

This will be reflected using a boolean value (True for expedited, False for regular)

Create a two-dimensional list called customer_data using the following table as a reference for the data. Each sublist should contain a name, size, and expedited shipping option for a single person.

    Name 	Size 	Expedited Shipping
    "Ainsley" 	"Small" 	True
    "Ben" 	"Large" 	False
    "Chani" 	"Medium" 	True
    "Depak" 	"Medium" 	False

Print customer_data to see the data.

5.

"Chani" reached out to Maria. She requested to switch to regular shipping to save some money.

Change the data value for "Chani"‘s shipping preference to False in our two-dimensional list to reflect the change.

6.

"Ben" reached out to Maria asking to remove his shipping option because he is not sure what type he wants.

Use the .remove() method to delete the shipping value from the sublist that contains ben’s data.

Note: We never explicitly went over how to use the .remove() method on a 2d list together. If you feel like you are struggling, take a look at the hint for some guidance.

7.

Great job making it this far! One last thing, Maria received a new customer "Amit" and "Karim" that had the following data:

```py
[["Amit", "Large", True], ["Karim", "X-Large", False]]
```

Create a new variable customer_data_final. Combine our existing list customer_data with our new customer 2d list using + by adding it to the end of customer_data.

Print customer_data_final to see our final result.

```py
# Your code below: 

# Checkpoint 1
first_names = ["Ainsley", "Ben", "Chani", "Depak"]

# Checkpoint 2
preferred_size = ["Small", "Large", "Medium"]

# Checkpoint 3
preferred_size.append("Medium")
print(preferred_size)

# Checkpoint 4
customer_data = [["Ainsley", "Small", True ], ["Ben", "Large", False ], ["Chani", "Medium", True ], ["Depak", "Medium", False ]]
print(customer_data)

# Checkpoint 5
customer_data[2][2] = False

# Checkpoint 6
customer_data[1].remove(False)

# Checkpoint 7
customer_data_final = customer_data + [["Amit", "Large", True], ["Karim", "X-Large", False]]
print(customer_data_final)
```

<br>

---

### Gradebook

You are a student and you are trying to organize your subjects and grades using Python. Let’s explore what we’ve learned about lists to organize your subjects and scores.

Your grade for poetry is an 85 and the value exists at gradebook[2][1]. Use the .remove() method on this sublist and provide the value you want to remove.

sublist.remove(value)


Your grade for poetry should exist on the sublist gracebook[2]. Call append on this sublist with the value of "Pass"

sublist.append(value)

```py
last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]
```

Create Some Lists:

1.

Create a list called subjects and fill it with the classes you are taking:

    "physics"
    "calculus"
    "poetry"
    "history"

2.

Create a list called grades and fill it with your scores:

    98
    97
    85
    88

3.

Create a two-dimensional list to combine subjects and grades. Use the table below as a reference to associated values.

    Name 	Test Score
    "Physics" 	98
    "Calculus" 	97
    "Poetry" 	85
    "History" 	88

Assign the value into a variable called gradebook.

4.

Print gradebook.

Does it look how you expected it would?
Add More Subjects:

5.

Your grade for your computer science class just came in! You got a perfect score, 100!

Use the .append() method to add a list with the values of "Computer Science" and an associated grade value of 100 to our two-dimensional list of gradebook.

6.

Your grade for visual arts just came in! You got a 93!

Use append to add ["Visual Arts", 93] to gradebook.
Modify The Gradebook:

7.

Our instructor just told us they made a mistake grading and are rewarding an extra 5 points for our visual arts class.

Access the index of the grade for your visual arts class and modify it to be 5 points greater.

8.

You decided to switch from a numerical grade value to a Pass/Fail option for your poetry class.

Find the grade value in your gradebook for your poetry class and use the .remove() method to delete it.

Your grade for poetry is an 85 and the value exists at gradebook[2][1]. Use the .remove() method on this sublist and provide the value you want to remove.

```py
sublist.remove(value)
```

9.

Use the .append() method to then add a new "Pass" value to the sublist where your poetry class is located.

Your grade for poetry should exist on the sublist gracebook[2]. Call append on this sublist with the value of "Pass"

```py
sublist.append(value)
```

One Big Gradebook!

10.

You also have your grades from last semester, stored in last_semester_gradebook.

Create a new variable full_gradebook that combines both last_semester_gradebook and gradebook using + to have one complete grade book.

Print full_gradebook to see our completed list

```py
# Your code below: 
subjects = [
    "physics"
    "calculus"
    "poetry"
    "history"
]
grades = [98,97,85,88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

print(gradebook)

gradebook.append(["Computer Science", 100])
gradebook.append(["Visual Arts", 93])

gradebook[-1][-1] = 98
gradebook[2].remove(85)
gradebook[2].append("Pass")
# gradebook.append(["Poetry", "Pass"])

full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook) 
```

<br>

---

## Working with Lists

Now that we know how to create and access list data, we can start to explore additional ways of working with lists.

In this lesson, you’ll learn how to:

    Add and remove items from a list using a specific index.
    Create lists with continuous values.
    Get the length of a list.
    Select portions of a list (called slicing).
    Count the number of times that an element appears in a list.
    Sort a list of items.

Note: In some of the exercises, we will be using built-in functions in Python. If you haven’t yet explored the concept of a function, it may look a bit new. Below we compare it to the method syntax we learned in the earlier lesson.

Here is a preview:

```py
# Example syntax for methods
list.method(input)
 
# Example syntax for a built-in function 
builtinfuncion(input)
```


### Adding by Index: Insert

The Python list method .insert() allows us to add an element to a specific index in a list.

The .insert() method takes in two inputs:

    The index you want to insert into.
    The element you want to insert at the specified index.

The .insert() method will handle shifting over elements and can be used with negative indices.

To see it in action let’s imagine we have a list representing a line at a store:

```py
store_line = ["Karla", "Maxium", "Martim", "Isabella"]
```

"Maxium" saved a spot for his friend "Vikor" and we need to adjust the list to add him into the line right behind "Maxium".

For this example, we can assume that "Karla" is the front of the line and the rest of the elements are behind her.

Here is how we would use the .insert() method to insert "Vikor" :

```py
store_line.insert(2, "Vikor")
print(store_line) 

# output:
 ['Karla', 'Maxium', 'Viktor', 'Martim', 'Isabella']
```

:memo: Some important things to note:

    The order and number of the inputs is important. The .insert() method expects two inputs, the first being a numerical index, followed by any value as the second input.

    When we insert an element into a list, all elements from the specified index and up to the last index are shifted one index to the right. This does not apply to inserting an element to the very end of a list as it will simply add an additional index and no other elements will need to shift.

Let’s practice using .insert()!

### Instructions

1.

We are helping out a popular grocery store called Jiho’s Produce.

Every week the store has to choose the order in which it displays some of its popular items on sale in the front window to attract customers.

Jiho, the store owner, likes to store the items for the display in a list.

Check out the current display list in our code editor. Click Run to print out the list.

2.

Jiho found out some great news! "Pineapple" is back in stock.

Jiho would like to put "Pineapple" in the front of the list so it is the first item customers see in the display window.

Use .insert() to add "Pineapple" to the front of the list.

Print the resulting list to see the change.

Note: For this list, the front will be the element at index 0

```py
front_display_list = ["Mango", "Filet Mignon", "Chocolate Milk"]
print(front_display_list)

# Your code below: 
front_display_list.insert( 0, "Pineapple")
```

---

## Removing by Index: Pop

Just as we learned to insert elements at specific indices, Python gives us a method to remove elements at a specific index using a method called .pop().

The .pop() method takes an optional single input:

    The index for the element you want to remove.

To see it in action, let’s consider a list called cs_topics that stores a collection of topics one might study in a computer science program.

```py
cs_topics = ["Python", "Data Structures", "Balloon Making", "Algorithms", "Clowns 101"]
```

Two of these topics don’t look like they belong, let’s see how we remove them using .pop().

First let’s remove "Clowns 101":

```py
removed_element = cs_topics.pop()
print(cs_topics)
print(removed_element)

# output:
['Python', 'Data Structures', 'Balloon Making', 'Algorithms']
'Clowns 101'
```

Notice two things about this example:

    The method can be called without a specific index. Using .pop() without an index will remove whatever the last element of the list is. In our case "Clowns 101" gets removed.

    .pop() is unique in that it will return the value that was removed. If we wanted to know what element was deleted, simply assign a variable to the call of the .pop() method. In this case, we assigned it to removed_element.

Lastly let’s remove "Balloon Making":

```py
cs_topics.pop(2)
print(cs_topics)

# output:
['Python', 'Data Structures', 'Algorithms']
```

Notice two things about this example:

    The method can be called with an optional specific index to remove. In our case, the index 2 removes the value of "Balloon Making".
    We don’t have to save the removed value to any variable if we don’t care to use it later.

Note: Passing in an index that does not exist or calling .pop() on an empty list will both result in an IndexError.

Let’s apply what we learned about the .pop() method.

### Instructions

1.

We have decided to pursue the study of data science in addition to our computer science coursework. We signed up for an online school that would help us become proficient.

Check out the current list of topics we will be studying in our code editor.

Click Run to print out the list.

2.

It looks like we have an overlap with our computer science curriculum for the topic of "Python 3".

Let’s remove the topic from the list of data_science_topics using our newly learned .pop() method.

Print data_science_topics to see your result.

3.

Looks like there is overlap on the "Algorithms" topic as well. Let’s use .pop() to remove it as well.

Print data_science_topics to see the changes.

```py
data_science_topics = ["Machine Learning", "SQL", "Pandas", "Algorithms", "Statistics", "Python 3"]
print(data_science_topics)

# Your code below: 
data_science_topics .pop()
print(data_science_topics )

data_science_topics.pop(3)
print(data_science_topics )
```

<br>

---

## Consecutive Lists: Range

Often, we want to create a list of consecutive numbers in our programs. For example, suppose we want a list containing the numbers 0 through 9:

```py
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Typing out all of those numbers takes time and the more numbers we type, the more likely it is that we have a typo that can cause an error.

Python gives us an easy way of creating these types of lists using a built-in function called range().

The function range() takes a single input, and generates numbers starting at 0 and ending at the number before the input.

So, if we want the numbers from 0 through 9, we use range(10) because 10 is 1 greater than 9:

```py
my_range = range(10)
print(my_range)

# output:
range(0, 10)
```

Notice something different? The range() function is unique in that it creates a range object. It is not a typical list like the ones we have been working with.

In order to use this object as a list, we have to first convert it using another built-in function called list().

The list() function takes in a single input for the object you want to convert.

We use the list() function on our range object like this:

```py
print(list(my_range))

# output:
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

Let’s try out using range()!

### Instructions

1.

Modify number_list so that it is a range containing numbers starting at 0 and up to, but not including, 9.

2.

Create a range called zero_to_seven with the numbers 0 through 7.

Print the result in list form.

```py
number_list = range(0,9)
print(list(number_list))
zero_to_seven = range(0, 8)
print(zero_to_seven)
```

The Power of Range!

By default, range() creates a list starting at 0. However, if we call range() with two inputs, we can create a list that starts at a different number.

For example, range(2, 9) would generate numbers starting at 2 and ending at 8 (just before 9):

```py
my_list = range(2, 9)
print(list(my_list))
# output:
[2, 3, 4, 5, 6, 7, 8]
```

If we use a third input, we can create a list that “skips” numbers.

For example, range(2, 9, 2) will give us a list where each number is 2 greater than the previous number:

```py
my_range2 = range(2, 9, 2)
print(list(my_range2))
# output:
[2, 4, 6, 8]
```

We can skip as many numbers as we want!

For example, we’ll start at 1 and skip in increments of 10 between each number until we get to 100:

```py
my_range3 = range(1, 100, 10)
print(list(my_range3))
# output:
[1, 11, 21, 31, 41, 51, 61, 71, 81, 91]
```

Our list stops at 91 because the next number in the sequence would be 101, which is greater than 100 (our stopping point).

Let’s experiment with our additional range() inputs!

### Instructions

1.

Modify the range() function that created the range range_five_three such that it:

    Starts at 5
    Has a difference of 3 between each item
    Ends before 15

2.

Create a range called range_diff_five that:

    Starts at 0
    Has a difference of 5 between each item
    Ends before 40

```py
range_five_three = range(5, 15, 3)
range_diff_five = range(0, 40, 5)
```

<br>

---

## Length

Often, we’ll need to find the number of items in a list, usually called its length.

We can do this using a built-in function called len().

When we apply len() to a list, we get the number of elements in that list:

```py
my_list = [1, 2, 3, 4, 5]
 
print(len(my_list))
# output:
5
```

Let’s find the length of various lists!

### Instructions

1.

Calculate the length of long_list and save it to the variable long_list_len.

2.

Use print() to examine long_list_len.

3.

We have provided a completed range() function for the variable range_list.

Calculate its length using the function len() and save it to a variable called range_list_length.

Note: Range objects do not need to be converted to lists in order to determine their length

4.

Use print() to examine range_list_length.

5.

Change the range() function that generates range_list so that it skips 100 instead of 10 steps between items.

How does this change range_list_len?

```py
long_list = [1, 5, 6, 7, -23, 69.5, True, "very", "long", "list", "that", "keeps", "going.", "Let's", "practice", "getting", "the", "length"]

range_list = range(2, 3000, 100)

# Your code below: 
long_list_len = len(long_list)
print(long_list_len)

range_list_length = len(range_list)
print(range_list_length)
```

<br>

---

## Slicing Lists I

In Python, often we want to extract only a portion of a list. Dividing a list in such a manner is referred to as slicing.

Lets assume we have a list of letters:

```py
letters = ["a", "b", "c", "d", "e", "f", "g"]
```

Suppose we want to select from "b" through "f".

We can do this using the following syntax: letters[start:end], where:

    start is the index of the first element that we want to include in our selection. In this case, we want to start at "b", which has index 1.
    end is the index of one more than the last index that we want to include. The last element we want is "f", which has index 5, so end needs to be 6.

```py
sliced_list = letters[1:6]
print(sliced_list)

# output:
["b", "c", "d", "e", "f"]
```

Notice that the element at index 6 (which is "g") is not included in our selection.

### Instructions

1.

Use print() to examine the variable beginning.

Before hitting Run think about what elements beginning will contain?

2.

Modify beginning, so that it selects the first 2 elements of suitcase.

3.

Create a new list called middle that contains the middle two items ( ["pants", "pants"] ) from suitcase.

Print middle to see the slice!

```py
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

#beginning = suitcase[0:4]
beginning = suitcase[0:2]

# Your code below: 
print(beginning)

middle = suitcase[2:4]
print(middle)
```

## Slicing Lists II

Slicing syntax in Python is very flexible. Let’s look at a few more problems we can tackle with slicing.

Take the list fruits as our example:

```py
fruits = ["apple", "cherry", "pineapple", "orange", "mango"]
```

If we want to select the first n elements of a list, we could use the following code:

```py
fruits[:n]
```

For our fruits list, suppose we wanted to slice the first three elements.

The following code would start slicing from index 0 (omitted) and up to index 3.

```py
print(fruits[:3])

# output:
['apple', 'cherry', 'pineapple']
```

We can do something similar when we want to slice the last n elements in a list:

```py
fruits[-n:]
```

For our fruits list, suppose we wanted to slice the last two elements.

This code slices from the element at index -2 up to the last index(ommited).

```py
print(fruits[-2:])

# output:
['orange', 'mango']
```

Negative indices can also accomplish taking all but n last elements of a list.

```py
fruits[:-n]
```

For our fruits example, suppose we wanted to slice all but the last element from the list.

This example starts counting from the 0 index (omitted) up to the element at index -1.

```py
print(fruits[:-1])

# output:
['apple', 'cherry', 'pineapple', 'orange']
```

Let’s practice some of these extra slicing techniques!

### Instructions

1.

Create a new list called last_two_elements containing the final two elements of suitcase.

Print last_two_elements to see your result.

2.

Create a new list called slice_off_last_three containing all but the last three elements.

```py
suitcase = ["shirt", "shirt", "pants", "pants", "pajamas", "books"]

# Your code below: 
last_two_elements = suitcase[-2:]
print(last_two_elements)
slice_off_last_three = suitcase[:-3]
print(slice_off_last_three)

```

<br>

## Counting in a List

In Python, it is common to want to count occurrences of an item in a list.

Suppose we have a list called letters that represents the letters in the word “Mississippi”:

```py
letters = ["m", "i", "s", "s", "i", "s", "s", "i", "p", "p", "i"]
```

If we want to know how many times i appears in this word, we can use the list method called .count():

```py
num_i = letters.count("i")
print(num_i)

# output:
4
```

Notice that since .count() returns a value, we must assign it to a variable to use it.

We can even use .count() to count element appearances in a two-dimensional list.

Let’s use the list number_collection as an example:

```py
number_collection = [[100, 200], [100, 200], [475, 29], [34, 34]]
```

If we wanted to know how often the sublist [100, 200] appears:

```py
num_pairs = number_collection.count([100, 200])
print(num_pairs)

# output:
2
```

Let’s count some list items using the .count() method!

### Instructions

1.

Mrs. Wilson’s class is voting for class president. She has saved each student’s vote into the list votes.

Use .count() to determine how many students voted for "Jake" and save the value to a variable called jake_votes.

2.

Use print() to examine jake_votes.

```py
votes = ["Jake", "Jake", "Laurie", "Laurie", "Laurie", "Jake", "Jake", "Jake", "Laurie", "Cassie", "Cassie", "Jake", "Jake", "Cassie", "Laurie", "Cassie", "Jake", "Jake", "Cassie", "Laurie"]

# Your code below: 
jake_votes = votes.count("Jake")
print(jake_votes)
```

<br>

## Sorting Lists I

Often, we will want to sort a list in either numerical (1, 2, 3, …) or alphabetical (a, b, c, …) order.

We can sort a list using the method .sort().

Suppose that we have a list of names:

```py
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
```

Let’s see what happens when we apply .sort():

```py
names.sort()
print(names)

# output:
['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
```

As we can see, the .sort() method sorted our list of names in alphabetical order.

.sort() also provides us the option to go in reverse. Instead of sorting in ascending order like we just saw, we can do so in descending order.

```py
names.sort(reverse=True)
print(names)

# output:
['Xander', 'Willow', 'Giles', 'Buffy', 'Angel']
```

Note: The .sort() method does not return any value and thus does not need to be assigned to a variable since it modifies the list directly. If we do assign the result of the method, it would assign the value of None to the variable.

To reverse a list using .sort(), add an optional input keyword argument and assign it the value of True.
list.sort(reverse=True)


Let’s experiment sorting various lists!

### Instructions

1.

Use .sort() to sort addresses.

2.

Use print() to see how addresses changed.

3.

Remove the # and whitespace in front of the line sort(names). Edit this line so that it runs without producing a NameError.

4.

Use print to examine sorted_cities. Why is it not the sorted version of cities?

5.

Edit the .sort() call on cities such that it sorts the cities in reverse order (descending).

Print cities to see the result.

```py
# Checkpoint 1 & 2
addresses = ["221 B Baker St.", "42 Wallaby Way", "12 Grimmauld Place", "742 Evergreen Terrace", "1600 Pennsylvania Ave", "10 Downing St."]


# Checkpoint 3
names = ["Ron", "Hermione", "Harry", "Albus", "Sirius"]
names.sort()


# Checkpoint 4 & 5
cities = ["London", "Paris", "Rome", "Los Angeles", "New York"]
sorted_cities = cities.sort(reverse=True)
print(sorted_cities)

addresses.sort()
print(addresses)
```


## Sorting Lists II

A second way of sorting a list in Python is to use the built-in function sorted().
In contrast to the method .sort(), the built-in function sorted() will not modify the original list. 

The sorted() function is different from the .sort() method in two ways:

    It comes before a list, instead of after as all built-in functions do.
    It generates a new list rather than modifying the one that already exists.

Let’s return to our list of names:

```py
names = ["Xander", "Buffy", "Angel", "Willow", "Giles"]
```

Using sorted(), we can create a new list, called sorted_names:

```py
sorted_names = sorted(names)
print(sorted_names)

# This yields the list sorted alphabetically:
['Angel', 'Buffy', 'Giles', 'Willow', 'Xander']
```

Note that using sorted did not change names:

```py
print(names)
#output:
['Xander', 'Buffy', 'Angel', 'Willow', 'Giles']
```

### Instructions

1.

Use sorted() to order games and create a new list called games_sorted.

2.

Print both games and games_sorted. How are they different?

```py
games = ["Portal", "Minecraft", "Pacman", "Tetris", "The Sims", "Pokemon"]

# Your code below:
games_sorted = sorted(games)

print(games)
print(games_sorted)
```

<br>

---

## Review

In this lesson, we learned how to:

- Add elements to a list by index using the .insert() method.
- Remove elements from a list by index using the .pop() method.
- Generate a list using the range() function.
- Get the length of a list using the len() function.
- Select portions of a list using slicing syntax.
- Count the number of times that an element appears in a list using the .count() method.
- Sort a list of items using either the .sort() method or sorted() function.


Since lists in Python of zero_indexed, the 5th element will be at index 4.
Use the .pop() method to remove elements from a list by index.


As you go through the exercises, feel free to use print() to see changes when not explicitly asked to do so.

### Instructions

1.

Our friend Jiho has been so successful in both the flower and grocery business that she has decided to open a furniture store.

Jiho has compiled a list of inventory items into a list called inventory and wants to know a few facts about it.

First, how many items are in the warehouse?

Save the answer to a variable called inventory_len.

2.

Select the first element in inventory. Save it to a variable called first.

3.

Select the last element from inventory. Save it to a variable called last.

4.

Select items from the inventory starting at index 2 and up to, but not including, index 6.

Save your answer to a variable called inventory_2_6.

5.

Select the first 3 items of inventory. Save it to a variable called first_3.

6.

How many 'twin bed's are in inventory? Save your answer to a variable called twin_beds.

7.

Remove the 5th element in the inventory. Save the value to a variable called removed_item.

8.

There was a new item added to our inventory called "19th Century Bed Frame".

Use the .insert() method to place the new item as the 11th element in our inventory.

9.

Sort inventory using the .sort() method or the sorted() function.

Print inventory to see the result.

```py
inventory = ["twin bed", "twin bed", "headboard", "queen bed", "king bed", "dresser", "dresser", "table", "table", "nightstand", "nightstand", "king bed", "king bed", "twin bed", "twin bed", "sheets", "sheets", "pillow", "pillow"]

inventory_len = len(inventory)
first = inventory[0]
last = inventory[-1]
inventory_2_6 = inventory[2:6]
first_3 = inventory[:3]
twin_beds = inventory.count('twin bed')
removed_item = inventory.pop(4)
inventory.insert(10, "19th Century Bed Frame")

inventory.sort()
# or this: sorted(inventory)
print(inventory)

```

<br>

---

## Tuples


https://www.youtube.com/watch?v=yDvRR8nWMNI&feature=emb_imp_woyt
