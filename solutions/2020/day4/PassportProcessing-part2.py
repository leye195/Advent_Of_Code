import re
'''
byr (Birth Year) - four digits; at least 1920 and at most 2002.
iyr (Issue Year) - four digits; at least 2010 and at most 2020.
eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
hgt (Height) - a number followed by either cm or in:
If cm, the number must be at least 150 and at most 193.
If in, the number must be at least 59 and at most 76.
hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
pid (Passport ID) - a nine-digit number, including leading zeroes.
cid (Country ID) - ignored, missing or not
'''

def check_validation(key,value):
    if key == "byr":
        return int(value) >=1920 and int(value) <=2002
    elif key == "iyr":
        return int(value) >=2010 and int(value) <=2020
    elif key == "eyr":
        return int(value) >=2020 and int(value) <=2030
    elif key == "hgt":
        if "cm" in value:
            h = int(value[0:len(value)-2])
            return h>=150 and h<=193
        if "in" in value:
            h = int(value[0:len(value)-2])
            return h>=59 and h<=76
        return False
    elif key == "ecl":
        return value in ["amb","blu","brn","gry","grn","hzl","oth"]
    elif key == "pid":
        return len(value)==9
    elif key == "hcl":
        r = re.compile('#[0-9a-z]{6}').match(value)
        if r:
            return True
        return False
    return True
    
def solution():
    f = open("/Users/yjlee/Documents/advent-of-code/solutions/day4/input.txt",'r')
    lines = f.readlines()
    answer = 0
    for line in lines:
        if line !='\n':
            info = line.split(" ")
            keys = [ i.split(":")[0] for i in info]
            if len(keys)==8 or (len(keys)==7 and "cid" not in keys): 
                flag = True
                for data in info:
                    key,value = data.split(":")
                    if(check_validation(key,value.split("\n")[0])==False):
                        flag = False
                        break
                if flag:
                    answer+=1                   
    return answer

print(solution())
