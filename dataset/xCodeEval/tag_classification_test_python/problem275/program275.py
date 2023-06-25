def program275():
    from datetime import *
    print(abs((datetime.strptime(input(),) "%Y:%m:%d")-datetime.strptime(input(), "%Y:%m:%d")).days)