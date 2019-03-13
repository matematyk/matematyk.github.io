def sum_fun(n):
    if n == 1:
        return 1
    return sum_fun(n-1)+1
print(sum_fun(9))

def sum_c_fun(n):
    if n != 1:
        return n + sum_c_fun(n-1)
    else:
        return n

print(sum_c_fun(9))