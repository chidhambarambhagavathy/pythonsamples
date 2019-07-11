should_continue = True
if should_continue:
    print("Hello")

known_people = ["John", "Anna", "Mary"]
person = input("Enter the person you know: ")

if person in known_people:
    print ("Yes, you known this person")

if person not in known_people:
    print ("No, you dont known this person")



if person in known_people:
    print ("Yes, you known {}!".format(person))
else:
    print ("No, you dont known {}!".format(person))
