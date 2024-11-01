fruits = {"apples", "banana", "blueberry", "mango", "guava", "papaya"}
print(fruits)
print(len(fruits))


# making a set constructor with set()

jobs = set(("UI/UX", "Developer", "Tester", "Engineer", "Animator"))
print(jobs)
print(len(jobs))


# Accessing set items

print("Magician" in jobs)
print("Strawberry" not in fruits)


# Removing set items

fruits.discard("papaya")
jobs.discard("Tester")

print(fruits)
print(jobs)

# clearing a set

a = {"a", "b", "c", "d", "e"}
print(a)
a.clear()
print(a)
