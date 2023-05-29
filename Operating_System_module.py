import os
import datetime as datetime

# print(dir(os))

# To get current working directory
print(os.getcwd())

# to change directory e.g ('/Users/file_folder/destination/')

# For Windows Operating System put 'r' to make it raw
# os.chdir(r'C:\Users\file_folder\Python_text_practice')
os.chdir(r'\Users\file_folder\Python_text_practice')

# print(os.getcwd())

#Create only top level directory
os.mkdir(r'OS-Demo')

# Create only top level directory and sub directory (tree structure)
os.makedirs(r'OS-Demo\Sub-Dir1')

# Remove directory /directories
os.rmdir(r'OS-Demo')
os.removedirs(r'OS-Demo\Sub-Dir1')

# Rename a file
os.rename('test_text.txt', 'new_test_text.txt')
os.rename('new_test_text.txt','test_text.txt')

# To list directory
print(os.listdir())
print(os.stat('test_text.txt'))

# Result of above
# os.stat_result(st_mode=33206, st_ino=9570149208350233,
# st_dev=776891029, st_nlink=1, st_uid=0, st_gid=0, st_size=11,
# st_atime=1589602867, st_mtime=1589602867, st_ctime=1589602867)

# Return a time stamp 1589602867.871859
print(os.stat('test_text.txt').st_mtime)

# To convert a human readable timestamp 2020-05-15 21:21:07.871859
mod_time = os.stat('test_text.txt').st_mtime
print(datetime.fromtimestamp(mod_time))

# If want to return a string representing the date.strftime(format)
str_time = datetime.fromtimestamp(mod_time)
print(str_time.strftime("The date is %B %d %Y time %I:%M:%S %p"))

#Using f-string. Do not forget to differentiate quotes ' / "
print(f'The month is {str_time.strftime("%B")} day is {str_time.strftime("%d")} year is {str_time.strftime("%Y")}')

# To go through path directories and filename by using os.walk
for dirpath, dirnames, filenames in os.walk(r'\Users\Documents\'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()

#"HOMEPATH, HOMEDRIVE, COMPUTERNAME, APPDATA, ALLUSERPROFILE, PUBLIC, USERPROFILE
# print(os.environ.get('HOMEDRIVE'))
# Use USERPROFILE (windows OS) instead of HOME (only for linux operating system)
# print(os.environ.get('HOME'))
# print(os.environ.get('USERPROFILE'))

# To add a file to your path
# This is not good example because it might forget the "\test_test.txt"
# file_path = os.environ.get('HOME') + 'test_text.txt')
# Best alternative is to use os.path.join using two args ('HOME', 'test_text.txt')
# file_path = os.path.join(os.environ.get('HOME', 'test_text.txt'))

# To get methods useful in os.path
print(dir(os.path))

'''['__all__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_abspath_fallback', '_get_bothseps', '_getfinalpathname', '_getfinalpathname_nonstrict', '_getfullpathname', '_getvolumepathname', '_nt_readlink', '_readlink_deep', 'abspath', 'altsep', 'basename', 'commonpath', 'commonprefix', 'curdir', 'defpath', 'devnull', 'dirname', 'exists', 'expanduser', 'expandvars', 'extsep', 'genericpath', 'getatime', 'getctime', 'getmtime', 'getsize', 'isabs', 'isdir', 'isfile', 'islink', 'ismount', 'join', 'lexists', 'normcase', 'normpath', 'os', 'pardir', 'pathsep', 'realpath', 'relpath', 'samefile', 'sameopenfile', 'samestat', 'sep', 'split', 'splitdrive', 'splitext', 'stat', 'supports_unicode_filenames', 'sys'] '''

# Linux uses forward slash '/' Windows back slash '\'

# print (os.path.basename(/tmp/test.txt)) # print out test.txt
# print(os.path.basename(r'\tmp\test.txt')) # print out test.txt

# print(os.path.dirname(r'\tmp\test.txt')) # print out \tmp directory

# print(os.path.split(r'\tmp\test.txt')) # print out ('\tmp', 'test.txt')

# print(os.path.exists(r'\tmp\test.txt')) # To check if the directory exist

# print(os.path.isdir(r'\tmp\test.txt')) # To check if the directory exist

# print(os.path.isfile(r'\tmp\test.txt')) # To check if the file exist

# print(os.path.splitext(r'\tmp\test.txt')) # result ('\tmp\test', '.txt) parse out the extension

















