from sys import argv
# read the WYSS section for how to run this
script, first, second = argv

print("The script is called: ", script)
print("Your first variable is: ", first)
print("Your second variable is: ", second)
multiplay_by = int(input("enter number to multiply by: "))
print(f"first num{first} multiply by {multiplay_by}")
print(f" {int(first) * multiplay_by}")

