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
                # generate list of 4 non-repeating random symbols
				symbol = ['!', '@', '#', '$', '%', '^']
                answer = (random.sample(symbol,4))

                # temp answer list when changes are made
                copy = answer

                # variables to keep track of corrects and wrongs
                countx = 0
                counto = 0
                # empty string to keep track of repeating symbols
                a = ""

                # this checker can also check for repeating random symbols
                # if the length of guesses equal 4
                if len(guess)== 4:
                    # loop through each index
                    for x in range(1, 4):
                        # if the index at guess equals to the index at answer
                        if guess[x] == answer[x]:
                            # increment count for number of X
                            countx += 1
                            # replace match with 'n' in copy to keep track
                            copy[x] = n
                        else:
                            # at the x position in guess, search through answer for O's
                            for i in range(1, 4):
                                # if a symbol match at different locations
                                if guess[x] == copy[i]:
                                    # if symbol is already found or if symbol is an exact match at future index
                                    if copy[i] == a or copy[i] == guess[i]:
                                        pass
                                    else:
                                        # when found, save to empty string
                                        a = guess[x]
                                        counto += 1
                                        copy[i] = m
                else:
                    print "You have entered the wrong number of values"



		conn.close()


if __name__ == '__main__':
	main()