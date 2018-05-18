
def handshake(n):

    if n<1:
        return n
    else:
        n=n*(n-1)/2
        return n       
    #
    # Write your code here.
    #



t = int(raw_input())

for t_itr in xrange(t):
    n = int(raw_input())

    result = handshake(n)

    print result


