'''

Create a Python program that allows a
user to enter their name and some notes, then saves the notes to a file and displays them.
This task will help you practice input/output operations, variables, and file handling.

'''

name = input("Enter your name: ")
print("the naem you entered is: " , name)
notes = input("Write some notes: ")
print ("the notes you entered are: " , notes)

with open("file.txt" , "w") as file:
 file.write("Your name is: " + name + "\n")
 file.write("Notes: " + notes + "\n")

with open("file.txt" , "r") as file:
 print(file.read())
