## loops

This lesson will help you review Python loops by providing some challenge exercises involving loops.

Some of these challenges are difficult! Take some time to think about them before starting to code.

You might not get the solution correct on your first try — look at your output, try to find where you’re going wrong, and iterate on your solution.

Finally, if you get stuck, use our solution code! If you “Check Answer” twice with an incorrect solution, you should see an option to get our solution code. However, truly investigate that solution — experiment and play with the solution code until you have a good grasp of how it is working. Good luck!
Function and Loop Syntax

As a refresher, function syntax looks like this:

```py
def some_function(some_input1, some_input2):
  … do something with the inputs …
  return output
```

For example, a function that prints all odd numbers in a list would look like this:

```py
def odd_nums(lst):
  for item in lst:
    if item % 2 == 1:
      print(item)
```

And this would produce output like:

    >>> odd_nums([4, 7, 9, 10, 13])
    7
    9
    13

<br>

## Challenges

We’ve included 5 challenges below. Try to answer all of them and polish up your problem-solving skills and your loop expertise.
1. Divisible By Ten

Let’s start our code challenges with a function that counts how many numbers are divisible by ten from a list of numbers. This function will accept a list of numbers as an input parameter and use a loop to check each of the numbers in the list. Every time a number is divisible by 10, a counter will be incremented and the final count will be returned. These are the steps we need to complete this:

    Define the function to accept one input parameter called nums
    Initialize a counter to 0
    Loop through every number in nums
    Within the loop, if any of the numbers are divisible by 10, increment our counter
    Return the final counter value

Create a function named divisible_by_ten() that takes a list of numbers named nums as a parameter.

Return the count of how many numbers in the list are divisible by 10.

```py
#Write your function here

#Uncomment the line below when your function is done
#print(divisible_by_ten([20, 25, 30, 35, 40]))
```

Let’s see how we solved it:

```py
def divisible_by_ten(nums):
  count = 0
  for number in nums:
    if (number % 10 == 0):
      count += 1
  return count
```

In this solution, we defined the function and set up our counter. We use a for loop to iterate through each number and check if its divisible by ten. If a number is divisible by another number then the remainder should be zero, so we use modulus. After the loop has finished, we return our count.


<br>

### Greetings

You are invited to a social gathering, but you are tired of greeting everyone there. Luckily we can create a function to accomplish this task for us. In this challenge, we will take a list of names and prepend the string 'Hello, ' before each name. This will require a few steps:

    Define the function to accept a list of strings as a single parameter called names
    Create a new list of strings
    Loop through each name in names
    Within the loop, concatenate 'Hello, ' and the current name together and append this new string to the new list of strings
    Afterwards, return the new list of strings

Create a function named add_greetings() which takes a list of strings named names as a parameter.

In the function, create an empty list that will contain each greeting. Add the string 'Hello, ' in front of each name in names and append the greeting to the list.

Return the new list containing the greetings.

```py
#Write your function here

#Uncomment the line below when your function is done
#print(add_greetings(["Owen", "Max", "Sophie"]))
```

This is one way to solve it:

```py
def add_greetings(names):
  new_list = []
  for name in names:
    new_list.append("Hello, " + name)
  return new_list
```

First, we set up our function to accept the list of strings and we initialized a new list of strings to hold our greetings. We iterate through each name and we append and concatenate the strings at the same time within our loop. Finally, we return the list containing all of our eloquent greetings.

<br>

### Delete Starting Even Numbers

Let’s try a tricky challenge involving removing elements from a list. This function will repeatedly remove the first element of a list until it finds an odd number or runs out of elements. It will accept a list of numbers as an input parameter and return the modified list where any even numbers at the beginning of the list are removed. To do this, we will need the following steps:

    Define our function to accept a single input parameter lst which is a list of numbers
    Loop through every number in the list if there are still numbers in the list and if we haven’t hit an odd number yet
    Within the loop, if the first number in the list is even, then remove the first number of the list
    Once we hit an odd number or we run out of numbers, return the modified list

