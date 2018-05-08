import shutil

def copyDirectory(src, dest):
   try:
       shutil.copytree(src, dest)
   # Directories are the same
   except shutil.Error as e:
       print('Directory not copied. Error: %s' % e)
   # Any error saying that the directory doesn't exist
   except OSError as e:
       print("failed"+e)

print("started copying")
copyDirectory("/Users/apple/Documents/tushar","/Users/apple/Documents/tushar2")
print("completed copying")
