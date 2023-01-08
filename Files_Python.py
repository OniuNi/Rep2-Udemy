# To open a file in Python, we use its built-in open() function.
# This function returns a file object, that would be utilized to call other methods associated with it.

# file object = open(file_name, access_mode)

# filename: It is the name of the file which needs to be opened.
# access_mode: It specifies the mode in which the file has to be opened such as read, write and so on.
# By default, it will be in the read-mode.

# We can specify the mode while opening a file, to specify whether
# we want to read(r),
# write(w) or
# append(a) to the file.

# There are six access modes available in python to work with a text file,
# “r” – Read mode is used only to read data from the file. It is also the default mode.
# “w” – It will create a new file if it does not exist, otherwise will overwrite the file and allow you to write to it.
# “a” – It will write data to the end of the file. It does not erase the existing data, and the file must exist for this mode.
# “r+” – It opens the file to read and write both. The file pointer will be at the beginning of the file.
# “w+” – The exact same as r+ but if the file does not exist, a new one is made. Otherwise, the file is overwritten.
# “a+” – Similar to w+ as it will create a new file if the file does not exist. Otherwise, the file pointer is at the end of the file if it exists.

path = "C:\Users\Nicoleta\OneDrive\Desktop\read.txt"

# myFile = open('path','r')
# file_handle.read(N)

# myFile.read()

file_input = open("read.txt", 'r')
data = file_input.readline()
print(data)
