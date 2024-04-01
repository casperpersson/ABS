spam = 0
while spam < 5:
    print("hello world!")
    spam = spam + 1

name = ""
while True:
    print("please type your name.")
    name = input()
    if name == "Casper":
        break
print("Thank you")

spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print("spam is " + str(spam))