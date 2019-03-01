import os
print(dir(os))
# print(os.uname())
def static_file(path):    #function defined and the text file is passed
    try:                # if file is found it enters try block for execution.
        os.stat(path)   #The method stat() performs a stat system call on the given path.
        # print(os.stat(path))  #it returns protection bits, inode number,device, number of hard links,  user id of owner,
                                #group id of owner, size of file, in bytes, time of most recent access,
                                #time of most recent content modification, chatbot-errors/os-errors.py.
        print("os.stat is working")
    except OSError:
        print("os error")

static_file("a.txt") #function is being called here.
