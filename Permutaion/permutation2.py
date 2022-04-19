# n개의 수에서 m개 중복 없이 선택(순열)
n, m = map(int, input().split())
arr = [0] * m
visited = [False] * (n+1)

def permutaion(depth):
    # m개를 골랐으면 출력하고 종료
    if depth == m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    # 마지막으로 선택된 인덱스에 접근해야 하는데 깊이가 0일 때 -1하면 인덱스 범위 초과 에러나니까 0보다 작아지지 않도록 한다.
    last = (0 if depth-1 < 0 else depth-1)
    for i in range(1, n+1):
        # i를 아직 선택하지 않았고 직전에 고른 수보다 크다면 선택
        if not visited[i] and i > arr[last]:
            visited[i] = True
            # 순열 배열에 추가
            arr[depth] = i
            # 어떤 수를 선택한 상태에서 다른 수를 선택하기 위한 재귀 호출
            permutaion(depth + 1)
            # 순열 뽑기가 끝나면 다음 경우를 탐색해야 하니까 방문 해제
            visited[i] = False

permutaion(0)
