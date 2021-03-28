# Python dictionary


## Creating Dictionaries

A dictionary is an unordered set of key: value pairs.

It provides us with a way to map pieces of data to each other so that we can quickly find values that are associated with one another.

Suppose we want to store the prices of various items sold at a cafe:

    Avocado Toast is 6 dollars
    Carrot Juice is 5 dollars
    Blueberry Muffin is 2 dollars

In Python, we can create a dictionary called menu to store this data:

```py
menu = {"avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
```

:memo: Notice that:

    A dictionary begins and ends with curly braces { and }.
    Each item consists of a key ("avocado toast") and a value (6).
    Each key: value pair is separated by a comma.

It’s considered good practice to insert a space () after each comma, but our code will still run without the space.

Instructions

1.

Suppose we have a dictionary of temperature sensors in the house and what temperatures they read. We’ve just added a sensor to the "pantry", and it reads 22 degrees.

Add this pair to the dictionary on line 1.

2.

Remove the # in front of the definition of the dictionary num_cameras, which represents the number of cameras in each area around the house.

If you run this code, you’ll get an error:

```
SyntaxError: invalid syntax
```

Try to find and fix the syntax error to make this code run.

### Hint:

Add commas (,) to num_cameras so that it runs without errors.

```py
sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)
```

---

## Make a Dictionary

In the previous exercise, we saw a dictionary that maps strings to numbers (i.e., "avocado toast": 6). However, the keys can be numbers as well.

For example, if we were mapping restaurant bill subtotals to the bill total after tip, a dictionary could look like:

```
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}
```

Values can be of any type. We can use a string, a number, a list, or even another dictionary as the value associated with a key!

For example:

```py
students_in_classes = {"software design": ["Aaron", "Delila", "Samson"], "cartography": ["Christopher", "Juan", "Marco"], "philosophy": ["Frederica", "Manuel"]}

The list ["Aaron", "Delila", "Samson"], which is the value for the key "software design", represents the students in that class.
```

We can also mix and match key and value types. For example:

person = {"name": "Shuri", "age": 18, "family": ["T'Chaka", "Ramonda"]}

Instructions

1.

Create a dictionary called translations that maps the following words in English to their definitions in Sindarin (the language of the elves):

English 	Sindarin
mountain 	orod
bread 	bass
friend 	mellon
horse 	roch

```py
translations = {
  "mountain": "orod", 
  "bread": "bass", 
  "friend": "mellon", 
  "horse": "roch"
}
```

Here are some helpful links to the top questions asked by coders about this exercise:

    Does a dictionary have to be created with initial values?

---

## Invalid Keys

We can have a list or a dictionary as a value of an item in a dictionary, but we cannot use these data types as keys of the dictionary. If we try to, we will get a TypeError.

For example:

```py
powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}
```

This code will yield:

```
TypeError: unhashable type: 'list'
```

The word “unhashable” in this context means that this ‘list’ is an object that can be changed.

Dictionaries in Python rely on each key having a hash value, a specific identifier for the key. If the key can change, that hash value would not be reliable. So the keys must always be unchangeable, hashable data types, like numbers or strings.

Instructions

1.

Run the code inside script.py. You should get an error:

TypeError: unhashable type

Make the code run without errors by flipping the items in the dictionary so that the strings are the keys and the lists are the values

children = {"von Trapp":["Johannes", "Rosmarie", "Eleonore"], "Corleone":["Sonny", "Fredo", "Michael"]}


---

## Empty Dictionary

A dictionary doesn’t have to contain anything. Sometimes we need to create an empty dictionary when we plan to fill it later based on some other input.

We can create an empty dictionary like this:

```py
empty_dict = {}
```

We will explore ways to fill a dictionary in the next exercise.

Instructions

1.

Create an empty dictionary called my_empty_dictionary.

my_empty_dictionary = {}


---

## Add A Key

To add a single key: value pair to a dictionary, we can use the syntax:

```py
dictionary[key] = value
```

For example, if we had our menu dictionary from the first exercise:

```py
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
```

And we wanted to add a new item, "cheesecake" for 8 dollars, we could use:

```py
menu["cheesecake"] = 8
```

Now, menu looks like:

```py
{"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2, "cheesecake": 8}
```

Instructions

1.

Create an empty dictionary called animals_in_zoo.

2.

Walking around the zoo, you see 8 zebras. Add "zebras" to animals_in_zoo as a key with a value of 8.

3.

The primate house was bananas! Add "monkeys" to animals_in_zoo as a key with a value of 12.

4.

