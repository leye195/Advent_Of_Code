
def solution():
    f = open("/Users/yjlee/Documents/advent-of-code/solutions/day5/data.txt",'r')
    lines = f.readlines()
    answer = 0

    for line in lines:
        boarding_pass = line.strip()
        row_st,row_en,col_st,col_en = 0,127,0,7 
        print(boarding_pass)
        for w in boarding_pass:
            if w == "F":
                row_md = (row_st + row_en)//2
                row_en = row_md-1
            elif w == "B":
                row_md = (row_st + row_en)//2
                row_st = row_md+1
            elif w == "L":
                col_md = (col_st + col_en)//2
                col_en = col_md-1
            elif w == "R":
                col_md = (col_st + col_en)//2
                col_st = col_md+1
        answer = max(answer,(row_st*8)+col_st)
    return answer
print(solution())