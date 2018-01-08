#pypractice.py
import sys
print(sys.executable)
print(sys.version)

age = "20"
food = "cheese"

print("Who are you?")
name = input()

print ("So you must be %s, %s years old. I think you like %s" % (name, age, food))
