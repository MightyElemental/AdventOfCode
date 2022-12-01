import math
with open("d5_input.txt", "r") as f:
    raw_data = f.readlines()

#raw_data = ["BFFFBBFRRR", "BBFFBBFRLL", "FFFBBBFRRR"]

data = []

seats = []
ids = []

max_id = 0

for line in raw_data:
    line = line.strip()
    lower = 0
    upper = 127
    low_col = 0
    upp_col = 7
    for i in range(len(line)):
        if line[i] == "F":
            upper -= math.ceil((upper-lower)/2)
        elif line[i] == "B":
            lower += math.ceil((upper-lower)/2)
        elif line[i] == "R":
            low_col += math.ceil((upp_col-low_col)/2)
        elif line[i] == "L":
            upp_col -= math.ceil((upp_col-low_col)/2)

    seat_row = lower
    seat_col = low_col
    seats.append((seat_row,seat_col,seat_row*8+seat_col))
    ids.append(seat_row*8+seat_col)
    max_id = max(seat_row*8+seat_col, max_id)
    #print(seat_row, seat_col)

print(max_id)

# part 2

for row in range(0,128):
    for col in range(0,8):
        id = row*8+col
        if (id not in ids) and (id+1 in ids) and (id-1 in ids):
            print(row, col, id)
