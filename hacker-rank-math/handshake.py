
# def handshake(n):

#     if n<1:
#         return n
#     else:
#         n=n*(n-1)/2
#         return n       
#     #
#     # Write your code here.
#     #



# t = int(raw_input())

# for t_itr in xrange(t):
#     n = int(raw_input())

#     result = handshake(n)

#     print result

# def lowestTriangle(base, area):
#     # Complete this function
#     #Area of an triangle with h is A=bh/2
#     x = area*2
#     ans = int(x/base)
#     if x % base == 0 :
#      H=ans
#     else :
#         H=ans + 1
#     return H
#     #So h= 2*A/b
#     # A=2.0*area/base
#     # return round(A)

# base, area = raw_input().strip().split(' ')
# base, area = [int(base), int(area)]
# height = lowestTriangle(base, area)
# print(height)



#
# Complete the gameWithCells function below.
#
def gameWithCells(n, m):

    if n%2==1: 
        n=n+1
    if m%2==1:
        m=m+1         

    return ((n*m)/4)       
    #
    # Write your code here.
    #


nm = raw_input().split()

n = int(nm[0])

m = int(nm[1])

result = gameWithCells(n, m)
print result