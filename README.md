# Python_Mastermind_guesser

Worked on by James Bui and Quyen Mac

This git repository include: mastermind.py and mastermind_user.py

tabulate 0.7.5 was installed and imported onto this project

This game is exactly like the Mastermind game we made for Project 2. The difference is that instead of having the user play against the script that generates the code and checks to see if it is correct, we divide the responsibilities up. There will be a player who will only keep guessing. The player will send his guess to the other person, whose program will generate the code and check to see if it is correct. Both people will connect using socket communication via TCP. 

In terms of networking, mastermind.py will act as the server, while mastermind_user.py is the client. The client will connect to the server with a known IP address and port number ahead of time. 

But for testing purposes, we set it so that whoever is testing this will be able to run it locally on 2 separate terminal windows. 

References we used:

http://www.tutorialspoint.com/python/python_networking.htm

https://docs.python.org/2/library/random.html

http://www.pythonforbeginners.com/basics/list-comprehensions-in-python

https://pypi.python.org/pypi/tabulate

