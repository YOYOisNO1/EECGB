    class Subject:
    def __init__(self, id, low, high, complexity):
            self.id = id
            self.low = low
            self.high = high
            self.complexity = complexity
            self.day_links = [ {} for i in range(high - low + 1) ]
    
    def add_link(self, link):
            days = link.days
            links = self.day_links[link.weight - self.low]
            if days not in links or links[days].total < link.total:
                links[days] = link
    
    class Link:
    def __init__(self, subject, weight, total, days, previous):
            self.subject = subject
            self.weight = weight
            self.total = total
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
    
    best_link = None
    
    for pos, group in enumerate(groups):
        if num_groups - pos >= need_days:
            for subject in group.subjects:
                for weight in range(subject.low, subject.high + 1):
                    subject.add_link(Link(subject, weight, weight, 1, None))
        for subject in group.subjects:
            for i, links in enumerate(subject.day_links):
                weight = subject.low + i
                for days, link in links.items():
                    if days == need_days:
                        if not best_link or best_link.total < link.total:
                            best_link = link
                        continue
                    for next_weight in [ weight + more, weight * more ]:
                        max_pos = num_groups + days - need_days
                        for next_pos in range(pos + 1, max_pos + 1):
                            for next_subject in groups[next_pos].subjects:
                                if next_weight < next_subject.low:
                                    continue
                                if next_weight > next_subject.high:
                                    continue
                                next_subject.add_link(Link(
                                    next_subject, next_weight,
                                    next_weight + link.total, days + 1, link))
    
    if best_link:
        print('YES')
        schedule = need_days * [ None ]
        link = best_link
        while link:
            subject = link.subject
            subject.weight = link.weight
            schedule[link.days - 1] = subject
            link = link.previous
        for subject in schedule:
            print(subject.id, subject.weight)
        import sys
        sys.exit()
    else:
        print('NO')