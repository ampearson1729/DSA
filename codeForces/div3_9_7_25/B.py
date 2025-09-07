import sys, math

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def valid_adjacent(s):
    # check gcd(s[i], s[i+1]) >= 3 for all i
    for i in range(len(s) - 1):
        if gcd(s[i], s[i+1]) < 3:
            return False
    return True

def solve_one(n, p):
    # available numbers grouped by residue mod 3
    avail = {0: [], 1: [], 2: []}
    for x in range(1, n + 1):
        avail[x % 3].append(x)

    q = [0] * n
    s = [None] * n  # sums p_i + q_i

    # Greedy: make sums ≡ 0 (mod 3) where possible
    leftovers = []
    for i, pi in enumerate(p):
        want = (-pi) % 3
        if avail[want]:
            qi = avail[want].pop()
            q[i] = qi
            s[i] = pi + qi
        else:
            leftovers.append(i)

    # Gather leftover numbers (m is 0, 1, or 2 for n%3 ≠ 0 cases)
    rem = avail[0] + avail[1] + avail[2]
    m = len(leftovers)

    if m == 0:
        # all sums ≡ 0 (mod 3) -> automatically valid
        return q

    # Helper: assign leftovers according to a pattern and test only the
    # affected neighborhood (but full check is still O(n) and cheap).
    def try_pattern(nums_order):
        for idx, num in zip(leftovers, nums_order):
            q[idx] = num
            s[idx] = p[idx] + num
        return valid_adjacent(s)

    if m == 1:
        # Only one leftover; try the only choice
        if try_pattern(rem):
            return q
        # If somehow not valid (rare), try swapping with a neighbor deterministically
        i = leftovers[0]
        if i > 0:
            q[i], q[i-1] = q[i-1], q[i]
            s[i], s[i-1] = p[i]+q[i], p[i-1]+q[i-1]
            if valid_adjacent(s):
                return q
            # revert
            q[i], q[i-1] = q[i-1], q[i]
            s[i], s[i-1] = p[i]+q[i], p[i-1]+q[i-1]
        if i+1 < n:
            q[i], q[i+1] = q[i+1], q[i]
            s[i], s[i+1] = p[i]+q[i], p[i+1]+q[i+1]
            if valid_adjacent(s):
                return q

    elif m == 2:
        # Two leftovers: try two fixed orders (no permutations explosion)
        a, b = rem[0], rem[1]
        if try_pattern([a, b]):
            return q
        if try_pattern([b, a]):
            return q
        # deterministic local swap with neighbors, if needed
        i, j = leftovers[0], leftovers[1]
        if i > 0:
            q[i], q[i-1] = q[i-1], q[i]
            s[i], s[i-1] = p[i]+q[i], p[i-1]+q[i-1]
            if valid_adjacent(s):
                return q
            # revert
            q[i], q[i-1] = q[i-1], q[i]
            s[i], s[i-1] = p[i]+q[i], p[i-1]+q[i-1]
        if j+1 < n:
            q[j], q[j+1] = q[j+1], q[j]
            s[j], s[j+1] = p[j]+q[j], p[j+1]+q[j+1]
            if valid_adjacent(s):
                return q

    # By problem statement, a solution always exists; the patterns above suffice.
    return q


def main():
    # read first line
    n = int(sys.stdin.readline())
    for line in sys.stdin:   # keeps reading until EOF
        nlst = line.strip().split()
        print(maxEvenSum(int(nlst[0]),list(map(int,lst[1]))))

if __name__ == "__main__":
    main()
