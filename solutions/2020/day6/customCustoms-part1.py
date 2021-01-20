
def solution():
    f = open("/Users/yjlee/Documents/advent-of-code/solutions/2020/day6/data.txt",'r')
    lines = f.readlines()
    answerList,answer = {},0
    for line in lines:
        if line == '\n':
            answer+= len(answerList.keys())
            answerList = {}
        else:
            for w in line:
                if w!='\n':
                    answerList[w] = 1
    return answer
print(solution())
