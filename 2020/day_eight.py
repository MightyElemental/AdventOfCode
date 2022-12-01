import math, copy
with open("d8_input.txt", "r") as f:
    raw_data = f.read().splitlines()

line_operations = []

for line in raw_data:
    opcode, num = line.split(" ")
    line_operations.append((opcode,num))

line_run_count = [0]*len(line_operations)

acc = 0
pointer = 0

while line_run_count[pointer] < 1:
    op, num = line_operations[pointer]
    line_run_count[pointer]+=1
    pointer+=1
    if op == "nop": continue
    elif op == "acc":
        acc += int(num)
    elif op == "jmp":
        pointer += int(num)-1

#print(acc)

# part 2

def verify_terminate(pointer_swap):
    acc = 0
    pointer = 0
    line_ops = copy.deepcopy(line_operations)
    line_count = [0]*len(line_ops)

    if line_ops[pointer_swap][0] == "nop":
        line_ops[pointer_swap] = ("jmp",line_ops[pointer_swap][1])
    elif line_ops[pointer_swap][0] == "jmp":
        line_ops[pointer_swap] = ("nop",line_ops[pointer_swap][1])

    while pointer < len(line_ops) and line_count[pointer] < 1:
        op, num = line_ops[pointer]
        line_count[pointer]+=1
        pointer+=1
        if op == "nop": continue
        elif op == "acc":
            acc += int(num)
        elif op == "jmp":
            pointer += int(num)-1
    print(acc, pointer, len(line_ops))
    if pointer >= len(line_ops):
        return True, acc
    return False, -1

for i in range(len(line_operations)):
    if line_operations[i][0] in ("jmp", "nop"):
        success, acc = verify_terminate(i)
        if success:
            print(acc)
            break