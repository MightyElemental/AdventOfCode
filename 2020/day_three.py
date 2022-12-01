import math

with open("d3_input.txt", "r") as f:
    raw_data = f.readlines()

data = []
width = len(raw_data[0].strip())
height = len(raw_data)

for line in raw_data:
    data.append([char for char in line.strip()])

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
tree_per_slope = []

for slope in slopes:
    trees = 0
    x=0
    y=0
    while y < height:
        if data[y][x%width] == "#": trees +=1
        x+=slope[0]
        y+=slope[1]
    tree_per_slope.append(trees)
    print(slope, trees)

print(tree_per_slope)
print(math.prod(tree_per_slope))