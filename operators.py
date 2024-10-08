# Arithmetic operators
# +	Addition	x + y
x=10
y=11
print(x+y)
# -	Subtraction	x - y
x=10
y=11
print(x-y)
# *	Multiplication	x * y
x=10
y=11
print(x*y)
# /	Division	x / y
x=20
y=11
print(x/y)
# %	Modulus	x % y
x=20
y=11
print(x%y)
# **	Exponentiation	x ** y
x=2
y=3
print(x**y)
# //	Floor division	x // y
x=30
y=11
print(x//y)

# Assignment operators
# =	x = 5
x = 5
print(x)
# +=	x += 3	x = x + 3
# -=	x -= 3	x = x - 3
# *=	x *= 3	x = x * 3
# /=	x /= 3	x = x / 3
# %=	x %= 3	x = x % 3
# //=	x //= 3	x = x // 3
# **=	x **= 3	x = x ** 3
# &=	x &= 3	x = x & 3
# |=	x |= 3	x = x | 3
# ^=	x ^= 3	x = x ^ 3
# >>=	x >>= 3	x = x >> 3
# <<=	x <<= 3	x = x << 3

# Comparison operators
# ==	Equal	x == y
x = 10
y = 11
print(x==y)
# !=	Not equal	x != y
x = 10
y = 11
print(x!=y)
# >	Greater than	x > y
x = 10
y = 11
print(x>y)
# <	Less than	x < y
x = 10
y = 11
print(x<y)
# >=	Greater than or equal to	x >= y
x = 10
y = 11
print(x>=y)
# <=	Less than or equal to	x <= y
x = 10
y = 11
print(x<=y)

# Logical operators
# and 		x < 5 and  x < 10
x = 5
print(x > 6 and x < 10)
# or		x < 5 or x < 4
x = 5
print(x > 6 or x < 10)
# not	 is true	not(x < 5 and x < 10)
x = 5
print(not(x > 6 and x < 10))
# # Identity operators
# is 	x is y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is z)
print(x is y)
print(x == y)
# is not	x is not y
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x
print(x is not z)
print(x is not y)
print(x != y)
# Membership operators
# in  x in y
x = ['mahafuja', 'barik']
print('barik' in x)
# not in  x not in y
x = ['mahafuja', 'barik']
print('barik' not in x)
# Bitwise operators