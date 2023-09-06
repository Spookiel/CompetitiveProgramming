p,q = list(map(int, input().split()))



grid = [[1-int((i+j)%2) for i in range(q)] for j in range(p)]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if not grid[i][j]:
            grid[i][j] = -1

for i in grid:
    print(*i)
### My turn first
def minimax(cols_taken, rows_taken, turn=0):
    if not turn:
        moves = [(0, [])]
        for col in range(1, q-cols_taken+1):
            ### Can take any whole number of columns
            darks = 0
            for r in range(p-rows_taken):
                for c in range(cols_taken, cols_taken+col):
                    darks += grid[r][c]
            print(darks, col)
            score, moves = minimax(cols_taken+col, rows_taken, 1-turn)
            result = darks+score
            moves.append((result, moves+[col]))
        moves.sort(reverse=True)
        return moves[0]
    else:
        return (0,[])

res = minimax(0,0)