# rock =1, paper =2 , scissors =3
# win = 6, draw = 3, lose = 0

# part1
def matchOutcome(play1: str, play2: str):
    return {
        "X":{
            "A":3+1,
            "B":0+1,
            "C":6+1
        },
        "Y":{
            "A":6+2,
            "B":3+2,
            "C":0+2
        },
        "Z":{
            "A":0+3,
            "B":6+3,
            "C":3+3
        }
    }.get(play2).get(play1)

def decodePlay(play1: str, play2: str):
    return {
        "X":{
            "A":"Z",
            "B":"X",
            "C":"Y"
        },
        "Y":{
            "A":"X",
            "B":"Y",
            "C":"Z"
        },
        "Z":{
            "A":"Y",
            "B":"Z",
            "C":"X"
        }
    }.get(play2).get(play1)


with open("day2_input.txt", "r") as f:
    raw_data = f.readlines()


totalScore = 0
for line in raw_data:
    play1, play2 = line.strip().split(" ")
    totalScore += matchOutcome(play1, play2)

print("part 1:",totalScore)

totalScore = 0
for line in raw_data:
    play1, play2 = line.strip().split(" ")
    totalScore += matchOutcome(play1, decodePlay(play1, play2))

print("part 2:", totalScore)

