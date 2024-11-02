# Match case in Python


mood = "hungry"

match mood:
    case "hungry":
        print("Get some food")
    case "thirsty":
        print("Get some water")
    case "tired":
        print("Get some sleep")
    case _:
        print("Any other mood")


# Exercise

"""
create variable with an integer between 1 and 5, call it grade
create a math case statement that writes 'ver good' when grade is 1
and very bad when the grade is 5 (and all other cases in between)
there should also be some default behavior if you get an unexpected value

"""

grade = int(input("Enter only from 1 to 5 of your grade: "))

match grade:
    case 1:
        print("Very Good")
    case 2:
        print("Still good")
    case 3:
        print("OKAY")
    case 4:
        print("needs improvement")
    case 5:
        print("very bad")
    case _:
        print("Invalid input")
