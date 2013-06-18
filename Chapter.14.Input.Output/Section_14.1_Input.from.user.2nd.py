def reverse(text):
        return text[::-1]
def is_palindrome(text):
        return text == reverse(text)

something = input('Enter text: ')
punctuation = [',', ' ', '_', '.', '\t', '?', '!', ':', ';',\
                '-', '()', '[]']        # the most common punctuation
                                        # symbols used in daily life.

# for symbol in punctuation:
for (symbol in punctuation):
        if (symbol in something)
                # if i in punctuation:
                # print(symbol)
                replace_punt = something.replace(symbol, '') # replace_punt
                                                # is the string after replace
                                                # all punctuation symbols.

if (is_palindrome(rplc_punt)):
        print("Yes, it is a palindrome")
else:
        print("No, it is not a plindrome")

