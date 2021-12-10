formatter = "{} {} {} {}"

print(formatter.format(1,2,3,4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False,True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
        "lala 1",
        "bo bo 2",
        "paz paz 3",
        "panpan 4"
))
