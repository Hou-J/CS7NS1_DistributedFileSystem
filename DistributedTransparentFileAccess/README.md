DFS task:
Jiongxu Hou 17304249

Distributed Transparent File Access:

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
	
	required input:
	
		number of workers
		
		github username
		
		github password(used package getpass)
		
		the repository belonged user
		
		the repository name
		
		
client:
	
	start with:	python worker.py [IP] [Port]
	
	no required input
	
	need open exact number of workers as the manager required
	
	
will add a .sh file later


