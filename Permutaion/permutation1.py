# n개의 수에서 m개 중복 없이 선택(순열)
n, m = map(int, input().split())
arr = []
visited = [False] * (n+1)

def permutaion(depth):
    # m개를 골랐으면 출력하고 종료
    if depth == m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    for i in range(1, n+1):
        # i를 아직 선택하지 않았으면 선택
        if not visited[i]:
            visited[i] = True
            # 순열 배열에 추가
            arr.append(i)
            # 어떤 수를 선택한 상태에서 다른 수를 선택하기 위한 재귀 호출
            permutaion(depth + 1)
            # 순열 뽑기가 끝나면 다음 경우를 탐색해야 하니까 방문 해제
            visited[i] = False
            arr.pop()

permutaion(0)
