
def solution():
    f = open("/Users/yjlee/Documents/advent-of-code/solutions/2020/day5/data.txt",'r')
    lines = f.readlines()
    answer = 0
    seat_ids = []

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
        seat_ids.append((row_st*8)+col_st)
    for i in range(1,127):
        for j in range(0,8):
            seat_id = i * 8 + j
            if (seat_id + 1) in seat_ids and (seat_id - 1) in seat_ids and  seat_id not in seat_ids:
                answer = seat_id
                break    
    return answer
print(solution())