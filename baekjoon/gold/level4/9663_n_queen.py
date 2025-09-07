import sys
input = sys.stdin.readline

def solve2():
    cnt=[0]
    N=int(input())
    mask = (1<<N)-1

    def dfs(i, l, m ,r):
        if i==N:
            cnt[0]+=1
            return
        
        roots = ~(l|m|r)&mask
        while roots:
            pos = roots & -roots
            roots ^= pos
            dfs(i+1, (l|pos)<<1, m|pos, (r|pos)>>1)

    dfs(0,0,0,0)
    print(cnt[0])

def solve():
    cnt=[0]
    N=int(input())
    board = [[0]*N for _ in range(N)]
    
    def dfs(i, N, board):
        if (i==N): 
            cnt[0]+=1
            return
        
        for j in range(N):
            if board[i][j]==0:
                setQueen(i, j, 1)
                dfs(i+1, N, board)
                setQueen(i, j, -1)

    
    def setQueen(i, j, dif):
        for dx in range(1, N-i):
            board[i+dx][j]+=dif
            if j+dx<N:
                board[i+dx][j+dx]+=dif
            if j-dx>-1:
                board[i+dx][j-dx]+=dif

    dfs(0, N, board)
    print(cnt[0])

if __name__ == '__main__':
    solve2()
"""
N-Queen
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
10 초	128 MB	143296	69967	44869	47.135%
문제
N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력
첫째 줄에 N이 주어진다. (1 ≤ N < 15)

출력
첫째 줄에 퀸 N개를 서로 공격할 수 없게 놓는 경우의 수를 출력한다.

예제 입력 1 
8
예제 출력 1 
92
"""