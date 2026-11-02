fruits = ["Apple", "Orange", "Mango", "Grapes", "Pineapple"]

userfruit=input("Enter a fruit to check if we have it in stock:")

FLAG=0
for i in fruits:
    if userfruit==i:
        print("FOUND!")
        FLAG=1
if FLAG==0:
    print("NOT FOUND!")