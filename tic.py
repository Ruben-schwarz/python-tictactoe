import os
def cls():
	os.system('cls' if os.name=="nt" else 'clear')

class Main:
	def __init__(self , input_size):
		self.active = True
		self.players = ['x' , 'o']
		self.board = []
		self.divided_board_array = None
		self.size = input_size 
	def init_board(self):
		for x in range(0 , (self.size) ** 2):
			self.board.append("-")
	
	def display(self): 
		self.divided_board_array = [self.board[x:x + self.size] for x in range(0, (self.size) **2, self.size)]
		for i in self.divided_board_array:
			print(i)
	
	def player_turn(self):
		turn = int(input(": ")) - 1
		if (self.board[turn] =="-"): 
			self.board[turn] = self.players[0]
		else:
			cls()
			self.display()
			print("that space is already taken, player: (" + self.players[0] + ") pick a different space")
			self.player_turn()
	
	def col_check(self):
		for j in range(0 , self.size):
			row = []
			for i in self.divided_board_array:
				row.append(i[j])
			if(len(set(row))==1):
				if (row[0] == "-"):
					return False
				else:
					return True
			else:
				return False
	def row_check(self):
		for i in self.divided_board_array:
			if(len(set(i))==1):
				if (i[0] == "-"):
					return False
				else:
					return True
			else:
				return False
	def dia_check(self):
		def check_fn(index , tf):
			ls = []
			for i in range(0 , self.size):
				ls.append(self.board[index])
				if (tf):
					index += self.size +1
				else:
					index += self.size -1
			if (len(set(ls)) == 1):
				if(ls[0] == "-"):
					return	False
				else:
					return True
			else:
				return False

		if(check_fn(self.size - 1 , False) or check_fn(0 , True)):
			return True
		else:
			return False
		
inp = int(input("How big do you want the board?: "))
game = Main(inp)

game.init_board()
cls()
game.display()
while game.active:
	game.player_turn()
	cls()
	game.display()
	if (game.dia_check() or game.col_check() or game.row_check()):
		game.active = False
		print("winner : " + game.players[0])
	game.players.reverse()