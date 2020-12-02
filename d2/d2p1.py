with open("Desktop/d2.txt","r") as f:
    content = f.readlines()
    content = [x.strip() for x in content]

total = 0

for x in content:
    pos = []
    a = [char for char in x]
    for m in range(len(a)):
        if a[m] == 'x':
            pos.append(m)
    s1 = ''
    a1 = s1.join(a[0:pos[0]])
    s2 = ''
    a2 = s2.join(a[pos[0]+1:pos[1]])
    s3 = ''
    a3 = s3.join(a[pos[1]+1:len(a)])
    tot = []
    total += 2 * int(a1) * int(a2)
    total += 2 * int(a1) * int(a3)
    total += 2 * int(a2) * int(a3)
    tot.append(int(a1) * int(a2))
    tot.append(int(a1) * int(a3))
    tot.append(int(a2) * int(a3))
    total += min(tot)
print(total)
