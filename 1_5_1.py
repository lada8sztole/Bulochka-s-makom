# Task 1
#
# Make a program that has some sentence (a string) on input and returns a dict containing
# all unique words as keys and the number of occurrences as values.

# a = 'Apple was sweet as apple'
# b = a.split()
a = input('enter the string ')
def word_count(str):
    counts = dict()
    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts
print(word_count(a))
