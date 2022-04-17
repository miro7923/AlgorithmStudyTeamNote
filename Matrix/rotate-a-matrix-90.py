def rotateAMatrix90(arr):
    n = len(arr)  # 행 길이
    m = len(arr[0])  # 열 길이
    result = [[0] * n for _ in range(m)]  # 회전 결과 배열
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = arr[i][j]

    return result