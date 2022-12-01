import math, itertools
with open("d7_input.txt", "r") as f:
    line_data = f.read().splitlines()

bag_dict = {}

for line in line_data:
    split_line = line.replace('bags','').replace('bag','').replace("contain", ",").replace(".","").replace(" ","").split(",")
    #print(split_line)
    bag_dict[split_line[0]] = split_line[1:]

#print(bag_dict)

count = 0

print(list(itertools.chain.from_iterable(bag_dict.values())))

def loop(key:str):
    pass

# part 2
#print((lambda f,x,l:f(f,x,l))(lambda f,x,l:sum(int(i[0])*(1+f(f,x+[i[1:]],l))for i in l[x[-1]]if i[1:]not in x)if x[-1]in l else 0,['shinygold'],{j[0]:j[1:]for j in[i[:-2].replace('bags','').replace('bag','').replace('contain',',').replace(' ','').split(',')for i in open('d7_input.txt','r')if not"other"in i]})) 
