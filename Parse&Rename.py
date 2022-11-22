import os

# os.chdir(r'C:\Dir1\SubDir1\SubDir2\SubDir3')- For windows
# os.chdir('/User/Dir1/SubDir1/) - For Linux or MAC
# print(f"{os.getcwd()} is the current directory")

# Write all the files in the current directory
# for f in os.listdir():
#     print(f)

# Go the file Parse&Rename.txt
with open('Parse&Rename.txt','r') as parseFile:
    # Read each item
    # parseData = parseFile.read()

    # Read per line
    # parseData = parseFile.readline(100)
    # parseData = parseFile.readline()

    # Read per line
    parseData = parseFile.readlines()

    # print(parseData,'-->Parse Data')

newName=[]
newFile=[]
for f in parseData:
    # print(f)
    x = f.splitlines()
    # print(x)


    for i in x:
        # print(i.split('.'))
        course, ext = i.split('.')
        planet, title, num = course.split(' - ')
        # Remove the number sign#. zfill (zero filled) replacing the # sign
        num = num.strip()[1:].zfill(2)

        # print(f"{num}-{planet}-{title}-{ext}")
        # print(f"{num}-{planet}.{ext}")

        newName = '{}-{}.{}'.format(num, planet, ext)
        newFile.append(newName)
        # print(newName)
        # print(newFile)
    

# print(newFile)

# Sorting the list in ascending order
x = sorted(newFile)

# Sorting the list in descending order
# x = sorted(newFile,reverse=True)

# print(x)

for i in x:
    print(i)
# for i in newFile:
#     print(i)
        
   




    