Write a function called delete_starting_evens() that has a parameter named lst.

The function should remove elements from the front of lst until the front of the list is not even. The function should then return lst.

For example if lst started as [4, 8, 10, 11, 12, 15], then delete_starting_evens(lst) should return [11, 12, 15].

Make sure your function works even if every element in the list is even!

```py
#Write your function here

#Uncomment the lines below when your function is done
#print(delete_starting_evens([4, 8, 10, 11, 12, 15]))
#print(delete_starting_evens([4, 8, 10]))
```

This is the way we solved it:

```py
def delete_starting_evens(lst):
  while (len(lst) > 0 and lst[0] % 2 == 0):
    lst = lst[1:]
  return lst
```

After defining our method, we use a while loop to keep iterating as long as some provided conditions are true. We provide two conditions for the while loop to continue. We will keep iterating as long as there is at least one number left in the list len(lst) > 0 and if the first element in the list is even lst[0] % 2 == 0. If both of these conditions are true, then we replace the list with every element except for the first one using lst[1:]. Once the list is empty or we hit an odd number, the while loop terminates and we return the modified list.

<br>

###  Odd Indices

This next function will give us the values from a list at every odd index. We will need to accept a list of numbers as an input parameter and loop through the odd indices instead of the elements. Here are the steps needed:

    Define the function header to accept one input which will be our list of numbers
    Create a new list which will hold our values to return
    Iterate through every odd index until the end of the list
    Within the loop, get the element at the current odd index and append it to our new list
    Return the list of elements which we got from the odd indices.

Create a function named odd_indices() that has one parameter named lst.

The function should create a new empty list and add every element from lst that has an odd index. The function should then return this new list.

For example, odd_indices([4, 3, 7, 10, 11, -2]) should return the list [3, 10, -2].

```py
#Write your function here

#Uncomment the line below when your function is done
#print(odd_indices([4, 3, 7, 10, 11, -2]))
```

Here is this solution:

```py
def odd_indices(lst):
  new_lst = []
  for index in range(1, len(lst), 2):
    new_lst.append(lst[index])
  return new_lst
```

In our solution, we iterate through a range of values. The function range(1, len(lst), 2) returns a list of numbers starting at 1, ending at the length of len, and incrementing by 2. This causes the loop to iterate through every odd number until the last index of our list of numbers. Using this, we can simply append the element at whatever index we are at since we know that using our range we will be iterating through only odd indices.

Another way to do this would be to iterate through all indices and use an if statement to see if the index you’re currently looking at is odd.

<br>

### Exponents

In this challenge, we will be using nested loops in order to raise a list of number to the power of a list of other numbers. What this means is that for every number in the first list, we will raise that number to the power of every number in the second list. If you provide the first list with 2 elements and the second list with 3 numbers, then there will be 6 final answers. Let’s look at the steps we need:

    Define the function to accept two lists of numbers, bases and powers
    Create a new list that will contain our answers
    Create a loop that iterates through every base in bases
    Within that loop, create another loop that iterates through every power in power
    Within that nested loop, append the result of the current base raised to the current power.
    After all iterations of both loops are complete, return the list of answers

Create a function named exponents() that takes two lists as parameters named bases and powers. Return a new list containing every number in bases raised to every number in powers.

For example, consider the following code.

```py
exponents([2, 3, 4], [1, 2, 3])
```

the result would be the list [2, 4, 8, 3, 9, 27, 4, 16, 64]. It would first add two to the first. Then two to the second. Then two to the third, and so on.

```py
#Write your function here

#Uncomment the line below when your function is done
#print(exponents([2, 3, 4], [1, 2, 3]))
```

Here is how we solved this one:

```py
def exponents(bases, powers):
  new_lst = []
  for base in bases:
    for power in powers:
      new_lst.append(base ** power)
  return new_lst
```

As you can see in this solution, we used two nested for loops so that, for every base, we iterate through every power. This allows us to raise each base to every single power in our list and append the answers to our new list. Finally, we return the list of answers.


