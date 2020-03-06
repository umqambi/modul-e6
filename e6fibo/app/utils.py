import functools

@functools.lru_cache
def fibo_steroids(n):
    if n in [0, 1]:
        return n
    else:
        return fibo_steroids(n-1) + fibo_steroids(n-2)

def is_positiv_integer(str):
    try:
        int(str)
        if int(str) >= 0:
            return True
        else:
            return False
    except ValueError:
        return False