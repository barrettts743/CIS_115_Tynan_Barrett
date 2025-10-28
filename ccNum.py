#this program will use the mod 10 function to validate a credit card number recieved from the user
#create the function to define the credit card validation
def validateCreditCard(ccNum):
    ccNum = input('Enter your credit card number: ')
    #create 2 lists to hold the digits
    oddDigits= []
    evenDigits = []
    total = 0
    #loop through the credit card number and separate the digits into odd and even lists
    for i in range(len(ccNum)-1, -1, -1):
        if (len(ccNum)-i) % 2 == 0:
            evenDigits.append(int(ccNum[i]))
        else:
            oddDigits.append(int(ccNum[i]))

    #double the even digits and if the result is greater than 9, subtract 9 from it
    for i in range(len(evenDigits)):
        evenDigits[i] = evenDigits[i] * 2
        if evenDigits[i] > 9:
            evenDigits[i] -= 9
    #sum all the digits in both lists
    total = sum(oddDigits) + sum(evenDigits)








