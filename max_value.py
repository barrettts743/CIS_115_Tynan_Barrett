#this program attemppts to grab two integer values from user
#and determine which is the larger value
#grab values from user
num1 = int(input('Enter a number: '))
num2 = int(input('Enter another number: '))


def max_value():
    #determine which value is larger
    if num1 > num2:
        return num1 
    else: 
        return num2
    #print the larger value
print('The larger value is:', max_value())
    

#call the funtion
max_value()
