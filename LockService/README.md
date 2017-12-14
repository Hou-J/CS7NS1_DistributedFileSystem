DFS task:
Jiongxu Hou 17304249

Lock Service:

Dependencies:
		
	flask:
		used to implement the restfull api
		
		can be installed through	pip install flask
		
	flask_restful:
	
		used to implement the restfull api
		
		can be installed through	pip install flask_restful
		
	requests:
	
		used to get requests
		
		can be installed through	pip install requests


server:

	the ip is: 0.0.0.0
	
	start with:	python manger.py [Port]
	
		
		
client:
	
	start with:	python worker.py [IP] [Port]
	
note:
    
        locking during editing or deleting, only the client who first select that file can edit or delete the file.
	
will add a .sh file later


