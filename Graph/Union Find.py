from random import randint




def main():
    n = 10
    pairs = generate(n)
    print pairs



def generate(n):
    res = set()
    for i in xrange(n):
        first = randint(0, n)
        second = randint(0, n)
        while second == first:
            second = randint(0, n)
        res.add((first, second))
    return res




if __name__ == '__main__':
    main()