![hBnB](img/hbnblogo.png)
# AirBnB Clone Proyect - The Console

### :computer: Introduction :computer:
This team proyect is the first step to create our clone of the AirBnB Website.
This first part is the **Console**, when we are going to manage objects.

## :page_with_curl:  How it Works? :page_with_curl:

To start the console you can do it in two ways, interactive and non-interactive mode.

#### Interactive Mode
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

#### Non-Interactive Mode
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
