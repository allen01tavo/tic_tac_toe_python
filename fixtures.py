"""
Python Version 3.9.1
@autor: Gus Maturana
"""
import logging
import random


class myGame:


	def __init__(self, title = ""):
		self._title = title
		self._matrix = [['','',''],['','',''],['','','']]

	# Returns the matrix array
	def get_matrix(self):
		return self._matrix

	# Returns the tile of the game
	def get_tile(self):
		return self._title

	# Adding value to a matrix cell
	def matrix (self, val, position):

		row = 10
		col = 10

		if position == 1:
			row = 0
			col = 0
		if position == 2:
			row = 0
			col = 1
		if position == 3:
			row = 0
			col = 2
		if position == 4:
			row = 1
			col = 0
		if position == 5:
			row = 1
			col = 1
		if position == 6:
			row = 1
			col = 2
		if position == 7:
			row = 2
			col = 0
		if position == 8:
			row = 2
			col = 1
		if position == 9:
			row = 2
			col = 2
		self._matrix[row][col]=val

		return self._matrix

	# Returns true if there is a winner
	def win_(self, _matrix):

		if(self.x_wins(_matrix)):
			print("X wins!")
			return True
		if(self.o_wins(_matrix)):
			print("O wins!")
			print("Computer Rules!")
			return True
		else:
			False

	def x_wins(self, _matrix):
		# first row X
		if((_matrix[0][0] == 'X') and (_matrix[0][1] == 'X') and (_matrix[0][2] == 'X')):
			return True
		#second row X
		if((_matrix[1][0] == 'X') and (_matrix[1][1] == 'X') and (_matrix[1][2] == 'X')):
			return True
		#thrid row X
		if((_matrix[2][0] == 'X') and (_matrix[2][1] == 'X') and (_matrix[2][2] == 'X')):
			return True
		#first column X
		if((_matrix[0][0] == 'X') and (_matrix[1][0] == 'X') and (_matrix[2][0] == 'X')):
			return True
		#second column X
		if((_matrix[0][1] == 'X') and (_matrix[1][1] == 'X') and (_matrix[2][1] == 'X')):
			return True
		#third column X
		if((_matrix[0][2] == 'X') and (_matrix[1][2] == 'X') and (_matrix[2][2] == 'X')):
			return True
		#first diagonal X
		if((_matrix[0][0] == 'X') and (_matrix[1][1] == 'X') and (_matrix[2][2] == 'X')):
			return True
		#second diagonal X
		if((_matrix[0][2] == 'X') and (_matrix[1][1] == 'X') and (_matrix[2][0] == 'X')):
			return True

	def o_wins(self, _matrix):
				# first row O
		if((_matrix[0][0] == 'O') and (_matrix[0][1] == 'O') and (_matrix[0][2] == 'O')):
			return True
		#second row O
		if((_matrix[1][0] == 'O') and (_matrix[1][1] == 'O') and (_matrix[1][2] == 'O')):
			return True
		#thrid row O
		if((_matrix[2][0] == 'O') and (_matrix[2][1] == 'O') and (_matrix[2][2] == 'O')):
			return True
		#first column O
		if((_matrix[0][0] == 'O') and (_matrix[1][0] == 'O') and (_matrix[2][0] == 'O')):
			return True
		#second column O
		if((_matrix[0][1] == 'O') and (_matrix[1][1] == 'O') and (_matrix[2][1] == 'O')):
			return True
		#third column O
		if((_matrix[0][2] == 'O') and (_matrix[1][2] == 'O') and (_matrix[2][2] == 'O')):
			return True
		#first diagonal O
		if((_matrix[0][0] == 'O') and (_matrix[1][1] == 'O') and (_matrix[2][2] == 'O')):
			return True
		#second diagonal O
		if((_matrix[0][2] == 'O') and (_matrix[1][1] == 'O') and (_matrix[2][0] == 'O')):
			return True

	# Prints all values stored in the matrix
	def print_matrix(self, _matrix):
		for i in _matrix:
			for d in i:
				print(f"[{d}]", end = " ")
			print()

	# Returns true if location is empty in the matrix
	def game_logic(self, _matrix, location):

		self._location = location
		cnt = 0

		for i in _matrix:
			for val in i:
				cnt = cnt + 1
				if (cnt == self._location):
					if (val == ''):
						return True
					else:
						return False

	# This function provides an status of the games
	def refresh(self):
		print("Games Status")
		self.print_matrix(self.get_matrix())

	# Another implementation of location matrix
	def entervalue(self, val, location):
		cnt = 0
		for i in range(0,3):
			for j in range(0,3):
				cnt = cnt + 1
				if cnt == location:
					self._matrix[i][j] = val
				else:
					continue
		return self._matrix

	# computer slects a position an places an 'O'
	def computer_selection(self):
		cnt = 0				#counter
		self._list = []		#creates a list

		#appends the list with all the emtpy locations
		for i in range(0,3):
			for j in range(0,3):
				cnt = cnt + 1
				if (self._matrix[i][j] ==''):
					self._list.append(cnt)
				else:
					continue

		n = random.randint(0,len(self._list)-1)

		# if middle location is availabe place O in it
		if (self.game_logic(self.get_matrix(), 5)):
			self.entervalue('O',5)
		# if there is an empty corner, computer places an 'O' on the empty corner
		elif ((self._list[n]==1) or (self._list[n]==3) or (self._list[n]==7) or (self._list[n]==9)):
			self.entervalue('O', self._list[n])
		else:
			self.entervalue('O', self._list[n])
			
		print(f"Computer played location {self._list[n]}:")
		self.refresh()

	# Function asks for user input (Recursive function)
	def get_input(self):

		try:
			self._location = int(input("Enter a location: "))
		except ValueError:
			print("Sorry, I din't undertand that. Try again: ")
			return self.get_input()

		if self._location > 9 or self._location < 1:
			print("Input is out of range type a number between 1 and 9. Try again: ")
			return self.get_input()

		if not self.game_logic(self.get_matrix(),self._location):
			print("Location is already being used. Try again: ")
			return self.get_input()
		else:
			return self._location

	# Function check if the matix is full for a tie
	def full_matrix(self, _matrix):
		cnt = 0
		for i in range (1, 9):
			if self.game_logic(_matrix, i) == False:
				cnt += 1
			else:
				continue
		if cnt == 9:
			return True
		else:
			return False

	def mim_max(self, ):
		state = self.get_matrix()

# End of myGame class

def main():

	logging.info("Starting Game")
	my = myGame("Tic Tac Toe")

	print(my.get_tile())
	my.refresh()
	
	while True:

		# getting input from the user
		location = my.get_input()

		# user's turn 		
		my.entervalue('X', int(location))
		my.refresh()

		# in case the user wins
		if my.win_(my.get_matrix()) == True:
			print("--------GAME OVER-----------")
			break

		# if it is a tie
		if my.full_matrix(my.get_matrix()):
			print ("It is a tie")
			break

		# computer's turn
		my.computer_selection()
		if my.win_(my.get_matrix()) == True:
			print("--------GAME OVER-----------")
			break


if __name__ == '__main__':

	main()
