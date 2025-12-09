import sys
input = sys.stdin.readline

def solve():
    astr=input().strip()
    bstr=input().strip()
    m=len(astr)
    n=len(bstr)
    dp = [[0]*(n+1) for _ in range(m+1)]
    
    for i in range(0,m):
        for j in range(0,n):
            if astr[i]==bstr[j]:
                dp[i+1][j+1]=dp[i][j]+1
            else :
                dp[i+1][j+1]=max(dp[i][j+1],dp[i+1][j])
    
    print(dp[m][n])

if __name__ == "__main__":
    solve()
"""
LCS
 
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
0.1 초 (하단 참고)	256 MB	109160	46959	34383	42.257%
문제
LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때, 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.

예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

입력
첫째 줄과 둘째 줄에 두 문자열이 주어진다. 문자열은 알파벳 대문자로만 이루어져 있으며, 최대 1000글자로 이루어져 있다.

출력
첫째 줄에 입력으로 주어진 두 문자열의 LCS의 길이를 출력한다.

예제 입력 1 
ACAYKP
CAPCAK
예제 출력 1 
4
"""