from sys import argv
# read the WYSS section for how to run this
script, first, second, third, fourth = argv

print("The script is called: ", script)
print("My first variable is: ", first)
print("My second variable is: ", second)
print("My third variable is: ", third)
print("My last var for Now is.. ", fourth)

multiplay_by = int(input("enter number to multiply by: "))
print(f"first num {first} multiply by {multiplay_by}:")
print(int(first) * multiplay_by)
raise_by = int(input("enter number to raise by: "))
print(f"fourth num {fourth} raise to the power of {raise_by}:\n{int(fourth) ** raise_by}")

