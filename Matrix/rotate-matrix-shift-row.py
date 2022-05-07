import numpy as np


def shiftRow(arr, n):
    arr = np.array(arr)
    ret = np.roll(arr, n*len(arr[0]))
    return ret.tolist()

# 시계방향 테두리 회전
def rotate(arr, x2, y2):
    save = arr[0][0]

    for i in range(0, x2-1):
        # 왼쪽 세로
        tmp = arr[i + 1][0]
        arr[i][0] = tmp

    for i in range(0, y2 - 1):
        # 하단 가로
        tmp = arr[x2 - 1][i + 1]
        arr[x2 - 1][i] = tmp

    for i in range(x2 - 1, 0, -1):
        # 오른쪽 세로
        tmp = arr[i - 1][y2 - 1]
        arr[i][y2 - 1] = tmp

    for i in range(y2 - 1, 0, -1):
        # 상단 가로
        tmp = arr[0][i - 1]
        arr[0][i] = tmp

    arr[0][1] = save

    return arr

# 반시계방향 테두리 회전
def rotateReverse(arr, x, y):
    save = arr[x-1][0]

    for i in range(x-1, 0, -1):
        # 왼쪽 세로
        tmp = arr[i-1][0]
        arr[i][0] = tmp

    for i in range(0, y-1):
        # 상단 가로
        tmp = arr[0][i+1]
        arr[0][i] = tmp

    for i in range(0, x-1):
        # 오른쪽 세로
        tmp = arr[i+1][y-1]
        arr[i][y-1] = tmp

    for i in range(y-1, 0, -1):
        # 하단 가로
        tmp = arr[x-1][i-1]
        arr[x-1][i] = tmp

    arr[x-1][1] = save

    return arr


def solution(rc, operations):
    cnt = 1
    curOp = operations[0]
    answer = rc.copy()
    borderLen = len(rc)*2 + len(rc[0])*2 - 4
    width, height = len(rc[0]), len(rc)
    for i in range(1, len(operations)):
        if curOp == operations[i]:
            cnt += 1
        else:
            if curOp == "ShiftRow":
                shiftTimes = cnt % height
                if shiftTimes > 0:
                    answer = shiftRow(answer, shiftTimes)
                curOp = "Rotate"
                cnt = 1
            else:
                rotateTimes = cnt % borderLen
                if borderLen - rotateTimes < rotateTimes // 2:
                    for _ in range(rotateTimes):
                        answer = rotateReverse(answer, height, width)
                else:
                    for _ in range(borderLen - rotateTimes):
                        answer = rotateReverse(answer, height, width)
                curOp = "ShiftRow"
                cnt = 1

    if curOp == "ShiftRow":
        shiftTimes = cnt % len(rc)
        if shiftTimes > 0:
            answer = shiftRow(answer, shiftTimes)
    else:
        for _ in range(cnt):
            answer = rotate(answer, len(rc), 0, len(rc[0]))

    return answer

solution([[1, 2, 3], [4, 5, 6], [7, 8, 9]], ["Rotate", "ShiftRow", "ShiftRow"])