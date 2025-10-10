def flatten(mat: list[list | tuple]) -> list:
    spisok = list()
    for i in range(len(mat)):
        if isinstance(mat[i], list) or isinstance(mat[i], tuple):
            for j in mat[i]:
                spisok.append(j)
        else:
            return 'TypeError'
    return spisok
print('flatten')
print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))