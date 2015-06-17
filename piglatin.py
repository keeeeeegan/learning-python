pyg = 'ay'

original = raw_input('Enter a word:')

if not (len(original) > 0 and original.isalpha()):
    print 'Error - invalid input'
    exit()
    
word = original.lower()
first = word[0]

new_word = word[1:len(word)] + first + pyg
print new_word
