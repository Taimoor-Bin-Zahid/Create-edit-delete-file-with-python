import os

#                                                   to create a new txt file


with open ('.\input.txt', 'w') as file:

    try:
        x = file.write("This is a text file")
        file.close()

    except Error as er:
        print(er)

    else:
        print("The file is created successfully")

#                                                    to read a txt file


# with open('.\input.txt', 'r') as file:

#     try:
#         x = file.read()

#         print(x)


#     except Error as er:
#         print(er)

#                                                    to append a txt file

# with open ('.\input.txt', 'a') as file:

#     try:
#         x = file.write("\nThis is a first text file")
#         x = file.write("\nThis is a second text file")
#         x = file.write("\nThis is a third text file")
#         x = file.write("\nThis is a fourth text file")
#         x = file.write("\nThis is a fifth text file")
#         file.close()

#     except OSError as er:
#         print(er)

#     else:
#         print("The file is appended successfully")

# os.remove('.\input.txt')