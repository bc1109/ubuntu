import os

os.chdir('/home/brandon/Desktop/Python_Google')

for filename in os.listdir():
    if filename.endswith('.txt'):
        #os.unlink(filename)  # comment'd out to see what files will actually be deleted. 
        print(filename)
