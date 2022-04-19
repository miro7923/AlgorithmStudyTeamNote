# n개의 수에서 m개 중복 없이 선택(조합)
n, m = map(int, input().split())
arr = [0] * m

def permutaion(depth):
    # m개를 골랐으면 출력하고 종료
    if depth == m:
        for i in arr:
            print(i, end=' ')
        print()
        return

    last = (0 if depth-1 < 0 else depth-1)
    for i in range(1, n+1):
        if i >= arr[last]:
            # 조합 배열에 추가
            arr[depth] = i
            # 어떤 수를 선택한 상태에서 다른 수를 선택하기 위한 재귀 호출
            permutaion(depth + 1)

permutaion(0)
