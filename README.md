![hBnB](img/hbnblogo.png)
# AirBnB Clone Proyect - The Console

### :computer: Introduction :computer:
This team proyect is the first step to create our clone of the AirBnB Website.
This first part is the **Console**, when we are going to manage objects.

## :construction_worker:  How it Works? :construction_worker:

To start the console you can do it in two ways, interactive and non-interactive mode.

#### Interactive Mode (type ./console.py)
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

#### Non-Interactive Mode (type echo ***command*** | ./console.py)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

### :speech_balloon: Basic Commands :speech_balloon:
The basic commands to use the console are:

| Command | Description |
| ------- | ----------- |
| ***quit*** | Exit the program |
| ***help*** | See available commands |

### :speech_balloon: Commands :speech_balloon:
| Command | Description |
| ------- | ----------- |
| ***create*** **(class)** | Creates a new instance of class and prints id |
| ***show*** **(class)** **(id)** | Prints the string representation of an instance |
| ***destroy*** **(class)** **(id)** | Prints the string representation |
| ***all*** **(class)** | Prints all string representation of all instances based or not on the class name |
| ***update*** **(class)** **(id)** **(attribute)** | Updates an instance based on the class name and id by adding or updating attribute |


## Usage

After typing ./console.py is going to show you the prmopt "(hbnb)", this is were you are going to type your commands to manage the console.

- To create a new instance just type **create** (class), if the class name is valid it would create a new instance and print it's id.
```
EXAMPLE:
	Input: (hbnb) create User
	Output: (hbnb) 9922284e-208c-42e6-ad39-e49075d007cb
```
- To Print the string representation of the instance type **show** (class) (id)
```
EXAMPLE:
	Input: (hbnb) show User 9922284e-208c-42e6-ad39-e49075d007cb
	Output: (hbnb) [User] (9922284e-208c-42e6-ad39-e49075d007cb) {'id': '9922284e-208c-42e6-ad39-e49075d007cb', 'created_at': datetime.datetime(2022, 3, 6, 9, 29, 7, 491528), 'updated_at': datetime.datetime(2022, 3, 6, 9, 29, 7, 492172)}
```
- If you want to delate an instance, in this case a User, type **destroy** (class) (id)
```
EXAMPLE:
	Input: (hbnb) destroy User 9922284e-208c-42e6-ad39-e49075d007cb
	Output: (hbnb) 
```
- You can update the instance you want by adding any attribute just typing **update** (class) (id) (attribute)
```
EXAMPLE
	Input: (hbnb) update User 9922284e-208c-42e6-ad39-e49075d007cb email "userexample@gmail.com"
	Output: (hbnb) show User 9922284e-208c-42e6-ad39-e49075d007cb
	        (hbnb) [User] (9922284e-208c-42e6-ad39-e49075d007cb) {'id': '9922284e-208c-42e6-ad39-e49075d007cb', 'created_at': datetime.datetime(2022, 3, 6, 9, 29, 7, 491528), 'updated_at': datetime.datetime(2022, 3, 6, 9, 29, 7, 492172), 'email': 'userexample@gmail.com'}


