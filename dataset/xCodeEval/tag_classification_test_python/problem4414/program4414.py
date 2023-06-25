def main():
        desc = input()
        chunk = desc[1:-1]
        chunk = chunk.replace("at", "@", 1)
        chunk = chunk.replace("dot", ".")
        print(desc[0] + chunk + desc[-1])
    main()