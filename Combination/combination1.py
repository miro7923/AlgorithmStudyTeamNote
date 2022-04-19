# n개 중에서 r개 선택하는 조합(중복 X)
arr = [1,2,3,4]
n = len(arr)
r = int(input())
pick = [0 for _ in range(r)]

def combination(depth, next):
    if depth == r:
        for i in pick:
            print(i, end=' ')
        print()
        return

    for i in range(next, n):
        pick[depth] = arr[i]
        # 다음에 선택할 범위를 한 칸 좁힌다.
        combination(depth+1, i+1)

combination(0, 0)