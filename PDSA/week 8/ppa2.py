def calculateAndAssign(x, y):
    num1_length = len(str(x))
    num2_length = len(str(y))
    n = max(num1_length,num2_length)
    l = n//2
    num1 = x // (10 ** l)
    rem1 = x % (10 ** l)
    num2 = y // (10 ** l)
    rem2 = y % (10 ** l)
    ac = Karatsuba(num1, num2)
    bd = Karatsuba(rem1, rem2)
    return (num1 + rem1), (num2 + rem2), ac, bd, l
def Karatsuba(x, y):
    if x < 10 and y < 10:
        return x * y
    var1, var2, var3, var4, var5 = calculateAndAssign(x, y)
    ad_plus_bc = Karatsuba(var1, var2) - var3 - var4
    return (10 ** (2*var5))*var3 + (10 ** var5)*ad_plus_bc + var4
x=int(input())
y=int(input())
print(Karatsuba(x,y))
