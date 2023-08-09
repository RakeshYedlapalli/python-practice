def solve(self):
    if len(self) == 0:
        return []
    k = 0
    for i in range(len(self)):
        if self[i] != 0:
            self[k] = self[i]
            k += 1
    for j in range(k, len(self)):
        self[j] = 0
    return self


L = [2, 0, 1, 4, 0, 5, 6, 4, 0, 1, 7]
print(solve(L))
