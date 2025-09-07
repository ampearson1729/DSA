import sys

def reverseCollatz(k: int, x: int) -> int:
    return x*2**k

def main():
    # read first line
    n = int(sys.stdin.readline())
    for line in sys.stdin:   # keeps reading until EOF
        kx = line.strip().split()
        print(reverseCollatz(int(kx[0]),int(kx[1])))

if __name__ == "__main__":
    main()

    