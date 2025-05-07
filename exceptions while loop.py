
#  using while loop and break(if not break use it loops everytime)
while True:
    try:
        x = int(input("what's the value of x? "))
    except ValueError:
        print("x is not an integer")
    else:
        break
print(f"x is {x}")

#or
while True:
    try:
        x = int(input("what's the value of x? "))
        break
    except ValueError:
        print("x is not an integer")
print(f"x is {x}")

#or
def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
    while True:
        try:
            x = int(input("what's the value of x? "))
        except ValueError:
            print("x is not an integer")
        else:
            return x

main()

 #or
def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
          return int(input("what's the value of x? "))
        except ValueError:
            print("x is not an integer") #or use pass keyword without print

main()
