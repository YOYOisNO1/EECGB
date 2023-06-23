def program624():
    w = input()
    word = ''.join([i if i != 'n' else "*" for i in w]
    
    vowels = "aeiou"
    cons = [word[i-1] + word[i] for i in range(1 , len(word)) if word[i-1] not in vowels]
    con_vow = [i for i in cons if i[-1] in vowels]
    
    if len(cons) == len(con_vow) :
        print("YES")
    else :
        print("NO")