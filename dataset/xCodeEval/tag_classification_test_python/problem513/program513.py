def check_word(word_list, word_need):
        unique = []
        for i in range(len(word_list)):
            # Pick each word in the list
            if word_need == 0:
                break
            for j in range(len(word_list[i])):
                if word_need == 0:
                    break
                # Check word without 1 char is in unique
                new_word = word_list[i][:j]+word_list[i][j+1:]
                if new_word not in unique:
                    unique.append(new_word)
                    word_need -= 1
        return unique
    
def check_all():
        cost_sum = 0
        cost_each = 1
        [raw_length, raw_size] = input().split()
        size = int(raw_size)
        words = input().split()
        size -= 1
        while size>0:
            if len(words[0]) == 0:
                return -1
            words = check_word(words, size)
            cost_sum += len(words)*cost_each
            cost_each += 1
            size -= len(words)
        return cost_sum
    
    print(check_all())