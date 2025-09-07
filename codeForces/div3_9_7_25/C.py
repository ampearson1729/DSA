import sys, math

def maxEvenSum(a: int, b: int) -> int:
    if b%2 == 0:
        if a%2 == 1 and b%4 ==2: return -1
        else: return a*b//2+2
    else:
        if a%2==1: return a*b+1
        else: return -1

def main():
    # read first line
    n = int(sys.stdin.readline())
    for line in sys.stdin:   # keeps reading until EOF
        ab = line.strip().split()
        print(maxEvenSum(int(ab[0]),int(ab[1])))

if __name__ == "__main__":
    main()
