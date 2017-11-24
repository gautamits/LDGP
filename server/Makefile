requirements:
	sudo apt-get install python-numpy python-scipy python-opencv python-pip zenity 
	sudo pip install easygui
database:
	echo "choose the directory ";\
	folder=$$(zenity --file-selection --directory --title="choose the root folder of database" --filename=~/);\
	python src/database.py $$folder
run:
	python src/client.py 
server:
	ip=$$(ifconfig enp2s0f0 | grep "inet\ addr" | cut -d: -f2 | cut -d" " -f1);\
	echo $$ip;\
	echo "enter the port you want to make server";\
	read port;\
	python src/server.py $$ip $$port
