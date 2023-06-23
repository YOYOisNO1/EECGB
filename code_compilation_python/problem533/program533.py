def codeforce(animal):
        animal=list(set(animal))
        if len(animal)==2:
            print 'Elephant'
        elif len(animal)==3:
            print 'Bear'
        else:
            print 'Alien'
    
    if __name__=='__main__':
        animal=input().split()
        
        codeforce(animal）