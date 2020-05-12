import sys 
import time

#time.sleep(2) is cool, play with it. 

print ('Hello, what is your name?')
myName=input()


if myName == 'Brandon':
    time.sleep(2)
    print ('My name is Brandon as well')
    

print ('It is nice to meet you, ' + myName)
   
print ('Can I ask how old are you? - Y/N?')
myResponse=input()

if myResponse == 'N' or 'n':
     print ('Well, this conversation is going no where. Peace! I\'m\' out')

     #find out how to end the script here and push them out

if myResponse == 'Y' or 'y':

    print ('How old are you?')
    myAge=input()
    myDogage=str(int(myAge) * 6)
    print ('This is how many years old you are in dog years:' + myDogage)


