import socket
import random
import string

def print_results(combine, matrix, row):
    for x in range(8):
        matrix[row][x+1] = combine[x]
    return matrix

def random_gen(repeat):
	symbol = ['!', '@', '#', '$', '%', '^']
	if repeat:
		answer = [symbol[random.randint(0,4)] for i in range(4)]
	else:
		answer = (random.sample(symbol,4))
	return answer

def check_symbol(guess):
	valid = True
	for x in range(4):
		if guess[x] not in '!@#$%^':
			value = False
	return valid

def toXandO(table):
	for i in range(4):
		if table[i] == 0:
			table[i] = ' '
		elif table[i] == 1:
			table[i] = 'O'
		elif table[i] == 2:
			table[i] = 'X'
	return table

def bubblesort(table):
	length = len(table) - 1
	sort = False
	temp = 0
	while not sort:
		sort = True
		for i in range(length):
			if table[i] < table[i+1]:
				temp = table[i]
				table[i] = table[i+1]
				table[i+1] = temp
				sort = False
	return table
def checker(guess, answer):
	countx = 0
	counto = 0

	a = ''
	copy = list(answer)
	for x in range(4):
		if guess[x] == answer[x]:
			countx += 1
			copy[x] = 'n'
		else:
			for i in range(4):
				if guess[x] == copy[i]:
					if copy[i] == a or copy[i] == guess[i]:
						pass
					else:
						a = guess[x]
						counto += 1
						copy[i] = 'm'
	newcopy = [0,0,0,0]
	for i in range(4):
		if copy[i] == 'n':
			newcopy[i] = 2
		elif copy[i] == 'm':
			newcopy[i] = 1
		else:
			newcopy[i] = 0
	return newcopy
def use_sockets():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	host = socket.gethostname()
	port = 9004				#this is arbitrary
	s.bind((host,port))
	s.listen(10)
	return s

def main():
	new_socket = use_sockets() #made changes here
	repeat = False
	code = random_gen(repeat)
	print code
	count = 0
	win = False

	tries = 10

	# create matrix to display results
	matrix = [[]]
	matrix = [[0 for i in xrange(9)] for i in xrange(tries)]
    for x in range(tries):
        matrix[x][0] = x + 1

    for i in range(tries):
            for o in range(1,9):
                    matrix[i][o] = ""

    row = 0

	conn, addr = new_socket.accept()
	while (count < 10):
		#guess = raw_input("Pleaase enter your guess: ")
		#conn, addr = new_socket.accept()
		guess = conn.recv(1024)
		#check here
		print guess
		check = check_symbol(guess)
		if check == True:
			checker_table = checker(guess, code)
			newChecker_table = bubblesort(checker_table)
			printChecker_table = toXandO(newChecker_table)

			# combine guesses and clues in one list
			combined = guesslist + printChecker_table
            print_results(combined, matrix, row)
            print tabulate(matrix, headers=["G","u","e","s", "s", "C", "l", "u", "e"],tablefmt="simple")

            row += 1

			#print printChecker_table
			if printChecker_table == ['X','X','X','X']:
				conn.send('Yay you win!')
				break
			else:
				conn.send(''.join(printChecker_table))
		else:
			conn.send('Incorrect input')


		count += 1
	conn.close()
	if count == 10:
		conn.send('Sorry you lose!')

if __name__ == '__main__':
	main()