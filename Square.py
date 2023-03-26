a = int(input("Enter your first number: "))
b = int(input("Enter your second number: "))
x = int(((a - b)/2))
y = b

if b >= a:
    print("Wrong order!")
elif ((a - b)%2) != 0:
    print("Wrong difference!")
else:
    while x > 0:
        print("*" * a)
        x = x - 1
    x = int((a - b)/2)
    while y > 0:
        print("*" * x , " " * (b - 2) , "*" * x)
        y = y - 1
    while x > 0:
        print("*" * a)
        x = x - 1