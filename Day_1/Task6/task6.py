import gmpy2

def add_bignums(a, b):
  return gmpy2.add(a, b)

def sub_bignums(a, b):
  return gmpy2.sub(a, b)

def mul_bignums(a, b):
  return gmpy2.mul(a, b)

def div_bignums(a, b):
  return gmpy2.div(a, b)

bigIntA = 12345678901234567890123456789012345678901234567890123456789012345678901234567890
bigIntB = 91234567890123456789012345678901234567890123456789012345678901234567890123456789

print('bigIntA + bigIntB=',add_bignums(bigIntA, bigIntB))
print('bigIntA - bigIntB=',sub_bignums(bigIntA, bigIntB))
print('bigIntA * bigIntB=',mul_bignums(bigIntA, bigIntB))
print('bigIntA / bigIntB=',div_bignums(bigIntA, bigIntB))