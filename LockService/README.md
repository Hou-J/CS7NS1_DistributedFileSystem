# Lock Service:
The lock service is an important user tool. Certain classes of user applications will modify (deliberately) the same files in a distributed file system. Such tools will need exclusive access to the files they modify. To provide this exclusive access, the client proxy can make use of a lock server. This server simply holds a semaphore for each file it is told about. Any client wishing to access a file could simply ask for access from the lock server. Providing all other clients do the same, it can be sure that ot has exclusive access when access is granted.

This service could be exposed (via the client proxies user API) to user applications. Alternatively, it could be provided as an attribute for particular directories. If, for example, the directory service was designed to allow particular directories to be marked as lockable, then the client proxy could be designed to use the locking service for access to files in that directory. This would mean that clients need not be aware of locking but would still benefit from it – ie. Transparency.

There are many possible schemes – use you imagination – but be sure to have valid reasons in mind when you finally settle on one or more solutions.

One for the advanced – consider how applications could be provided with support to enable them to usefully share files simultaneously. For example, an event service could let applications know when someone else modifies a file they are modifying – what would this be useful for? A groupware lock service?

## server:

	the ip is: 0.0.0.0
	
	start with:	python manger.py [Port]
	
## client:
	
	start with:	python worker.py [IP] [Port]
	
## note:
Lock the file during editing or deleting it, only the client who first select that file can edit or delete the file.

