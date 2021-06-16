# Mutations

# HackerRank Problem solved

def mutate_string(string, position, character):
    
    t=list(string)
    t[position]=character
    return "".join(t)

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
