def gather_data():
    n1 = input()
    n2 = input() 
    op = input()

    return n1, n2, op

def main():
    n1, n2, op = gather_data()
    print(eval(n1+op+n2))

    return None

if __name__ == "__main__":
    main()