As you leave the zoo, you are saddened that you did not see any dinosaurs. Add "dinosaurs" to animals_in_zoo as a key with a value of 0.

5.

Print animals_in_zoo.

```py
animals_in_zoo = {"zebras":8, "monkeys":12}
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)
```

---

## Add Multiple Keys

If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.

Looking at our sensors object from a previous exercise:

```py
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
```

If we wanted to add 3 new rooms, we could use:

```py
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
```

This would add all three items to the sensors dictionary.

Now, sensors looks like:

```py
{"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}
```

Instructions

1.

In one line of code, add two new users to the user_ids dictionary:

    theLooper, with an id of 138475
    stringQueen, with an id of 85739

2.

Print user_ids.

hint:
Add Multiple Keys

If we wanted to add multiple key : value pairs to a dictionary at once, we can use the .update() method.

Looking at our sensors object from a previous exercise:

```py
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
```

If we wanted to add 3 new rooms, we could use:

```py
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
```

This would add all three items to the sensors dictionary.

Now, sensors looks like:

```py
{"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22, "guest room": 25, "patio": 34}
```

Instructions

1.
In one line of code, add two new users to the user_ids dictionary:

    theLooper, with an id of 138475
    stringQueen, with an id of 85739

2.

Print user_ids.

```py
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}

user_ids.update({"theLooper":138475, "stringQueen":85739})
print(user_ids)
```

---

## Overwrite Values

We know that we can add a key by using syntax like:

```py
menu["avocado toast"] = 7
```

This will create a key "avocado toast" and set the value to 7. But what if we already have an 'avocado toast' entry in the menu dictionary?

In that case, our value assignment would overwrite the existing value attached to the key 'avocado toast'.

```py
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
menu["oatmeal"] = 5
print(menu)
```

This would yield:

```
{"oatmeal": 5, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
```

Notice the value of "oatmeal" has now changed to 5.

Instructions

1.

Add the key "Supporting Actress" and set the value to "Viola Davis".

2.

Without changing the definition of the dictionary oscar_winners, change the value associated with the key "Best Picture" to "Moonlight".

```py
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"
```

---

## List Comprehensions to Dictionaries

Let’s say we have two lists that we want to combine into a dictionary, like a list of students and a list of their heights, in inches:

```py
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
```

Python allows you to create a dictionary using a list comprehension, with this syntax:

```py
students = {key:value for key, value in zip(names, heights)}
#students is now {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
```

Remember that zip() combines two lists into a zipped list of pairs. This list comprehension:

    Takes a pair from the zipped list of pairs from names and heights
    Names the elements in the pair key (the one originally from the names list) and value (the one originally from the heights list)
    Creates a key : value item in the students dictionary
    Repeats steps 1-3 for the entire list of pairs

Instructions

1.

You have two lists, representing some drinks sold at a coffee shop and the milligrams of caffeine in each. First, create a variable called zipped_drinks that is a zipped list of pairs between the drinks list and the caffeine list.

2.

Create a dictionary called drinks_to_caffeine by using a list comprehension that goes through the zipped_drinks list and turns each pair into a key:value item.

```py
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)

drinks_to_caffeine = {key:value for key, value in zipped_drinks }
```

---

## Review

So far we have learned:

    How to create a dictionary
    How to add elements to a dictionary
    How to update elements in a dictionary
    How to use a list comprehension to create a dictionary from two lists

Let’s practice these skills!

Instructions

1.

We are building a music streaming service. We have provided two lists, representing songs in a user’s library and the amount of times each song has been played.

Using a list comprehension, create a dictionary called plays that goes through zip(songs, playcounts) and creates a song:playcount pair for each song in songs and each playcount in playcounts.

2.

Print plays.

3.

After printing plays, add a new entry to it. The entry should be for the song "Purple Haze" and the playcount is 1.

4.

This user has caught Aretha Franklin fever and listened to “Respect” 5 more times. Update the value for "Respect" to be 94 in the plays dictionary.

5.

Create a dictionary called library that has two key: value pairs:

    key "The Best Songs" with a value of plays, the dictionary you created
    key "Sunday Feelings" with a value of an empty dictionary

6.

Print library.

```py
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
plays["Purple Haze"] = 1
plays.update({"Respect": 94})

library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
```
---

## Using Dictionaries

Now that we know how to create a dictionary, we can start using already created dictionaries to solve problems.

In this lesson, you’ll learn how to:

    Use a key to get a value from a dictionary
    Check for existence of keys
    Find the length of a dictionary
    Iterate through keys and values in dictionaries


## Get A Key

