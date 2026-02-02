variable = input("Enter a variable name in camel case: ")
new_variable = ("")
for i in variable:
    if i.isupper():
        new_variable = new_variable + ("_") + i.lower()
    else:
        new_variable = new_variable + i

print(new_variable)