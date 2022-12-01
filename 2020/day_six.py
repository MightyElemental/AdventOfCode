import math
with open("d6_input.txt", "r") as f:
    raw_data = f.readlines()

data  = []

temp = []
for line in raw_data:
    line = line.strip()
    if line == "":
        data.append(set(temp))
        temp.clear()
        continue
    temp.extend(line)

data.append(set(temp))

count = 0
for d in data:
    count+=len(d)

#print(count)

# part 2

data = []
temp = []
for line in raw_data:
    line = line.strip()
    if line == "":
        data.append(temp.copy())
        temp.clear()
        continue
    temp.append(set(line))

data.append(temp.copy())

count = 0
for d in data:
    base = d[0]
    for d2 in d:
        base = base.intersection(d2)
    count += len(base)
    print(base)

print(count)