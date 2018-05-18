#
# Complete the findPoint function below.
#
# Midpoint of two point 
def findPoint(px, py, qx, qy):
    l=list()
    nX=2*qx-px
    nY=2*qy-py
    l.append(nX)
    l.append(nY)
    # print(nX)
    return l


n = int(raw_input())

for n_itr in xrange(n):
    pxPyQxQy = raw_input().split()

    px = int(pxPyQxQy[0])

    py = int(pxPyQxQy[1])

    qx = int(pxPyQxQy[2])

    qy = int(pxPyQxQy[3])

    result = findPoint(px, py, qx, qy)
    print(' '.join(map(str,result)))
