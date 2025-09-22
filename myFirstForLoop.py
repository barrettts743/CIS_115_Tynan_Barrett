#this program uses a for loop that allows the user to enter any number of iterations
#grab user input
num = int(input("Enter your number of iterations you would like to do: "))

#loop over the range of numbers up to the user input
for num in range(num):
    print("This is iteration number", num + 1)