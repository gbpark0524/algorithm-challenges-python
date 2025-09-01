"""
백준 28278번: 스택 2
실버 4
https://www.acmicpc.net/problem/28278

문제:
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.

명령:
1 X: 정수 X를 스택에 넣는다.
2: 스택에 정수가 있다면 맨 위의 정수를 빼고 출력한다. 없다면 -1을 출력한다.
3: 스택에 들어있는 정수의 개수를 출력한다.
4: 스택이 비어있으면 1, 아니면 0을 출력한다.
5: 스택에 정수가 있다면 맨 위의 정수를 출력한다. 없다면 -1을 출력한다.

입력:
첫째 줄에 명령의 수 N (1 ≤ N ≤ 1,000,000)
둘째 줄부터 N개 줄에 명령이 하나씩 주어진다.

출력:
출력하는 명령이 주어질 때마다 한 줄에 하나씩 출력한다.

예제 입력 1:
9
1 3
2
1 5
1 2
2
2
2
3
4

예제 출력 1:
3
2
5
-1
0
1
"""

import sys
input = sys.stdin.readline

def solve():
    cnt = int(input())
    stack = []
    for _ in range(cnt):
        command = input().split()
        if command[0] == '1':
            stack.append(int(command[1]))
        elif command[0] == '2':
            print(stack.pop() if stack else -1)
        elif command[0] == '3':
            print(len(stack))
        elif command[0] == '4':
            print(1 if not stack else 0)
        elif command[0] == '5':
            print(stack[-1] if stack else -1)   

if __name__ == "__main__":
    solve()
