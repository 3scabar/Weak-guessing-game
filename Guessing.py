from random import randrange
n = randrange(1000)
while True:
    v = int(input())
    if n == v:
        print("You win!")
        break
    print("Smaller" if (n < v) else "Bigger")
#Generates a random number from the range 1-1000 = (n). if the user input (v) matches (n) "You win!" is printed
#prints smaller is (v) is smaller than (n) else it prints "Bigger" 
