# File Objects

f = open('test.txt', 'w')
f.write('1) This is a test file!\n')
f.write('2) With multiple lines of data...\n')
f.write('3) Third line\n')
f.write('4) Fourth line\n')
f.write('5) Fifth line\n')
f.write('6) Sixth line\n')
f.write('7) Seventh line\n')
f.write('8) Eight line\n')
f.write('9) Ninth line\n')
f.write('10) Tenth line\n')
f = open('test.txt', 'r')

# Read the file
print(f.read())

# Do not forgot to close the file!!!
f.close()

# Recommend to use context managers: 
# After reading the file it will be automatically be closed.
with open('test.txt', 'r') as f:
    f_contents = f.readline()

    print(f_contents, end='')
    f_contents = f.readline()

    print(f_contents, end='')
    f_contents = f.readline()

    print(f_contents, end='')
    print('\n')

# For a larger file to iterate use the for loop:
with open('test.txt', 'r') as f:
    for line in f:
        print(line, end='')
print('\n')

# For more control!
with open('test.txt', 'r') as f:
    size_to_read = 15
    f_contents = f.read(size_to_read)
    print(f_contents, end='')

    print(f.tell())
    f_contents = f.read(size_to_read)

    print(f_contents)

    print(f.tell())
    
print('\n')

with open('test.txt', 'r') as f:
    size_to_read = 100
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='*')
        # Without this advance the above will be in a forever loop
        f_contents = f.read(size_to_read)

# f = open('test.txt', 'w')
# lines_of_text = ["One line of text here", " Second line of text", " Third line"," And So on...."]
# f.writelines(lines_of_text)
# f = open('test.txt', 'r')
# f_contents = f.read()
# print(f_contents)
# # for line in f:
# #     print(line,'\n')
# f.close()






# Basic
# f = open('test.txt', 'r')
#
# print(f.mode)
#
# f.close()
