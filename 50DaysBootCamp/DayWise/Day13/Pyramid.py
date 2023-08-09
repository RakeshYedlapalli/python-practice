from emoji import emojize


def pyramid():
    numberOfStars = int(input("Enter number of stars:"))

    for x in range(1, numberOfStars+1):
        #print("X value ->", x)
        print()
        for x in range(0, x):
            print('*', end=' ')


def Python_snakes(n: int):
    # the loop to determine the number of rows of the pyramid
    for i in range(0, n):
        # The loop that determines number of columns
     for j in range(n, i, -1):
        # print space between the snake signs
        print(end=" ")
     for k in range(0, i):
        # printing the snake emoji
         print(emojize(':snake:'), end=" ")
     print("\n")


pyramid()
Python_snakes(10)
