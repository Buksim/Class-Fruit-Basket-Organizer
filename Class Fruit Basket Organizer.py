import array as arr
# PART 1: Create two fruit baskets as sets
basket1 = {"apple", "banana", "cherry", "grape"}
basket2 = {"orange", "pear", "plum", "grape"}
print("Basket 1:", basket1)
print("Basket 2:", basket2)

# PART 2: Add a nw fruit to basket1
basket1.add("kiwi")
print("Basket 1 after adding kiwi:", basket1)

# PART 3: Find Fruits common to both baskets
common_fruits = basket1.intersection(basket2)
print("Common fruits in both baskets:", common_fruits)

# PART 4: Create and Arrau of Fruit Counts using the array module
fruit_counts = arr.array('i', [3, 5, 2, 4])
print("Fruit Counts Array:", fruit_counts)

# PART 5: Add new fruit counts to the array
fruit_counts.insert(0, 1)
fruit_counts.append(6)
print("Fruit Counts Array after adding new counts:", fruit_counts)

# PART 6: County how many times the number 4 appears in the array
count_of_4 = fruit_counts.count(4)
print("Number of times 4 appears:", count_of_4)

# PART 7: Reverse the order of the fruit counts array
fruit_counts.reverse()
print("Reversed Fruit Counts Array:",fruit_counts)

# PART 8: Print the Final Class Fruit Basket Organizer History
print("")
print("===== CLASS FRUIT BASKET  ORGANIZER =====")
print("Basket 1:", basket1)
print("Basket 2:", basket2)
print("Shared Fruits:", common_fruits)
print("Fruit Counts:", fruit_counts)
print("=====================================================")