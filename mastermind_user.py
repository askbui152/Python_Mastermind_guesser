import socket
import sys
import argparse

def send_guess(TCP_IP, TCP_PORT, guess):
	count = 0
	win = False
	while (count < 0) or (win == False):
		parser = argparse.ArgumentParser()



def main():
	#this is main
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	s.send(guess)

	parser = argparse.ArgumentParser()
	parser.add_argument('-c', action='store', dest='code', help='My Guess')
	results = parser.parse_args()
	guess = results.code



if __name__ == '__main__':
	main()