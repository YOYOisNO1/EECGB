    import sys
    
def main():
        for a in sys.argv:
            print(a)
        cha_count = 0
        seq_start = 0
        for i in range(1, len(dna)):
            if dna[i-1] != dna[i] or i == len(dna) - 1:
                if (i - seq_start)%2 == 0:
                    cha_count += 1
                    seq_start = i
        print(cha_count)
        return 0
    main()