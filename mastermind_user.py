import socket
import sys

def main():
	TCP_IP = ''
	TCP_PORT = 9000
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	count = 0
	win = False
	while (count < 0) or (win == False):
		guess = raw_input("Please enter your guess:")
		#print "You entered: "
		data_recv = s.recv(1024)
		print data_recv
		if data_recv == guess:
			win = True
		count += 1
	if count == 10:
		print "Sorry you lose!"

if __name__ == '__main__':
	main()