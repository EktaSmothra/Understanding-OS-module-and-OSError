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


