import math


def is_prime_num(n):
    if n < 2: return False

    # 소수 판별은 제곱근까지만 비교해보면 충분하다
    tmp = int(math.sqrt(n))
    for i in range(2, tmp + 1):
        if n % i == 0: return False

    return True
