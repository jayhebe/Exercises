def dimension(row_num, col_num):
    multilist = [[0 for col in range(col_num)] for row in range(row_num)]
    
    for row in range(row_num):
        for col in range(col_num):
            multilist[row][col] = row * col
            
    print(multilist)
    
dimension(3, 6)