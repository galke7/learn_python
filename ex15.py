# imorting argv module to get filename parameter befor the script run
from sys import argv
# unpack parameters from argv to variable
script, filename = argv
# open file and assign txt as its handler
txt = open(filename)
# read the file and printing it to the screen
print(f"Here's your file {filename}:")
print(txt.read())
txt.close()

print("Type the filename again:")

file_again = input("> ")
# open anather file from user input
txt_again = open(file_again)
# read the txt file and print it
print(txt_again.read())
txt_again.close()
