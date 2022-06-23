passerby = (input().split())
for i in range(0, len(passerby)):
    passerby[i] = int(passerby[i])
rich = []
poor = []
a = 0
n = len(passerby)
passerby.sort()
for i in range(0, n // 2):
    poor.append(passerby[i])
for i in range(n // 2, n):
    rich.append(passerby[i])
if n % 2 == 0:
    for i in range(0, n // 2):
        a = a + rich[n//2 - 1 - i] - poor[i]
else:
    for i in range(0, n // 2):
        a = a + rich[n//2 - i] - poor[i]
print(a)
