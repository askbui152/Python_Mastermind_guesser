import socket
import random
import string


def main():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
	port = 9000
	s.bind((host, port))

	s.listen(10)
	count = 0
	win = False
	while True:
		conn, addr = s.accept()
		print 'Connecting with ', addr
		if (count < 10) or (win = True):
			break
		else:
			guess = conn.recv(1024)
			if not guess:
				pass
			else:
                # generate list of random symbols
				symbol = ['!', '@', '#', '$', '%', '^']
                combination = (random.sample(symbol,4))

                


		conn.close()


if __name__ == '__main__':
	main()