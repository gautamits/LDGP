requirements:
	sudo apt-get install python-numpy python-scipy python-opencv python-pip 
	sudo pip install easygui
database:
	echo "enter the directory name"
	read a
	python database.py $a
run:
	python 
