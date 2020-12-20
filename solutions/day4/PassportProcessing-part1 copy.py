'''
byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''
def solution():
    f = open("/Users/yjlee/Documents/advent-of-code/solutions/day4/input.txt",'r')
    lines = f.readlines()
    answer = 0
    for line in lines:
        if line !='\n':
            info = [ i.split(":")[0] for i in line.split(" ")]
            if len(info)==8 or (len(info)==7 and "cid"  not in info):
                answer+=1
    return answer
print(solution())
