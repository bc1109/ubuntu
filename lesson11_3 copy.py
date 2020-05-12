print('How many cats do you have?')
numCats = input ()
try:
    if int(numCats) <0:
        print('Wait, is that even possible?')
    #if int(numCats) =0:
        print('Sorry to hear you do not have any cats.')
    if int(numCats) >=4:
        print('That is a lot of cats.')
    if int(numCats) <=3:
        print('That is not that many cats.')
except ValueError:
    print('***You did not enter a number')