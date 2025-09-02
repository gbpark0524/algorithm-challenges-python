#브론즈1
import sys
from math import factorial as ft
import math
input = sys.stdin.readline

def solve():
    N, K=map(int, input().split())
    print(int(ft(N)/ft(N-K)/ft(K)))

if __name__ == '__main__':
    solve()
"""
이항계수 구하기
예제 입력 1 
5 2
예제 출력 1 
10
"""