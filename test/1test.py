def iloczyn(T, n):
    iloczyn0 = 1
    for i in range(n):
        iloczyn0 = iloczyn0 * T[i]
    return iloczyn0
print(iloczyn([1, 2, 3, 4], 4))

a = [1, 2, 3, 4]
iloc = 1
for i in range(len(a)):
    iloc = iloc * a[i]
print(iloc)