def program1389():
    months = [ 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    month = input()
    idx = months.index(month)
    tonext = (int(input()) + idx )% 12
    print(months[tonext])