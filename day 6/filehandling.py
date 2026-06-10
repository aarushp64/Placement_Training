# file handling in python help you in read write and append and modify the files stored on you system.
# 'r' for read, 'w' for write, 'a' for append, 'x' for create, 't' for text mode, 'b' for binary mode.'
# 'r+' for read and write, 'w+' for write and read, 'a+' for append and read.


# file = open('./README.md', 'r')
# content = file.read()
# print(content)
# file.write("\nThis is a new line added to the file.")   
# file.close()



# file = open('file.txt', 'x')

# file = open('file.txt', 'w')
# file.write("This is a new file created using Python.")
# file.close()
# file = open('file.txt', 'a')
# file.write("\nThis line is appended to the file.")
# file.close()

# file = open('file.txt', 'a')
# file.write('''\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Donec sapien risus, facilisis ac nunc eu, laoreet tempus diam. Maecenas tortor orci, dignissim accumsan sollicitudin vitae, ornare mollis eros. Maecenas luctus nisi sit amet lectus imperdiet molestie. Curabitur sollicitudin gravida diam. In in ipsum in arcu porta lobortis. Duis ullamcorper dignissim imperdiet. Aliquam arcu neque, finibus eget consequat sit amet, laoreet eget nisi. Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi congue ipsum mauris, nec varius dui iaculis vel. Aenean elementum fringilla erat aliquet pharetra. Nam sit amet urna feugiat, sollicitudin odio et, tempor elit. Morbi eu volutpat ex. Mauris commodo non metus ut fringilla. Ut elementum tortor vel elementum rhoncus. Aenean efficitur et velit ac dapibus. Phasellus faucibus in metus sed.''')
# file.close()
# file = open('file.txt', 'r')
# content = file.read()
# print(content)
# file.close()

   

# Open the file in read mode using 'with', which automatically closes the file 
# with open("file.txt", "r") as f: 
#     text = f.read()
#     f.append("\nThis line is appended to the file using with statement.\n") 
# print(text)


#count the number of lines and words and characters in a file
# with open("file.txt", "r") as f:
#     lines = f.readlines()
#     print("Number of lines in the file:", len(lines))
#     words = 0
#     for line in lines:
#         words += len(line.split())
#     print("Number of words in the file:", words)        
#     characters = sum(len(line) for line in lines)
#     print("Number of characters in the file:", characters)

# Check if a file exists and delete it
import os
if os.path.exists("file.txt"):
    os.remove("file.txt")
else:    print("The file does not exist.")