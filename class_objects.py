lottery_player_dict = {
    'name' : 'Rolf',
    'numbers' : (5, 9, 12, 3, 1, 21)
}

class LotteryPlayer:
    def __init__(self):
        self.name = "Rolf"
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return (sum(self.numbers))

players = LotteryPlayer()

print (players)
print (players.name)
print (players.numbers)
print (players.total())


class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return (sum(self.marks) / len(self.marks))
 
    @classmethod #@staticmethod
    def go_to_school(cls):
        print("I am going to school")


anna = Student("Anna", "MIT")
anna.go_to_school()

Student.go_to_school()