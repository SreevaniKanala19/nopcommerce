def print_rangoli(n):
    # your code goes here
    import string
    design = string.ascii_lowercase

    L = []
    for i in range(n):
        s = "-".join(design[i:n])
        L.append((s[::-1] + s[1:]).center(4 * n - 3, "-")) # [s = a-b-c, c-b-a-b-c .center(9, -),i = 1, s = b-c, --c-b-c--, ----c----]

    # print('\n'.join(L[:0:-1] + L))
    print(L)
    print(L[:0:-1])


print_rangoli(3)

