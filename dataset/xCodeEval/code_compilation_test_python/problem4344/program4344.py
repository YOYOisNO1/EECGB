    #!/usr/bin/python     
    import sys
    
def main():
      lines = sys.stdin.readlines()
      a, b, m = map(int, lines.pop(0).split(' '))
      vx, vy, vz = map(int, lines.pop(0).split(' '))
      #print "dimensions of room: (" + str(a) + ", 0, " + str(b) + ")"
      #print "distance away: " + str(m)
      #print vx, vy, vz
      coordinates = (a/2.0, m, 0)
      steps = -1*m/float(vy)
      x_move = (steps*vx)%(2*a)
      z_move = (steps*vz)%(2*b)
      #print "x movement: " + str(x_move)
      #print "y movement: " + str(z_move)
      final_x = 0
      final_z = 0
      if x_move > a:
      	#print "x move is larger than dim"
      	x_move = x_move % a
      	final_x = a/2.0 + (a-x_move)
      else:
      	final_x = a/2.0 + x_move
    
      if z_move > b:
      	#print "z move is larger than dim"
      	z_move = z_move % b
      	final_z = (b-z_move)
      else:
      	final_z = z_move
    
      #while coordinates[1]
    
      print str(final_x) + " " + str(final_z)
    
      return
    
    if __name__ == "__main__":
      main()