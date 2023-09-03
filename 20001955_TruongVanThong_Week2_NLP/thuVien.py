import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

'''
Hàm tính phương trình bậc 2:
    - Input: a, b, c
    - Output: nghiệm của phương trình
'''
def tinhPTB2(a, b, c):
    if a == 0:
        if b == 0:
            return "Phương trình vô nghiệm"
        else:
            x = -c / b
            return "Phương trình có một nghiệm: x = {:.2f}".format(x)
    else:
        delta = b**2 - 4*a*c
        if delta < 0:
            return "Phương trình vô nghiệm"
        elif delta == 0:
            x = -b / (2 * a)
            return "Phương trình có nghiệm kép: x1 = x2 = {:.2f}".format(x)
        else:
            x1 = (-b + math.sqrt(delta)) / (2 * a)
            x2 = (-b - math.sqrt(delta)) / (2 * a)
            return "Phương trình có 2 nghiệm phân biệt: x1 = {:.2f}, x2 = {:.2f}".format(x1, x2)