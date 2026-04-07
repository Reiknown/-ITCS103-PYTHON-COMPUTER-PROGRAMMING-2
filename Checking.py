# Checking if the file exists
import os

current = os.getcwd()
print(current)

# file_dir = os.path.join(file name)
file_dir = os.path.join(current, 'Hanni.txt')

if os.path.exists(file_dir):
    file = open("Hanni.txt","r")
    content = file.read()
    print(content)
else:
    print('file does not exists')