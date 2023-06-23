    def calc_max(a, b, ab):
            # full pattern 'fp' ocurres at least once or more "b ab a" = 4 chars
            fp = min(a, b, ab)  # how many fps we have
            a, b, ab = map(lambda x: x-fp, (a, b, ab))  # update strings removing fp
            count = fp * 4
         
            # now we're left with at least one string or more as zero:
            # if it's 'ab' then we have unlimited chances of:
            # a-b ( +1 if result isn't zero)
            if ab == 0:
                count += min(a, b) * 2
                if a != b:
                    count += 1
                return count
         
            # add the rest of 'ab'
            count += ab * 2
            # if both 'a', 'b' are zero we're done:
            if a == b:
                return count
    
            # else then one of 'a' or 'b' left we can have one of it
            return count + 1
         
         
        if __name__ == "__main__":
            a, b, ab = map(int, input().split())
            print(calc_max(a, b, ab))