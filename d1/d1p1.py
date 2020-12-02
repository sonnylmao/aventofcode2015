with open("d1.txt","r") as f:
    content = f.readlines()
    content = [x.strip() for x in content]
a = [char for char in content[0]]
print(a)

f = 0
pos = 0
for x in a:
    if x == '(':
        f += 1
    elif x == ')':
        f -= 1
    if f == -1:
        print(pos+1)
        break
    else:
        pos += 1
