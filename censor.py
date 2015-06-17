def censor(words, cus, debug = False):
    if debug:
        print words
        print cus.upper()

    new_words = ""
    count = 0
    while count < len(words):

        # if we find a letter match
        if words[count] == cus[0]:
            if debug:
                print "first letter match"
                print words[count], cus[0]
            censored_word = "*"
            cus_count = 1
            # look through the cus word and compare
            # it to the phrase
            while cus_count < len(cus):
                found = True
                if debug:
                    print words[count + cus_count], cus[cus_count]
                if words[count + cus_count] == cus[cus_count]:
                    censored_word += "*"
                else:
                    cus_count = len(cus)
                    found = False
                    break
                cus_count += 1
            # if we know we found it, add the words to
            # the string and advance the count iterator
            if found == True:
                if debug:
                    print "found", censored_word
                new_words += censored_word
                count += len(censored_word) - 1
            else:
                if debug:
                    print "not a match"
                new_words += words[count]
        else:
            new_words += words[count]
        count += 1
    if debug:
        print new_words
    return new_words

print censor("silly fucking rabbit, trix are for fucking kids, you fuck!", "fuck")
print censor("Theres a shit typhoon a commin', so haul in the jub before it gets covered in shit", "shit", True)
