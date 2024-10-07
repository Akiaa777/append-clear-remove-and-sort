
ask = input("delete?: ")
numbers = ["6", "5", "4", "3"]
if ask == "yes":
    numbers.clear()
    print(numbers)
    
elif ask == "no":
    print(numbers)
