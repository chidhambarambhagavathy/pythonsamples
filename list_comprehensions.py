my_list = [1, 2, 3, 4, 5]
an_equal_list = [x*3 for x in range(5)]

print (an_equal_list)

print ([n for n in range(10) if n % 2 == 0])

people_you_know = ["Rolf", " John", "anna", "GREP"]
normalized_people = [person.strip().lower() for person in people_you_know]

print (normalized_people)