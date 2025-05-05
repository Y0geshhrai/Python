#nested loop

def main():
    print_column(4)


def print_column(height):
    for _ in range(height):
        print("***")

main()

#OR
def main():
    print_column(4)


def print_column(height):
    print("***\n" * height , end= "")
main()