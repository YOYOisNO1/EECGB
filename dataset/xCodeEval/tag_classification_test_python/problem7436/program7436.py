    import string
    
    class Position:
  def __init__(self, r, c):
        self.r = r
        self.c = c
    
def s_to_position(s):
      letter, number = s[0], s[1]
      return Position(string.ascii_letters.index(letter), int(number) - 1)
    
def finish(message):
      print(message)
      import sys; sys.exit()
    
def king_attacks(attacker, defender):
      for dr in range(-1, 2):
        r = attacker.r + dr
        for dc in range(-1, 2):
          c = attacker.c + dc
          if r == defender.r and c == defender.c:
            return True
      return False
    
def rook_attacks(attacker, defender, blockers=[]):
      if attacker.r == defender.r and attacker.c == defender.c:
        return False
      if attacker.r == defender.r:
        blocked = False
        for blocker in blockers:
          if blocker.r == attacker.r:
            if attacker.c < blocker.c and blocker.c < defender.c:
              blocked = True
            if defender.c < blocker.c and blocker.c < attacker.c:
              blocked = True
        if not blocked:
          return True
      if attacker.c == defender.c:
        blocked = False
        for blocker in blockers:
          if blocker.c == attacker.c:
            if attacker.r < blocker.r and blocker.r < defender.r:
              blocked = True
            if defender.r < blocker.r and blocker.r < attacker.r:
              blocked = True
        if not blocked:
          return True
      return False
    
    rook_a, rook_b, king_white, king_black = map(s_to_position, input().split())
    
    for dr in range(-1, 2):
      r = king_black.r + dr
      for dc in range(-1, 2):
        c = king_black.c + dc
        if r < 0 or r > 7 or c < 0 or c > 7:
          continue
        current_king = Position(r, c)
        if king_attacks(king_white, current_king):
          #print('king attacks %d, %d' % (r, c))
          continue
        if rook_attacks(rook_a, current_king, [king_white]):
          #print('rook A attacks %d, %d' % (r, c))
          continue
        if rook_attacks(rook_b, current_king, [king_white]):
          #print('rook B attacks %d, %d' % (r, c))
          continue
        #print('%d, %d is safe' % (r, c))
        finish('OTHER')
    
    finish('CHECKMATE')