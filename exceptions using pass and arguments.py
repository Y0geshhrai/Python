#pass
def main():
    x = get_int("what's x?" )
    print(f"x is {x}")

#prompt is what you wanna see
def get_int(prompt):
    while True:
        try:
           return int(input(prompt))
        except ValueError:
            pass
main()

#or using prompt
def main():
    x = get_int("what's x?" )
    print(f"x is {x}")

#prompt is what you wanna see
def get_int():
    while True:
        try:
            return int(input("what's the value of x?" )
        except ValueError:
            pass
main()
