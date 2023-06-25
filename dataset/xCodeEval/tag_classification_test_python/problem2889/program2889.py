def program2889():
    import re
    n = input()
    print(next(filter(re.compile(input() + '$').match, ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"])))