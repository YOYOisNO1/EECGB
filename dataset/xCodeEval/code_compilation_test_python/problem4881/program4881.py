    class Subject:
    def __init__(self, id, low, high, complexity):
            self.id = id
            self.low = low
            self.high = high
            self.complexity = complexity
            self.links = (high - low + 1) * [ None ]
    
    def add_link(self, weight, new_link):
            link = self.links[weight - self.low]
            if link == None or link.days < new_link.days:
                self.links[weight - self.low] = new_link
    
    def __str__(self):
            return '[%d [%d, %d] %d]' % (self.id,
                    self.low, self.high, self.complexity)
    
    class Link:
    def __init__(self, subject, weight, days, previous):
            self.subject = subject
            self.weight = weight
            self.days = days
            self.previous = previous
    
    class Group:
    def __init__(self, complexity):
            self.complexity = complexity
            self.subjects = []
    
    need_days, num_subjects, more = map(int, input().split())
    groups = {}
    for i in range(num_subjects):
        subject = Subject(i + 1, *list(map(int, input().split())))
        if subject.complexity not in groups:
            groups[subject.complexity] = Group(subject.complexity)
        groups[subject.complexity].subjects.append(subject)
    groups = sorted(groups.values(), key = lambda group: group.complexity)
    num_groups = len(groups)
    
def win(link):
        print('YES')
        schedule = need_days * [ None ]
        while link:
            subject = link.subject
            subject.weight = link.weight
            schedule[link.days - 1] = subject
            link = link.previous
        for subject in schedule:
            print(subject.id, subject.weight)
        import sys
        sys.exit()
    
    for pos, group in enumerate(groups):
        #print(pos, '', '  '.join(map(str, group.subjects)))
        if num_groups - pos >= need_days:
            for subject in group.subjects:
                for weight in range(subject.low, subject.high + 1):
                    subject.add_link(weight, Link(subject, weight, 1, None))
                    #print(pos, weight, 1)
        for subject in group.subjects:
            for i, link in enumerate(subject.links):
                if link == None:
                    continue
                if link.days == need_days:
                    win(link)
                weight = subject.low + i
                for next_weight in [ weight + more, weight * more ]:
                    max_pos = num_groups + link.days - need_days
                    for next_pos in range(pos + 1, max_pos + 1):
                        for next_subject in groups[next_pos].subjects:
                            if next_weight < next_subject.low:
                                continue
                            if next_weight > next_subject.high:
                                continue
                            next_subject.add_link(next_weight, Link(
                                next_subject, next_weight, link.days + 1, link))
                            #print(next_pos, next_weight, link.days + 1)
    
    print('NO')