Jiongxu Hou  17304249

There is a readme in each folder.


# Individual Programming Project
The assignment is to design and implement a distributed file system exhibiting a range of properties. This system should be constructed using REST services. 

The task is to design and implement a distributed file system including a set of 7 optional features. A distributed file system consisting of a set of individual services or components, that we itemise below:
Distributed Transparent File Access, 
Security Service, 
Directory Service, 
Replication, 
Caching, 
Transactions, 
Lock Service.

Grading will be assesed based on a maximum of 25% for any feature implemented, with a total grade capped at 100%. Thus, if you complete 7 features, then your work will be graded out of a maximum of 175%, with any grade above 100% reduced to 100%. It is anticipated that most students will implement 4 features.

## DistributedTransparentFileAccess
	
Client using restful to access the files on the server.

Can view file list, read a file, edit a file or delete a file.

## DirectoryService

The client can only take the whole path together with the filename as input (e.g. files\asd\123.txt).

View directory using *os.walk()*.

When deleting a folder, all the folder and files inside are deleted (*shutil.rmtree()*).

## LockService

Using a list to store the clientid together with the file they are occupying, only the clientid matched, can the client access the file.
	

## Caching

This is not fully done, my thought is to use a dict as the local cache.
Store all the operation to that cache.
Push the cache to the server when exiting or manually select push.
	

### Dependencies:
		
	pip install -r requirements.txt