#!/usr/bin/python

# Authors: James Bui and Quyen Mac
# Modified: December 9, 2015
# Project Name: Mastermind in Python
# File name: mastermind_user.py [user/client]

import socket
import sys
import pickle
from tabulate import tabulate

def main():
	# If we want to connect to different server, we would just 
	# set, for example, host = '192.168.1.32'
	host = socket.gethostname() 	# Gets local host information
	port = 9009		# Port number is arbitrary as long as it matches the server's port
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# Create a socket
	s.connect((host, port))		# Connect to the server
	count = 0
	while (count < 10):
		guess = raw_input("Please enter your guess: ")	# Accept command line input
		s.send(guess) 			# Send your guess through the socket via TCP 
		data_recv = s.recv(1024)	# Get data back from the server
		if data_recv == 'Yay you win!':
			print data_recv
			break
		else:
			data_matrix = pickle.loads(data_recv)	#deserialize the data back into a list
			#print data_recv
			print tabulate(data_matrix, headers=["G","u","e","s","s","C","l","u","e"],
				tablefmt="simple")
			count += 1 		# Increment to next round 

	# Outside while loop
	if count == 10:
		print "Sorry you lose!"

if __name__ == '__main__':
	main()