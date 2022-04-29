def get_k_num(n, k):
    arr = ''

    while n > 0:
        n, mod = divmod(n, k)
        arr += str(mod)

    # 순서대로 저장된 나머지를 뒤집어야 진짜 k 진수를 얻을 수 있다.
    return arr[::-1]
