    #!/usr/bin/python3.6
    
    '''
            .__     .__                                _______   _______ _________
      ______|  |__  |__|  ____    ____ _______ _____   \   _  \  \   _  \\______  \
     /  ___/|  |  \ |  | /    \  /  _ \\_  __ \\__  \  /  /_\  \ /  /_\  \   /    /
     \___ \ |   Y  \|  ||   |  \(  <_> )|  | \/ / __ \_\  \_/   \\  \_/   \ /    /
    /____  >|___|  /|__||___|  / \____/ |__|   (____  / \_____  / \_____  //____/
         \/      \/          \/                     \/        \/        \/
    
    '''
    # Run locally with python3.6 -O code.py to run in not debug mode. [ONLINE_JUDGE]
    # rm ~/pipe2; mkfifo ~/pipe2 ; ./code.py < ~/pipe2 | ./interactive.py > ~/pipe2
    # rm ~/pipe2; mkfifo ~/pipe2 ; ./code.py < ~/pipe2 | ./matcher.py > ~/pipe2
    
    # one-way
    # ./haha.py > input.txt ; ./code.py < input.txt
    
    import sys
    
def eprint(*args, **kwargs):
        if __debug__:
            print(*args, file=sys.stderr, **kwargs)    
    
def calculate_res(visit, n):
        return n*len(visit) - sum([len(x) for x in visit])
    
def traverse(s, k):
        _que = []
        visit = set([])
    
        _que.append(s)
        visit.add(s)
        if len(visit) == k:
            return calculate_res(visit, len(s))
    
        while len(_que) > 0:
            cur = _que.pop(0)
            for i in range(len(cur)):
                adj_s = cur[0:i] + cur[i+1:len(cur)]
                if adj_s not in visit:
                    _que.append(adj_s)
                    visit.add(adj_s)
                    if len(visit) == k:
                        return calculate_res(visit, len(s))
        return -1
    
    
    if __name__ == "__main__":
        n, k = map(int, input().split(' '))
        s = input()
    
        print(traverse(s, k))
    