Once you have a dictionary, you can access the values in it by providing the key. For example, let’s imagine we have a dictionary that maps buildings to their heights, in meters:

```py
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}

# Then we can access the data in it like this:

>>> building_heights["Burj Khalifa"]
828
>>> building_heights["Ping An"]
599
```

Instructions

1.

We have provided a dictionary that maps the elements of astrology to the zodiac signs. Print out the list of zodiac signs associated with the "earth" element.

2.

Print out the list of the "fire" signs.

```py
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])
print(zodiac_elements["fire"])
```


## Get an Invalid Key

Let’s say we have our dictionary of building heights from the last exercise:

```py
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
```

What if we wanted to know the height of the Landmark 81 in Ho Chi Minh City?    
We could try:

```py
print(building_heights["Landmark 81"])
```

But "Landmark 81" does not exist as a key in the building_heights dictionary! So this will throw a KeyError:

```
KeyError: 'Landmark 81'
```

One way to avoid this error is to first check if the key exists in the dictionary:

key_to_check = "Landmark 81"
 
if key_to_check in building_heights:
  print(building_heights["Landmark 81"])

This will not throw an error, because key_to_check in building_heights will return False, and so we never try to access the key.

Instructions

1.

Run the code. It should throw a KeyError! "energy" does not exist as one of the elements.

2.

Add the key "energy" to the zodiac_elements. It should map to a value of "Not a Zodiac element". Run the code. Did this resolve the KeyError?

```py
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

zodiac_elements["energy"] = "Not a Zodiac element"

print(zodiac_elements["energy"])
```


## Try/Except to Get a Key

We saw that we can avoid KeyErrors by checking if a key is in a dictionary first. Another method we could use is a try/except:

```py
key_to_check = "Landmark 81"
try:
  print(building_heights[key_to_check])
except KeyError:
  print("That key doesn't exist!")
``` 

When we try to access a key that doesn’t exist, the program will go into the except block and print "That key doesn't exist!".

Instructions

1.

Use a try block to try to print the caffeine level of "matcha". If there is a KeyError, print "Unknown Caffeine Level".

2.

Above the try block, add "matcha" to the dictionary with a value of 30.

```py
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}

caffeine_level["matcha"] = 30

check_key = "matcha"
try:
  print(caffeine_level[check_key])
except KeyError:
  print("Unknown Caffeine Level")
```


---

## Safely Get a Key

We saw in the last exercise that we had to add a key:value pair to a dictionary in order to avoid a KeyError. This solution is not sustainable. We can’t predict every key a user may call and add all of those placeholder values to our dictionary!

Dictionaries have a .get() method to search for a value instead of the my_dict[key] notation we have been using. If the key you are trying to .get() does not exist, it will return None by default:

```py
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
 
#this line will return 632:
building_heights.get("Shanghai Tower")
 
#this line will return None:
building_heights.get("My House")
```

You can also specify a value to return if the key doesn’t exist. For example, we might want to return a building height of 0 if our desired building is not in the dictionary:

```
>>> building_heights.get('Shanghai Tower', 0)
632
>>> building_heights.get('Mt Olympus', 0)
0
>>> building_heights.get('Kilimanjaro', 'No Value')
'No Value'
```

Instructions

1.

Use .get() to get the value of "teraCoder"‘s user ID, with 100000 as a default value if the user doesn’t exist. Store it in a variable called tc_id. Print tc_id to the console.

2.

Use .get() to get the value of "superStackSmash"‘s user ID, with 100000 as a default value if the user doesn’t exist. Store it in a variable called stack_id. Print stack_id to the console.

```py
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
stack_id = user_ids.get("superStackSmash", 100000)
```

---

## Delete a Key

Sometimes we want to get a key and remove it from the dictionary. Imagine we were running a raffle, and we have this dictionary mapping ticket numbers to prizes:

```py
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
```

When we get a ticket number, we want to return the prize and also remove that pair from the dictionary, since the prize has been given away. We can use .pop() to do this. Just like with .get(), we can provide a default value to return if the key does not exist in the dictionary:

```
>>> raffle.pop(320291, "No Prize")
"Gift Basket"
>>> raffle
{223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
>>> raffle.pop(100000, "No Prize")
"No Prize"
>>> raffle
{223842: "Teddy Bear", 872921: "Concert Tickets", 412123: "Necklace", 298787: "Pasta Maker"}
>>> raffle.pop(872921, "No Prize")
"Concert Tickets"
>>> raffle
{223842: "Teddy Bear", 412123: "Necklace", 298787: "Pasta Maker"}
```

.pop() works to delete items from a dictionary, when you know the key value.

