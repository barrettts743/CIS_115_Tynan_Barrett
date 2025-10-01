#this program will use a user defined function to loop over
#a list and print the loop variable
#define user function
def getMyList():
    list = ['10, 20, 30, 40, 50, 60'] * 6
    return list

#assign list to variable
myList = getMyList()
for numbers in myList:
    print(numbers)

 #print total of loop iterations
print("The total number of loop iterations was:", len(myList))