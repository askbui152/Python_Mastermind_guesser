# Python_Mastermind_guesser

Worked on my James Bui
Partner is Quyen Mac

This game is exactly like the Mastermind game we made for Project 2. The difference is that instead of having the user play against the script that generates the code and checks to see if it is correct, we divide the responsibilities up. There will be a player who will only keep guessing. The player will send his guess to the other person, whose program will generate the code and check to see if it is correct. Both people will connect using socket communication via TCP. 