string = input("please enter any word:")
hup = input("Please enter your character:")
i = 0 
count = 0
while (i < len(string)):
    if (string[i] == hup):
        count = count + 1
    i = i + 1
print("The total number of times ", hup, " has occurred = ", count)
