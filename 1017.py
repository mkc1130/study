import sys
import math

def dfs(x):   #소수 판독 명령 정의
    global Y                                                #Y를 만든다.
    global matched                                          #맞는지 확인할 matched를 만든다.
    global visited                                          #다녀갔는지 확인할 visited를 만든다.
    if visited[Y.index(x)]: return False                    #(matched[y]) visited리스트의 인덱싱값을 확인하고 나면 False값을 돌려준다.
    visited[Y.index(x)] = True                              #visited리스트의 인덱싱값을 true로 바꿔준다.
    for y in Y:                                             #y가 Y와 일치한다면 다음과 같은 명령문을 실행한다.
        if x + y in primes:                                 #x+y가 소수리스트에 있다면 다음과 같은 명령문을 실행한다.
            if y not in matched or dfs(matched[y]):         #y가 matched에 없거나 matched[y]에 있는 수를 다시 명령어를 돌리고 난 결과값이 true일 경우 다음과 같은 명령문을 싱행한다. 
                matched[y] = x
                return True
    return False

N = int(sys.stdin.readline())                               #입력값을 가져오고 Int로 형변환한다.
X = list(map(int, sys.stdin.readline().split()))            #입력값을 가져오고 split을 사용하여 값을 나눠 리스트에 넣을 때 map를 사용하여 Int로 형변환 시켜준다.

# 소수 목록을 준비하기
primes = []
for i in range(2, 2000):                                    #2000까지의 범위에서 1을 제외한 소수를 찾기위한 방법.
    is_prime = True                                         #is_prime의 기본값을 true로 지정해준다.
    for j in range(2, i):                                   #2부터 i까지의 반복문을 실행할 임시변수인 i를 사용한다.
        if i % j == 0:                                      #i를 j로 나눈값의 나머지가 0일경우 다음과 같은 명령문을 실행한다.
            is_prime = False                                #나머지가 0이라면 나눠떨어진경우이므로 소수가 아니기에 false로 값을 바꿔준다.
            break
    if is_prime : primes.append(i)                          #true라면 소수인 것이기에 primes리스트에 I값을 넣어준다.
    else : continue                                         #false라면 계속한다.

answers = []                                                #answers 리스트를 선언
for i in X:                                         
    matched = {}                                    
    if i == X[0]: continue                                  #i값이 x[0]값이라면 다음 숫자로 건너뛰고 계속한다.
    if X[0] + i in primes:                                  #x[0] + i값이 소수리스트안에 포함된다면
        if N == 2:                                          #N의 값이 2라면 다음과같은 반복문을 실행시킨다.
            answers.append(i)                               #answers에 i값을 추가한다.
            break                                           #명령문을 중지시키고 탈출한다.
        # 첫번째 숫자와 현재 매치된 숫자를 제외한 새 리스트를 만들어준다.
        Y = [x for x in X]
        del Y[0]
        del Y[Y.index(i)]
        matched = {}
        for y in Y:                                         #y값이 Y에 존재할경우 다음과같은 명령문을 실행한다.
            visited = [False for _ in range(len(Y))]
            dfs(y)                                          #y값을 판독한다.

    if N != 2 and len(matched) == N - 2: answers.append(i)  #만약 N이 2가 아니고 matched의 길이값이 N-2일경우 answers리스트에 i값을 추가한다.

if not answers:     
    answers.append(-1)

answers.sort()

print(' '.join(list(map(str,answers)))) #answers값을 출력한다.