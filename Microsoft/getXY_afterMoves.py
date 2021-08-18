def solution(board, moves):
    N, M = len(board), len(board[0])
    new_r, new_c =0,0
    for move in moves:
        if move=="L" and isSafe(board, new_r, new_c-1, N, M):
            new_c-=1
        elif move =="R" and isSafe(board, new_r, new_c+1, N, M):
            new_c+=1
        elif move=="U" and isSafe(board, new_r-1, new_c, N, M):
            new_r-=1
        elif move=="D" and isSafe(board, new_r+1, new_c, N, M):
            new_r+=1
    return [new_r,new_c]

def isSafe(board, r, c, N, M):
    return r>=0 and r<N and c>=0 and c<M and board[r][c]=="."

board = ["...","...","..."]
moves = "DDURRR"
print(solution(board, moves))
