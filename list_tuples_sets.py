my_variable = "hello"

grades = [77, 80, 90, 95, 100]
tuple_grades = (77, 80, 90, 95, 100)
set_grades = {77, 80, 90, 95, 100, 100}

print ( sum(grades) / len(grades))
grades.append(200)

print(grades)

print(set_grades)

print ("Printing Tuples")
print(tuple_grades)
tuple_grades = tuple_grades + (100,)
print(tuple_grades)


print("Set Operations")

your_lottery_numbers = {1, 2, 3, 4, 5}
winning_numbers = {1, 3, 5, 7, 9, 11}

print (your_lottery_numbers.intersection(winning_numbers))
print (your_lottery_numbers.union(winning_numbers))
print (your_lottery_numbers.difference(winning_numbers))
