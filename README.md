# Understanding-OS-module-and-OSError
The OS module in Python provides a portable way of using operating system dependent functionalities that is it allows us to interface with the underlying operating system that Python is running on – be that Windows, Mac or Linux. It's a way of interacting with the operating system by using functions of this module. The *os* and *os.path* modules include many functions to interact with the file system.

## OS Functions
* __import os__  
For importing the module in program
* __os.system()__  
Executing a shell command
* __os.getcwd()__  
Returns the current working directory.
* __os.environ()__  
Get the users environment 
* __os.getuid()__  
Return the current process’s user id.
* __os.getgid()__  
Return the real group id of the current process.
* __os.getpid()__  
Returns the real process ID of the current process.
* __os.umask(mask)__  
Set the current numeric umask and return the previous umask.
* __os.chroot(path)__  
Change the root directory of the current process to path.
* __os.uname()__  
Return information identifying the current operating system.
* __os.listdir(path)__  
Return a list of the entries in the directory given by path.
* __os.makedirs(path)__  
Recursive directory creation function.
* __os.mkdir(path)__  
Create a directory named path with numeric mode mode.
* __os.remove(path)__  
Remove (delete) the file path.
* __os.removedirs(path)__  
Remove directories recursively.
* __os.rmdir(path)__  
Remove (delete) the directory path.
* __os.rename(src, dst)__  
Rename the file or directory src to dst.

## OS Module: os.stat()
os.stat() is used to perform a stat system call on the given path. This module defines functions and constants that are used for interpreting the results of os.stat(), os.fstat() and os.lstat() (if they exist). For carrying out this process, first we need to import os module and then specify the path of the file on which you want to perform the system call by using the following syntax:

    import os
    print("os.stat    = status of a file 	" , os.stat('/usr/bin/vi'))
    
* __Output__  
 
      os.stat    = status of a file 	posix.stat_result(st_mode=33261, st_ino=1835889, st_dev=37, st_nlink=1, st_uid=0, st_gid=0,      st_size=1092688, st_atime=1498220605, st_mtime=1498220605, st_ctime=1545683204)

 The function os.stat(path) returns stat information about path in the same format (which happens to have originated with the POSIX interface).
 
 ## Note
All functions in this module raise OSError in the case of invalid or inaccessible file names and paths, or other arguments that have the correct type, but are not accepted by the operating system.

## OSError
In case of invalid or inaccessible file names and paths, or other arguments that have the correct type, but are not accepted by the operating system, the functions in this module raise OSError. os.error is an alias for built-in OSError exception.

## Example program to understand os.stat, OSError with try and except  

    import os
    print(dir(os))
    
    def static_file(path):       #function defined and the text file is passed
    try:                         # if file is found it enters try block for execution.
         os.stat(path)           #The method stat() performs a stat system call on the given path.
         print(os.stat(path))    #it returns protection bits, inode number,device, number of hard links etc.
         print("os.stat is working")
     except OSError:
         print("os error")

    static_file("a.txt") #function is being called here.



## References
https://docs.python.org/3/library/os.html  
https://docs.python.org/2/library/stat.html  
https://www.geeksforgeeks.org/os-module-python-examples/
