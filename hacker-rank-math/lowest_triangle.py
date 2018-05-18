def lowestTriangle(base, area):
    # Complete this function
    #Area of an triangle with h is A=bh/2
    x = area*2
    ans = int(x/base)
    if x % base == 0 :
     H=ans
    else :
        H=ans + 1
    return H
    #So h= 2*A/b
    # A=2.0*area/base
    # return round(A)

base, area = raw_input().strip().split(' ')
base, area = [int(base), int(area)]
height = lowestTriangle(base, area)
print(height)
