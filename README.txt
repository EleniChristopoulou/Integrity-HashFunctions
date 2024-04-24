To run program succesfully:

1. In a terminal run command
	python3 commander.py
	
2. Insert first command or string

3. Then in a new terminal run command
	python3 receiver.py
	
The txt file with the name of 'inbetween' is representing the a place in between the communication of the two nodes

Utilising the hash256 function, keeps the integrity of the command due to tehnical mistake along the way that altered the command

This can be seen when altering the last line of txt file terminal prints error and therefore command is rejected not entering the commandRecorder.txt file.


It should be noted that in the case of an active man in the middle who passes a successful message along with its own hash, the system will not reject the message thus he has the ability to control the receiver!

In order to simulate that scenario we need to open the inbetween.txt file and therefore pass correctly our own message and its digest of hash256 function. 
