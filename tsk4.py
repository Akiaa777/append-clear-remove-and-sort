numbers = ["18", "16", "60", "20"]
ask = input("sort or reverse? ")

if ask == "sort":
    numbers.sort()
    print(numbers)
    
elif ask == "reverse":
    numbers.reverse()
    print(numbers)