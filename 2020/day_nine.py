with open("d9_input.txt", "r") as f:
    raw_data = f.read().splitlines()

preamble = 25
data = [int(x) for x in raw_data]
last_25 = data[:preamble]
fail_pos = -1

answer = -1

for i in range(preamble, len(data)):
    number = data[i]
    flag = True
    for test in last_25:
        val = abs(number-test)
        if val in last_25:
            if val != test or (val == test and last_25.count(val) > 1):
                del last_25[0]
                last_25.append(number)
                flag = False
                break
    if flag:
        print(number)
        answer = number
        fail_pos = i
        break

# part 2

for start in range(fail_pos):
    for end in range(fail_pos):
        if sum(data[start:end]) == answer:
            mi = min(data[start:end])
            ma = max(data[start:end])
            e = end
            print(mi, ma, mi+ma)