#!/usr/bin/python3
write_file = __import__('1-write_file').write_file

# Writing text to a file and printing the number of characters written
nb_characters = write_file("my_first_file.txt", "This School is so cool!\n")
print(nb_characters)

