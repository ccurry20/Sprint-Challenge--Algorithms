'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #base case..length of word less than 2 return 0
    result = 0
    if len(word) < 2:
        return 0

    # If word[0] is "t" and word[1] is "h" add 1 to result
    if word[0] == 't' and word[1] == 'h':
        result += 1

            #This will re-run until a break case, and return this final value.
            #Call the count_th with the word up to the last character you called.

    return result + count_th(word[1:]) #recursive call