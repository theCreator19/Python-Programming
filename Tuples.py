# Tuples
# HackerRank problem solved

if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    c=tuple(integer_list)
    print(hash(tuple(c)))
