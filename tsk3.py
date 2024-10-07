ask = input("do you want to remove an element by index or value? ")
name = ["angela", "julia", "allyssa","ellize", "chino"]

if ask  == "index":
    Name = int(input("which name do you want to delete? "))
    name.pop(Name)
    print(name)
    
elif ask  == "value":
    Name = input("which name do you want to delete? ")
    name.remove(Name)
    print(name)
    
    



