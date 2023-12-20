def gather_data():
    n1 = int(input())
    n2 = int(input())

    return n1, n2

def print_msg(n1, n2):
    print(f'{n1} + {n2} = {n1+n2}')
    return None

def main():
    n1, n2 = gather_data()

    print_msg(n1, n2)
    return None

if __name__ == "__main__":
    main()