Instructions

1.

You are designing the video game Big Rock Adventure. We have provided a dictionary of items that are in the player’s inventory which add points to their health meter. In one line, add the corresponding value of the key "stamina grains" to the health_points variable and remove the item "stamina grains" from the dictionary. If the key does not exist, add 0 to health_points.

2.

In one line, add the value of "power stew" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.

3.

In one line, add the value of "mystic bread" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.

4.

Print available_items and health_points.

```py
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)
print(health_points)
```

---

## Get All Keys

Sometimes we want to operate on all of the keys in a dictionary. For example, if we have a dictionary of students in a math class and their grades:

```py
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
```

We want to get a roster of the students in the class, without including their grades. We can do this with the built-in list() function:

```
>>> list(test_scores)
["Grace", "Jeffrey", "Sylvia", "Pedro", "Martin", "Dina"]
```

Dictionaries also have a .keys() method that returns a dict_keys object. A dict_keys object is a view object, which provides a look at the current state of the dictionary, without the user being able to modify anything. The dict_keys object returned by .keys() is a set of the keys in the dictionary. You cannot add or remove elements from a dict_keys object, but it can be used in the place of a list for iteration:

for student in test_scores.keys():
  print(student)

will yield:
```
"Grace"
"Jeffrey"
"Sylvia"
"Pedro"
"Martin"
"Dina"
```

Instructions

1.

Create a variable called users and assign it to be a dict_keys object of all of the keys of the user_ids dictionary.

2.

Create a variable called lessons and assign it to be a dict_keys object of all of the keys of the num_exercises dictionary.

3.

Print users to the console.

4.

Print lessons to the console.

```py
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)
```

---

## Get All Values

Dictionaries have a .values() method that returns a dict_values object (just like a dict_keys object but for values!) with all of the values in the dictionary. It can be used in the place of a list for iteration:

```py
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
 
for score_list in test_scores.values():
  print(score_list)
```

will yield:

```
[80, 72, 90]
[88, 68, 81]
[80, 82, 84]
[98, 96, 95]
[78, 80, 78]
[64, 60, 75]
```

There is no built-in function to get all of the values as a list, but if you really want to, you can use:

```py
list(test_scores.values())
```

However, for most purposes, the dict_list object will act the way you want a list to act.

Instructions

1.

Create a variable called total_exercises and set it equal to 0.

2.

Iterate through the values in the num_exercises list and add each value to the total_exercises variable.

3.

Print the total_exercises variable to the console.

```py
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0

for num in num_exercises.values():
  total_exercises += num

print(total_exercises)
```


## Get All Items

You can get both the keys and the values with the .items() method. Like .keys() and .values(), it returns a dict_list object. Each element of the dict_list returned by .items() is a tuple consisting of:

(key, value)

so to iterate through, you can use this syntax:

```py
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
 
for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")

which would yield this output:

Apple has a value of 184 billion dollars.
Google has a value of 141.7 billion dollars.
Microsoft has a value of 80 billion dollars.
Coca-Cola has a value of 69.7 billion dollars.
Amazon has a value of 64.8 billion dollars.
```

Instructions

1.

Use a for loop to iterate through the items of pct_women_in_occupation. For each key : value pair, print out a string that looks like:

Women make up [value] percent of [key]s.

```py
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, percentage in pct_women_in_occupation.items():
  print("Women make up " + str(percentage) + " percent of " + occupation + "s.") 
```

---

## Review

In this lesson, you’ve learned how to go through dictionaries and access keys and values in different ways. Specifically you have seen how to:

    Use a key to get a value from a dictionary
    Check for existence of keys
    Find the length of a dictionary
    Remove a key: value pair from a dictionary
    Iterate through keys and values in dictionaries

Instructions

1.

We have provided a pack of tarot cards, tarot. You are going to do a three card spread of your past, present, and future.

Create an empty dictionary called spread.

2.

The first card you draw is card 13. Pop the value assigned to the key 13 out of the tarot dictionary and assign it as the value of the "past" key of spread.

3.

The second card you draw is card 22. Pop the value assigned to the key 22 out of the tarot dictionary and assign it as the value of the "present" key of spread.

4.

The third card you draw is card 10. Pop the value assigned to the key 10 out of the tarot dictionary and assign it as the value of the "future" key of spread.

5.

Iterate through the items in the spread dictionary and for each key: value pair, print out a string that says:

Your {key} is the {value} card.

6.

Congratulations! You have learned about how to modify and use dictionaries.

```py
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print("Your "+key+" is the "+value+" card. ")
```
