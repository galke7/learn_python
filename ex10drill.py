tabby_cat = "\tI'm tabbed in."
parsian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(f"this is a tabby cat(with fstring):\n{tabby_cat}\n\t*** and this is my parsian cat: {parsian_cat}")
print(backslash_cat)
print(fat_cat)


