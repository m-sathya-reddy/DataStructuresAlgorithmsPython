import sys

input = sys.stdin.readline


############ ---- Input Functions ---- ############
def inp():
    return (int(input()))


def inlt():
    return (list(map(int, input().split())))


def insr():
    s = input()
    return (list(s[:len(s) - 1]))


def invr():
    return (map(int, input().split()))


if __name__ == '__main__':
    num = inp()
    result = "YES" if (num / 2 == num // 2) else "NO"
    print (result)
