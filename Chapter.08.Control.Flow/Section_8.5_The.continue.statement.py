# the continue statement is used to tell python to skip the rest of
# the statements in the current loop block and to continue to the next
# iteration of the loop.

while True:
        s = input('Enter something :')
        if s == 'quit':
                break
        if len(s) < 3:
                print('Too small')
                continue
        print('Input is of sufficient length')
