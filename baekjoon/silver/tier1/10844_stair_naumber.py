import sys
input = sys.stdin.readline

def solve():
    max_num = 1_000_000_000
    N=int(input())
    dp=[0]*(N+1)
    dp[1] = []
    dp[1].append(0)
    for _ in range(1, 10):
        dp[1].append(1)
    
    for i in range(2, N+1):
        dp[i]=[0]*10
        dp[i][0]=dp[i-1][1]
        dp[i][9]=dp[i-1][8]
        
        for j in range(1, 9):
            dp[i][j]=(dp[i-1][j-1]+dp[i-1][j+1])%max_num

    sm=0
    for n in dp[N]:
      sm=(n+sm)%max_num

    print(sm)

if __name__ == "__main__":
    solve()
"""
문제
"""