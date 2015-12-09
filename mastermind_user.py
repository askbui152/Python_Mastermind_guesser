#!/usr/bin/python

import socket
import sys

def main():
	# If we want to connect to different server, we would just 
	# set, for example, host = '192.168.1.32'
	host = socket.gethostname() 	# Gets local host information
	port = 9004		# Port number is arbitrary as long as it matches the server's port
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	# Create a socket
	s.connect((host, port))		# Connect to the server
	count = 0
	while (count < 10):
		guess = raw_input("Please enter your guess: ")	# Accept command line input
		s.send(guess) 			# Send your guess through the socket via TCP 
		data_recv = s.recv(1024)	# Get data back from the server
		print data_recv
		if data_recv == 'Yay you win!':
			break
		count += 1
	if count == 10:
		print "Sorry you lose!"

if __name__ == '__main__':
	main()