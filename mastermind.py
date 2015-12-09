import socket
import random
import string

def random_gen(repeat):
    symbol = ['!', '@', '#', '$', '%', '^']
    if repeat:
        # generate list of 4 repeating random symbols
        answer = [symbol[random.randint(0,4)] for i in range(4)]
    else:
        # 4 non repeating random symbols
        answer = (random.sample(symbol,4))
    return answer

def check_symbol(guess):
    valid = True
    for x in range(4):
        if guess[x] not in '!@#$%^':
            valid = False
    return valid

def checker():
    # this checker can also check for repeating random symbols

    # variables to keep track of corrects and wrongs
    countx = 0
    counto = 0
    # empty string to keep track of repeating symbols
    a = ""

    # loop through each index
    for x in range(4):
        # if the index at guess equals to the index at answer
        if guess[x] == answer[x]:
            # increment count for number of X
            countx += 1
            # replace match with 'n' in copy to keep track
            copy[x] = n
        else:
            # at the x position in guess, search through answer for O's
            for i in range(4):
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
                # need to get repeat Y/N from user
                answer = random_gen(repeat)
                copy = answer

                # if the length of guesses equal 4
                if len(guess)== 4:
                    # if input is valid
                    if check_symbol(guess):
                        # keep track of amount of tries
                        count += 1
                        # call checker
                        checker(copy)

                        # print table somewhere here
                        # if there are 4 X's
                        if countx == 4:
                            win = True
                        else:
                            print "You have attempted %d/10 tries." % count
                    else:
                        print "One or more symbols is invalid."

                else:
                    print "You have entered the wrong number of values."



		conn.close()


if __name__ == '__main__':
	main()