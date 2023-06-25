def program2875():
    if __name__ == "__main__":
        pass = input()
        digs = {}
        for i in range(10):
            digs[input()] = i
        print ''.join(str(digs[pass[i*10:(i+1)*10]]) for i in range(8))