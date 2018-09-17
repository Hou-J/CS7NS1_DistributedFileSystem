# Directory Service：
The directory service is responsible for mapping human readable, global file names into file identifiers used by the file system itself. A user request to open a particular file X should be passed by the client proxy to the directory server for resolution. The returned file identifier should identify the server actually holding the file (or perhaps, servers, if you have decided to expose replication to client proxies) and the name of the file on that server. It is perhaps best if the directory server maps directories to server:directory identifiers : that is, the directory server should not remap actual file names. This is simply for scale – the are generally a lot more files than directories in a file system,and managing the location of files is probably best done on a per directory basis, implying that a directory service that works at the level of directory mappings is probably sufficient. An alternative model involves storing all files in a file server in a flat file system (i.e. each file server provides a single directory in effect), requiring the directory server to maintain mapping of full file names to server:filename mappings. You may choose either scheme, or a variant of your own devising.

## Usage:
    
       first: python server.py [PORT]
       second: python client.py [IP] [PORT]

## Note:
        
All fuctions should be operated by inputing the full path and file name.
	
	

