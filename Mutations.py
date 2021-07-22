def mutate_string(string, position, character):
    mutate_string = string[:i] + f"{c}" + string[i+1:]
    return mutate_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)