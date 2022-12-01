f = open("d2a_input.txt", "r")
data = f.read().split("\n")

#data = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

valid = 0

for dat in data:
    policy, char, pwd = dat.replace(":", "").split(" ")
    chars_in_pwd = pwd.count(char)
    policy_bounds = policy.split("-")
    policy_bounds = [int(x) for x in policy_bounds]
    if chars_in_pwd >= policy_bounds[0] and chars_in_pwd <= policy_bounds[1]:
        valid += 1


print(valid)

# part 2

valid = 0

for dat in data:
    policy, char, pwd = dat.replace(":", "").split(" ")
    policy_bounds = policy.split("-")
    policy_bounds = [int(x)-1 for x in policy_bounds]
    place_valid = 0
    if len(pwd) > policy_bounds[0]-1:
        if pwd[policy_bounds[0]] == char:
            place_valid += 1
    if len(pwd) > policy_bounds[1]-1:
        if pwd[policy_bounds[1]] == char:
            place_valid += 1
    if place_valid == 1:
        valid += 1
        

print(valid)