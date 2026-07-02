#Spiral Matrix
matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
n = len(matrix)
m = len(matrix[0])
res = []
col_start = 0
col_end = m - 1
row_start = 0
row_end = n - 1

while len(res) < n*m:
    #row_start, col_start -> col_end
    for i in range(col_start, col_end+1):
        res.append(matrix[row_start] [i])
    row_start += 1
    
    if len(res) == n*m:
        break
    
    #col_end, row_start -> row_end
    for i in range(row_start, row_end+1):
        res.append(matrix[i][col_end])
    col_end -= 1
    
    if len(res) == n*m:
        break
    
    #row_end, col_end -> col_start
    for i in range(col_end, col_start -1, -1):
        res.append(matrix[row_end][i])
    row_end -= 1
    
    if len(res) == n*m:
        break
    
    #col_start, row_end --> row_start
    for i in range(row_end, row_start -1, -1):
        res.append(matrix[i][col_start])
    col_start += 1 
    
    
print(res)


#TC: O(n * m)
#SC: O(n * m)