def main():
  import os
  global b
  def cls():
      os.system('cls' if os.name=='nt' else 'clear')

  b = int(input("how big do you want the board: "))

  col_sto = []
  ls_turn = []
  players = ['x','o']
  board = []
  turn_count = 0
  for x in range(0, b):
      for x in range(0, b):
          board.append("-")
  game_active = True
  while game_active == True:
      test = int(input(":")) - 1
      ls_turn.append(test)
      while len(ls_turn) != len(set(ls_turn)):
        ls_turn = list(dict.fromkeys(ls_turn))
        test = int(input(" :"))-1
        ls_turn.append(test)
      board[test] = players[0]

      global ls
      ls = [board[x:x + b] for x in range(0, len(board), b)]
      test_ls = [board[x:x + b] for x in range(0, len(board), b)]

      def display():
          for i in ls:
              print(i)
      cls()
      display()

      def end_game():
        global game_active
        wld = input("would you like to play again[y/n]: ")
        if wld == "y":
         main()
        else: 
         quit()

      def row_allcheck():
          global winner
          for x in range(0, b):

              if all(x == ls[0][0] for x in ls[0]):
                  #print("All elements in list are equal")
                  winner = ls[0][0]
                  if winner == '-':
                      None
                  if winner == 'x' or 'o':
                      return winner
                  
              #else:
              #print("All elements in list are not equal")
              del ls[0]
          #print(winner)

      def col_allcheck():
        global winner
        global col_sto
        col_sto = []
        ls = [board[x:x+b] for x in range(0, len(board),b)]
        global loop1
        global loop2
        loop1 = 0
        loop2 = 0
        #col
      
        def  col_check(loop1):
            for x in range(0,b):
             del ls[0+loop1][1:b]
             if loop1 < b-1:
              loop1 = loop1 +1
      
            return(ls)
        def col_rotate(loop2):
          global winner
          for x in range(0,b):
           del ls[loop2][0]
           loop2 = loop2 + 1
           return(ls)

        colcheck = []
        col = 0
        for x in range(0,b):

          for x in range(0,col):
           ls = col_rotate(loop2)
        
      

      
          colcheck = [tuple(lst) for lst in ls]
          
          if(len(set(colcheck))==1):
          #print("col_All elements in list are the same")
           winner = colcheck[0][0]
           if winner == '-':
            None

          
           if winner == 'o' or 'x':
             return winner
          #else:
            #print("col_All elements in list are not same")
        
      
          ls = [board[x:x+b] for x in range(0, len(board),b)]
          if col < b:
            col = col + 1

      def dia_allcheck():
          global winner
          ls = [board[x:x + b] for x in range(0, len(board), b)]
          #dia check 1
          #print("dia")
          dia = 0
          dia1 = []
          for x in range(0, b):
              dia1.append(ls[dia][dia])
              if dia < b:
                  dia = dia + 1
          #print(dia1)
          if (len(set(dia1)) == 1):
              #print("All elements in list are same")
              winner = dia1[0]
              if winner == '-':
                  None
              if winner == 'o' or 'x':
                  return winner
              
              #print(winner)
          #else:
          #print("All elements in list are not same")

          ls = [board[x:x + b] for x in range(0, len(board), b)]
          #dia check 2
          #print("dia2")
          dia2 = []
          dia = 0
          for x in range(0, b):
              dia2.append(ls[dia][b - dia - 1])
              if dia < b:
                  dia = dia + 1
          #print(dia2)
          if (len(set(dia2)) == 1):
              #print("All elements in list are same")
              winner = dia2[0]
              #print(winner)
          #else:
          #print("All elements in list are not same")

      row_allcheck()
      col_allcheck()
      dia_allcheck()
      players.reverse()
      if winner == 'o' or winner == 'x':
          print(winner + " wins the game")
          end_game()

      turn_count = turn_count + 1
      if turn_count == b*b:
        if winner != 'x' and winner != 'o':
         print("looks like a tie")
         end_game()

main()    
