#nested loop
#column
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

#row
def main():
    print_row(4)
def print_row(width):
    print("#" * width)

main()


#block like mario game
def main():
    print_square(3)
def print_square(size):

    #for  each row in square
    for i in range(size):

    #for each brick in row
       for j in range(size):

           #print brick
           print("#", end = "")
       print()

main()

#OR
def main():
    print_square(3)
def print_square(size):
    for i in range(size):
        print("#" * size)
main()

#OR
def main():
    print_square(3)
def print_square(size):
    for i in range(size):
        print_row(size)
def print_row(width):
    print("#" * width)

main()