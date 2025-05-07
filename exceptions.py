#try keyword allows python to check
try:
    x = int(input("what's the value of x? "))
 #print("x is", x) or
    print(f"x is {x}")
#except keyword indicates do something goes wrong  , ValueError keyword
except ValueError:
    print("x is not an integer")

#  using else
try:
    x = int(input("what's the value of x? "))
except ValueError:
    print("x is not an integer")
else:
    #f inficates format string or F-string
    print(f"x is {x}")


