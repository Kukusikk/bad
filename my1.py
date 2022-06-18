S = input("Введите загаданное слово:  ")
Q = input("Введите попытку:  ")
res=[]
use_sym = list(S)
for s, q in zip(S, Q):
    if s==q:
        res.append('correct')
        use_sym = [x for x in use_sym if x != q]
        continue

    if q in use_sym:
        res.append('present')
        use_sym = [x for x in use_sym if x != q]
        continue

    res.append('absent')

print(*res, sep='\n')

    