import copy
with open("d10_input.txt", "r") as f:
    data = [int(x) for x in f.read().splitlines()]

def build_chain(adapters: list, current_jolt:int = 0, jolt_diffs:list = [0]*4):
    if not adapters: return jolt_diffs, True
    valid_adap = [x for x in adapters if current_jolt<x<=current_jolt+3]
    if not valid_adap: return None, False
    for v in valid_adap:
        remaining_adapters = copy.deepcopy(adapters)
        remaining_adapters.remove(v)
        jolt_diffs[v-current_jolt] += 1
        differences, eoc = build_chain(remaining_adapters, v, jolt_diffs)
        if eoc: return differences, True
    return jolt_diffs, False

print(build_chain(data))