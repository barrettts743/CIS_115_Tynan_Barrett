#this program will add a nested for loop to a program that already
#has a for loop to loop over a list and print each value
def printWordList():
    myList = ['Apples', 'Bananas', 'Pears', 'Carrots']
    return myList

#assign list to variable and loop over list
#then using a nested loop to loop back over and print results
wordList = printWordList()
for word in wordList:
    print(word)
    for fruit in word:
        print(fruit)