import os
# only works in linux
# user needs to be root for script to work (sudo -i) in the terminal
# if the file opendir.txt already exists
# removes it
if os.path.exists('./opendir.txt'):
	os.remove('./opendir.txt')
	print "file removed"

# open all directories and subdirectories and print out the path for each file found
# to only open dirs and files for current directory replace "/" with "."
for root, dirs, files in os.walk("/", topdown=False):
    for name in files:
	filepath = (os.path.join(root, name))
        print filepath
	#writes to file
	with open("opendir.txt", "a") as myfile:
		myfile.write(filepath + "\n")
    for name in dirs:
	dirpath = (os.path.join(root, name))
        print dirpath
	#writes to file
	with open("opendir.txt", "a") as myfile:
		myfile.write(dirpath + "\n")
