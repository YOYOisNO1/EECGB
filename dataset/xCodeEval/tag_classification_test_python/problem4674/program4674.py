    import sys
    input = sys.stdin.readline
    
    """ Interval intersection """
    
def main():
      n, k = map(int, input().split())
      guests = input().rstrip()
      guestbook = {}
      for idx, guest in enumerate(guests):
        if guest not in guestbook:
          guestbook[guest] = (idx, idx)
        else:
          val = guestbook[guest]
          guestbook[guest] = (val[0], idx)
    
      timeline = [0]*n
      for timings in guestbook.values():
        for idx in range(timings[0], timings[1]+1):
          timeline[idx] += 1
    
      print("YES") if max(timeline) > k else print("NO")
    
    if __name__ == "__main__":
      main()