<br>

---

## Loops Advanced

We’ve included 5 challenges below. Try to answer all of them and polish up your problem-solving skills and your loop expertise.

### Larger Sum

We are going to start our advanced challenge problems by calculating which list of two inputs has the larger sum. We will iterate through each of the list and calculate the sums, afterwards we will compare the two and return which one has a greater sum. Here are the steps we need:

    Define the function to accept two input parameters: lst1 and lst2
    Create two variables to record the two sums
    Loop through the first list and add up all of the numbers
    Loop through the second list and add up all of the numbers
    Compare the first and second sum and return the list with the greater sum

Create a function named larger_sum() that takes two lists of numbers as parameters named lst1 and lst2.

The function should return the list whose elements sum to the greater number. If the sum of the elements of each list are equal, return lst1.

```py
#Write your function here

#Uncomment the line below when your function is done
#print(larger_sum([1, 9, 5], [2, 3, 7]))
```

Here’s one way to do it:

```py
def larger_sum(lst1, lst2):
  sum1 = 0
  sum2 = 0
  for number in lst1:
    sum1 += number
  for number in lst2:
    sum2 += number
  if sum1 >= sum2:
    return lst1
  else: 
    return lst2
```

In this solution, we manually iterate through each element in each list and calculate our sums. We then return the list with the greater sum and break the tie by returning lst1. You can also try solving this problem using the sum() function in python. The body of this function could also be condensed into one line of code if you want an additional challenge!

<br>


### Over 9000

We are constructing a device that is able to measure the power level of our coding abilities and according to the device, it will be impossible for our power levels to be over 9000. Because of this, as we iterate through a list of power values we will count up each of the numbers until our sum reaches a value greater than 9000. Once this happens, we should stop adding the numbers and return the value where we stopped. In order to do this, we will need the following steps:

    Define the function to accept a list of numbers
    Create a variable to keep track of our sum
    Iterate through every element in our list of numbers
    Within the loop, add the current number we are looking at to our sum
    Still within the loop, check if the sum is greater than 9000. If it is, end the loop
    Return the value of the sum when we ended our loop

Create a function named over_nine_thousand() that takes a list of numbers named lst as a parameter.

The function should sum the elements of the list until the sum is greater than 9000. When this happens, the function should return the sum. If the sum of all of the elements is never greater than 9000, the function should return total sum of all the elements. If the list is empty, the function should return 0.

For example, if lst was [8000, 900, 120, 5000], then the function should return 9020.

```py
#Write your function here

#Uncomment the line below when your function is done
#print(over_nine_thousand([8000, 900, 120, 5000]))
```

Here is this solution:

```py
def over_nine_thousand(lst):
  sum = 0
  for number in lst:
    sum += number
    if (sum > 9000):
      break
  return sum
```

Our solution follows a similar pattern to some of the other code challenges, except that we have a condition where we end early. In the case where we reach a sum greater than 9000, we can use the break keyword to exit our loop. This will continue to execute the code outside of our loop, which in this case, returns the sum that we found.


<br>

### Max Num

Here is a more traditional coding problem for you. This function will be used to find the maximum number in a list of numbers. This can be accomplished using the max() function in python, but as a challenge, we are going to manually implement this function. Here is what we need to do:

    Define the function to accept a list of numbers called nums
    Set our default maximum value to be the first element in the list
    Loop through every number in the list of numbers
    Within the loop, if we find a number greater than our starting maximum, then replace the maximum with what we found.
    Return the maximum number

Create a function named max_num() that takes a list of numbers named nums as a parameter.

The function should return the largest number in nums

```py
#Write your function here

#Uncomment the line below when your function is done
#print(max_num([50, -10, 0, 75, 20]))
```

Here is one way to solve this:

```py
def max_num(nums):
  maximum = nums[0]
  for number in nums:
    if number > maximum:
      maximum = number
  return maximum
```

There are a few different ways to accomplish this task, but the way we did it was to check every element in the list and see if there is one bigger than what we currently think is the biggest. If there is a bigger one, then replace it. We keep replacing the number until the largest number has been found.


