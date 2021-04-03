print(2 ** 4)

print("Module:", 14 % 4)

cool_number = 12 + 30
cool_number * 5
print(cool_number)


print("========================")

print((5 * 2) - 1 == 8 + 1)
print(13 - 6 != (3 * 2) + 1)
print(3 * (2 - 1) == 4 - 1)

print((4 <= 2 * 3) and (7 + 1 == 8))

print("========================")

# x = 0
 
# if x == 0:
#   print("x is equal to zero.")
# elif x >= 0:
#   print("x is greater than zero.")
# else:
#   print("x is less than zero.")

print("========================")

print(4 * 5 <= 21 - 1)
print( 3 ** 2 + 1 != 30 / 3)
print((9 - 4) * 2 == 77 / 7 - 1)

print("========================")

x = 5
 
if x <= 2:
  print("This is printed")
if x <= 4:
  print("This is also printed")
if x <= 6:
  print("Is this printed?")
if x <= 8:
  print("This might be printed.")

print("========================")

friends = ["Annabelle", "Greg", "Katya", "Sol"]
friends.insert(-2, "Gus")
print(friends)

mylist = ["a", "b", "c", "d", "e"]
new_list = mylist[1:3]
print(new_list) # ["b", "c"]
print(mylist)


mylist2 = ["a", "b", "c", "d", "e", "f"]
print(mylist2[2:5])

print(mylist2[-3:])

olympic_sports = ["Hockey", "Swimming", "Fencing", "Vollyball", "Breakdancing"]
remove_breakdance = olympic_sports.pop()
print(remove_breakdance)

# list2(range(2, 14, 4)) # [2, 6, 10]
list2 = range(2, 14, 4)
print(list2)


print("loops ========================")

numbers = [2, 4, 6, 8]
for number in numbers:
  print("hello!")

drink_choices = ["coffee", "tea", "water", "juice", "soda"]
for drink in drink_choices:
  print(drink)


print([i-1 for i in range(5)])


for i in range(3):
    print(i)


my_list3 = [5, 10, -2, 8, 20]
desired_list = [10, 8, 20]

print([i for i in my_list3 if i > 5])

numbers = [1, 1, 2, 3]
for number in numbers:
  if number % 2 == 0:
    break
  print(number)

print("-----")

numbers2 = [1, 1, 2, 3]
for number in numbers2:
  if number % 2 == 0:
    continue
  print(number)


print("===============")


def tell_me_about_icecream(favorite_icecream):
    response = "My favorite icecream is" + favorite_icecream + "."
    print(response)
 
tell_me_about_icecream("chocolate")


def print_some_characters(word):
    for i in range(len(word)):
      if i % 2 == 0:
        print(word[i])
 
print_some_characters("watermelon")


least_favorite_fruit = "cantaloupe"
# print(least_favorite_fruit[5:-2])
print(least_favorite_fruit[5:8])


cool_fruit = "watermelon"
print(cool_fruit[len(cool_fruit) - 2])


good_fruit = "Raspberry"
print(good_fruit[3])


dirty_harry = "Go ahead, make my day."
split_hairs = dirty_harry.split("a")
print(split_hairs)


print("===============")

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
print(12 in inventory)


combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
print(combo_meals[2])


oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
 
for element in oscars:
  print(element)


oscars = {"Best Picture": "Moonlight", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
 
for element in oscars.values():
  print(element)



combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
#print(combo_meals[3])


raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
 
raffle.pop(561721, "No Value")
print(raffle)


combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
print(combo_meals.get(3, ["hamburger", "fries"]))


inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
print("the peacemaker" in inventory)


inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}
print(inventory.get("stone glove", 30))



print("===============")

def return_translated_point(x, y, change_x, change_y):
  return x + change_x, y + change_y
 
a, b = return_translated_point(1, 2, 5, 8)
print(b)


def unite_args(*args):
  new_string = ""
  for arg in args:
    new_string += arg
  return new_string
    
print(unite_args("I'm ", "here ", "for ", "this "))


# ------------------------------------------
# https://www.codecademy.com/profiles/Futurist4

