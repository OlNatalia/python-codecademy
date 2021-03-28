# Python dictionary

## Code Challenge

### Introduction

This lesson will help you review Python functions by providing some challenge exercises involving dictionaries.

As a refresher, function syntax looks like this:

```py
def some_function(some_input1, some_input2):
  … do something with the inputs …
  return output
```

For example, a function that counts the number of values in a dictionary that are above a given number would look like this:

```py
def greater_than_ten(my_dictionary, number):
  count = 0
  for value in my_dictionary.values():
    if value > number:
      count += 1
  return count
```

And this would produce output like:

```
>>> greater_than_ten({"a":1, "b":2, "c":3}, 0)
3
>>> greater_than_ten({"a":1, "b":2, "c":3}, 5)
0
```

<br>

---

### :page_facing_up: Instructions - Sum Values

1. Write a function named sum_values that takes a dictionary named my_dictionary as a parameter. The function should return the sum of the values of the dictionary

### :computer: Solution

```py
# Write your sum_values function here:
def sum_values(my_dictionary):
  sum = 0
  for value in my_dictionary.values():
    sum += value

  return sum

# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
# should print 10
#print(sum_values({10:1, 100:2, 1000:3}))
# should print 6
```

---

### :page_facing_up: Instructions - Even Keys

1. Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, as a parameter. This function should return the sum of the values of all even keys.

```
# Write your sum_even_keys function here:
def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key%2 == 0:
      total += my_dictionary[key]
  return total

# Uncomment these function calls to test your  function:
print(sum_even_keys({1:5, 2:2, 3:3}))
# should print 2
print(sum_even_keys({10:1, 100:2, 1000:3}))
# should print 6
```

---

### :page_facing_up: Instructions - Add Ten

1. Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. The function should add 10 to every value in my_dictionary and return my_dictionary

### :computer: Solution

```py
# Write your add_ten function here:
def add_ten(my_dictionary):
  for key in my_dictionary.keys():
    my_dictionary[key] += 10
  return my_dictionary

# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
# should print {1:15, 2:12, 3:13}
print(add_ten({10:1, 100:2, 1000:3}))
# should print {10:11, 100:12, 1000:13}
```

---

### :page_facing_up: Instructions - Values That Are Keys

1. Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. This function should return a list of all values in the dictionary that are also keys.

### :page_facing_up: :flashlight: Hint:

Loop through all values in the dictionary by using for value in my_dictionary.values(). Check to see if value is in my_dictionary.keys() and if so, append it to a list.

### :computer: Solution

```py
# Write your values_that_are_keys function here:
def values_that_are_keys(my_dictionary):
  list = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      list.append(value)
  return list

# Uncomment these function calls to test your  function:
print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
# should print [1, 4]
#print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
# should print ["a"]
```

---

### :page_facing_up: Instructions - Largest Value

1. Write a function named max_key that takes a dictionary named my_dictionary as a parameter. The function should return the key associated with the largest value in the dictionary.

### :flashlight: Hint:

Begin by creating two variables named largest_key and largest_value. Initialize largest_value to be the smallest number possible (you can use float("-inf"). Initialize largest_key to be an empty string.

Loop through all keys/value pair in the dictionary. Any time you find a value larger than what is currently stored in largest_value, replace largest_value with that new value. Similarly, replace largest_key with the key associated with the new largest value.

After looping through all key/value pairs, return largest_key.

### :computer: Solution

```py
# Write your max_key function here:
def max_key(my_dictionary):
  largest_key = float("-inf")
  largest_value = float("-inf")
  for key, value in my_dictionary.items():
    if value > largest_value:
      largest_value = value
      largest_key = key
  return largest_key

# Uncomment these function calls to test your  function:
print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
```

---

### :page_facing_up: Instructions - Word Length Dict

1. Write a function named word_length_dictionary that takes a list of strings named words as a parameter. The function should return a dictionary of key/value pairs where every key is a word in words and every value is the length of that word.

### :flashlight: Hint:

First create an empty dictionary named something like word_lengths. Loop through every word in words and add a new key using word_lengths[word] = len(word)

### :computer: Solution

```py
# Write your word_length_dictionary function here:
def word_length_dictionary (words):
  word_lengths = {}
  for word in words:
    word_lengths[word] = len(word)
  return word_lengths

# another possibility
def word_length_dictionary (words):
  word_lengths = {}
  return {word:len(word) for word in words}

# Uncomment these function calls to test your  function:
print(word_length_dictionary(["apple", "dog", "cat"]))
# should print {"apple":5, "dog": 3, "cat":3}
print(word_length_dictionary(["a", ""]))
# should print {"a": 1, "": 0}
```

---

### :page_facing_up: Instructions - Frequency Count

1. Write a function named frequency_dictionary that takes a list of elements named words as a parameter. The function should return a dictionary containing the frequency of each element in words.

### :flashlight: Hint:

First, create a new empty dictionary. Then, loop through every word in words. If word is not a key in the dictionary, make word a key with a value of 1. If word was already a key, increase the value associated with word by 1.

### :computer: Solution

```py
# Write your frequency_dictionary function here:
def frequency_dictionary(words):
  frequency_words = {}
  for word in words:
    if word not in frequency_words:
    	frequency_words[word] = 0
    frequency_words[word] += 1
  return frequency_words 

# Uncomment these function calls to test your  function:
print(frequency_dictionary(["apple", "apple", "cat", 1]))
# should print {"apple":2, "cat":1, 1:1}
#print(frequency_dictionary([0,0,0,0,0]))
# should print {0:5}
```

---

### :page_facing_up: Instructions - Unique Values

1. Create a function named unique_values that takes a dictionary named my_dictionary as a parameter. The function should return the number of unique values in the dictionary.

### :flashlight: Hint:

Begin by creating a new empty list named seen_values. Loop through all of the values of my_dictionary. For every value, check to see if that value is in seen_values. If it is, continue to the next value. If it is not, add it to seen_values. After looping through all values, return the length of seen_values.

### :computer: Solution

```py
# Write your unique_values function here:
def unique_values(my_dictionary):
  seen_values = []
  for value in my_dictionary.values():
    if value not in seen_values:
      seen_values.append(value)
  return len(seen_values)

# Uncomment these function calls to test your  function:
print(unique_values({0:3, 1:1, 4:1, 5:3}))
# should print 2
#print(unique_values({0:3, 1:3, 4:3, 5:3}))
# should print 1
```

---

### :page_facing_up: Instructions - Count First Letter

1. Create a function named count_first_letter that takes a dictionary named names as a parameter. names should be a dictionary where the key is a last name and the value is a list of first names. For example, the dictionary might look like this:

```
names = {"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}
```

The function should return a new dictionary where each key is the first letter of a last name, and the value is the number of people whose last name begins with that letter.

So in example above, the function would return:

```
{"S" : 4, "L": 3}
```

### :flashlight: Hint:

Begin by creating an empty dictionary named something like letters. Loop through the keys of names and access the first letter of each the key using key[0].

If that letter is not a key in letters, create a new key/value pair where the key is key[0] and the value is the length of names[key].

If that letter is a key in letters, simply add the length of names[key] to value associated with key[0] in letters.

### :computer: Solution

```py
# Write your count_first_letter function here:
def count_first_letter(names):
  letters = {}
  for key in names:
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters

# Uncomment these function calls to test your  function:
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 4, "L": 3}
#print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
# should print {"S": 7}
```