<br>


### Same Values

In this challenge, we need to find the indices in two equally sized lists where the numbers match. We will be iterating through both of them at the same time and comparing the values, if the numbers are equal, then we record the index. These are the steps we need to accomplish this:

    Define our function to accept two lists of numbers
    Create a new list to store our matching indices
    Loop through each index to the end of either of our lists
    Within the loop, check if our first list at the current index is equal to the second list at the current index. If so, append the index where they matched
    Return our list of indices

Write a function named same_values() that takes two lists of numbers of equal size as parameters.

The function should return a list of the indices where the values were equal in lst1 and lst2.

For example, the following code should return [0, 2, 3]

```py
same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5])

#Write your function here

#Uncomment the line below when your function is done
#print(same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))
```

Here’s how we did it:

```py
def same_values(lst1, lst2):
  new_lst = []
  for index in range(len(lst1)):
    if lst1[index] == lst2[index]:
      new_lst.append(index)
  return new_lst
```

In this solution, we used a loop that iterates using the range of the len of our list. This generates the indices we need to iterate through. Note that we assume the lists are of equal size. We then access the element at the current index from each list using lst1[index] and lst2[index]. If they are equal we add the index to the new list. Finally, we return the results. 

<br>

### Reversed List

For the final challenge, we are going to test two lists to see if the second list is the reverse of the first list. There are a few different ways to approach this, but we are going to try a method that iterates through each of the values in one direction for the first list and compares them against the values starting from the other direction in the second list. Here is what you need to do:

    Define a function that has two input parameters for our lists
    Loop through every index in one of the lists from beginning to end
    Within the loop, compare the element in the first list at the current index against the element at the second list’s last index minus the current index. If there was a mismatch, then the lists aren’t reversed and we can return False
    If the loop ended successfully, then we know the lists are reversed and we can return True.

Create a function named reversed_list() that takes two lists of the same size as parameters named lst1 and lst2.

The function should return True if lst1 is the same as lst2 reversed. The function should return False otherwise.

For example, reversed_list([1, 2, 3], [3, 2, 1]) should return True.

### Hint

Let's say the lists are of size 5. You want to compare lst1[0] with lst2[4], lst1[1] with lst2[3] and so on.

Loop through the numbers created by range(len(lst1)) using a variable named index

Compare lst1[index] to lst2[len(lst2) - 1 - index]. If those two items are not equal, return False. If you loop through the entire list and you never return False, that means that every item was equal, and you should return True.

```py
#Write your function here

#Uncomment the lines below when your function is done
#print(reversed_list([1, 2, 3], [3, 2, 1]))
#print(reversed_list([1, 5, 3], [3, 2, 1]))
```

Here is one way to do it:

```py
def reversed_list(lst1, lst2):
  for index in range(len(lst1)):
    if lst1[index] != lst2[len(lst2) - 1 - index]:
      return False
  return True
```

In this code, we iterate through each of the indices for the entire length of either of the lists (since we assume the lengths are equal) and we perform a comparison on each of the elements. We get the element at the current index from our first list with lst1[index] and we test it against the last index of the second list minus the current index len(lst2) - 1 – index.

That math is a little complicated — it helps to look at a concrete example. If we are given a list of 5 elements, the valid indices are 0 to 4. Because of this, the last index in the second list is len(lst2) - 1, or 5 - 1 = 4. Now in order to get the inverse of the position we are at in the first list, we subtract the index we are at from the end of the second list. So on the first pass, we’ll compare the element at position 0 to the element at position 5 - 1 - 0 = 4. On the next pass, we’ll compare the element at position 1 to the element at position 5 - 1 - 1 = 3, and so on.

If any of the two elements are not equal then we know that the second list is not the reverse of the first list and we return False. If we made it to the end without a mismatch then we can return True since the second list is the reverse of the first. You could also try simplifying this code by using the python function reversed() or other methods that you will learn later on such as ‘slicing’.
