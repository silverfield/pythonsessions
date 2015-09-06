__author__ = 'ferrard'


def main(argv):
    start = int(argv[0])
    end = int(argv[1])
    if start == 5:
        import time
        time.sleep(1)
    print((end - start + 1)*(start + end)//2)

if __name__ == '__main__':
    import sys
    main(sys.argv[1:])
