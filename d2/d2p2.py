with open("d2.txt","r") as f:
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
    t = [int(a1),int(a2),int(a3)]
    t.sort()
    tot = []
    tot.append(int(a1)*2+int(a2)*2)
    tot.append(t[0]*2+t[1]*2)
    total += min(tot)
    total += int(a1) * int(a2) * int(a3)
print(total)