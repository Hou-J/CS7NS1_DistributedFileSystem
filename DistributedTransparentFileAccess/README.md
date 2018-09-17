# Distributed Transparent File Access:

This is the core of any distributed file system and will consist of a server which provides access to files on the machine on which it is executed and a client side file service proxy that provides a language specific interface to the file system. This system should provide functionality compatible with either an upload/download, or a NFS style access model. It should exhibit a layered design to simplify its extension to support other features as the file systems functionality grows.

A client side file system proxy should be provided as a lirbary, that hides all access to the file system behind a simple language specific mechanism. Henceforth, this component will be referred to simply as the client proxy. The client proxy should be packaged as a library and you should implement a sample client side application that makes use of ths interface (such as a simple text editor for example).




### server:

	the ip is: 0.0.0.0
	
	start with:	python manger.py [Port]
	
		
		
### client:
	
	start with:	python worker.py [IP] [Port]
	

