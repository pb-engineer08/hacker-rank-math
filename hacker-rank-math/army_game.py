

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