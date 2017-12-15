Jiongxu Hou  17304249

there is a readme in each folder.

DistributedTransparentFileAccess
	
	client using restful to access the files on the server.
	can view file list, read a file, edit a file or delete a file.

DirectoryService

	the client can only take the whole path together with the filename as input(e.g. files\asd\123.txt).
	view directory using os.walk().
	when deleting a folder, all the folder and files inside are deleted (shutil.rmtree()).

LockService

	using a list to store the clientid together with the file they are occupying,
	only the clientid matched, can the client access the file.
	
Caching

	this is not fully done, my thought is to use a dict as the local cache.
	store all the operation to that cache.
	push the cache to the server when exiting or manually select push.
	

	