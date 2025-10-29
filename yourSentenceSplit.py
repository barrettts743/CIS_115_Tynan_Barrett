#this program will count the frequency of each word in a sentence entered by the user

#function to count word frequency
def word_frequency(yourSentence):
    #split the sentence into words
    words = yourSentence.split()
    #initialize an empty dictionary to hold the word counts
    word_count = {}
    #count the frequency of each word in the sentence
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    return word_count

#prompt the user for a sentence
yourSentence = input("Enter a sentence: ")
frequency = word_frequency(yourSentence)

#print the word frequency
print('Word Frequency:')
for word, count in frequency.items():
    print(f'"{word}": {count}')
