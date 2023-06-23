    #!/usr/bin/env python
    # -*- coding: utf-8 -*-
    
def group_of_study ():
        nr_students = input()
        nr_stu_at_score = input().split(' ')
        min_student, max_student = input.split(' ')
    
        cur = 0
        for cnt, num in enumerate(nr_stu_at_score):
            cur += num
            nr_students -= num
            if (cur >= min_student) and (nr_students <= max_student):
                print cur + 1
                exit
        print '0'
    
    if __name__ == '__main__':
        group_of_study()