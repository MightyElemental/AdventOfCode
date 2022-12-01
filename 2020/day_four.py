with open("d4_input.txt", "r") as f:
    raw_data = f.readlines()

data = []

passp = {}
for line in raw_data:
    if line == "\n":
        data.append(passp.copy())
        passp.clear()
        continue
    line_data = line.strip().split(" ")
    for ld in line_data:
        key, value = ld.split(":")
        passp[key] = value

data.append(passp.copy())

valid = 0

for passport in data:
    fields = len(passport.keys())
    if fields >= 8: valid += 1
    elif fields == 7 and "cid" not in passport.keys(): valid += 1
    #else: print(passport)


#print(valid)

# part 2

valid = 0

eye_colors=["amb", "blu","brn","gry", "grn", "hzl", "oth"]

for passport in data:
    fields = len(passport.keys())
    if fields >= 8 or (fields == 7 and "cid" not in passport.keys()):
        #print(0, passport["byr"])
        if int(passport["byr"]) not in range (1920,2002+1): continue
        #print(1, passport["iyr"])
        if int(passport["iyr"]) not in range(2010,2020+1): continue
        #print(2, passport["eyr"])
        if int(passport["eyr"]) not in range(2020,2030+1): continue
        #print(3)
        
        height_unit = passport["hgt"][-2:]
        height_data = int(passport["hgt"][:-2])
        if height_unit == "cm":
            if height_data not in range(150,193+1): continue
        else:
            if height_data not in range(59,76+1): continue
        #print(4)

        hcl = passport["hcl"]
        if len(hcl) < 7: continue
        if not hcl.startswith("#"): continue
        
        if passport["ecl"] not in eye_colors: continue
        if len(passport["pid"]) != 9: continue

        valid+=1

    #else: print(passport)

print(valid)