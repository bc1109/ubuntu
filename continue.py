spam = 0
while spam <10:
    spam = spam + 1
    if spam == 3: #3 isn't printed because of the continue. 
        continue
    print('spam is ' + str(spam))
