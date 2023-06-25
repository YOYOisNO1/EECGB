    #!/usr/bin/env python3 
    
    import itertools
    
    class Solitaire:
  def __init__(self):
        # Read inputs
        (self.n,self.m) = map(int,input().split())
        self.table = [input().split() for i in range(self.n)]
    
        # Determine the unused cards and the positions of the jokers
        ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]
        suits = ["C", "D", "H", "S"]
        deck = set(("%s%s" % card) for card in itertools.product(ranks,suits))
        self.J1_position = None
        self.J2_position = None
    
        for (r,c) in itertools.product(range(self.n), range(self.m)):
          card = self.table[r][c]
          deck.discard(card)
          if (card == "J1"):
            self.J1_position = (r,c)
          elif (card == "J2"):
            self.J2_position = (r,c)
    
        self.unused_cards = list(deck)
        self.unused_cards.sort() # Sort to make things deterministic (easier for testing)
    
  def is_solved_square(self, r, c):
        cards = [self.table[r+ro][c+co] for (ro, co) in itertools.product(range(3), range(3))]
        suits = set(card[1] for card in cards)
        ranks = set(card[0] for card in cards)
        solved = (len(suits) == 1) or (len(ranks) == 9)
        return solved
    
  def is_solved(self):
        all_positions = itertools.product(range(self.n-2), range(self.m-2))
        all_solved_squares = [(r,c) for (r,c) in all_positions if self.is_solved_square(r,c)]
        for ((r1, c1), (r2,c2)) in itertools.combinations(all_solved_squares, 2):
          if (abs(r1-r2) >= 3) or (abs(c1-c2) >= 3):
            return ((r1,c1),(r2,c2))
        return None
    
  def replace_card(self, position, card):
        (r,c) = position
        self.table[r][c] = card
    
  def print_solution(self, joker_line, solution):
        if (solution == None):
          print("No solution.")
        else:
          ((r1,c1),(r2,c2)) = solution
          print("Solution exists.")
          print(joker_line)
          print("Put the first square to (%d, %d)." % (r1+1,c1+1))
          print("Put the second square to (%d, %d)." % (r2+1,c2+1))
        exit()
    
    
  def solve(self):
        if (self.J1_position != None) and (self.J2_position != None):
          for (replacement1, replacement2) in itertools.permutations(self.unused_cards,2):
            self.replace_card(self.J1_position, replacement1)
            self.replace_card(self.J2_position, replacement2)
            solution = self.is_solved()
            if (solution):
              self.print_solution("Replace J1 with %s and J2 with %s." % (replacement1, replacement2), solution)
        elif (self.J1_position != None):
          for replacement in self.unused_cards:
            self.replace_card(self.J1_position, replacement)
            solution = self.is_solved()
            if (solution):
              self.print_solution("Replace J1 with %s." % replacement, solution)
        elif (self.J2_position != None):
          for replacement in self.unused_cards:
            self.replace_card(self.J2_position, replacement)
            solution = self.is_solved()
            if (solution):
              self.print_solution("Replace J2 with %s." % replacement, solution)
        else:
          solution = self.is_solved()
          self.print_solution("There are no jokers.", solution)
        self.print_solution("", None)
    
    Solitaire().solve()
    