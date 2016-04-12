from sys import stdin as Si
if __name__=='__main__':
    n = int(Si.readline())
    for i in range(1,n+1):
        S = Si.readline().strip('\n')
        Str,l = S[0],len(S)
        for j in range(1,l):
            Str = max(Str+S[j],S[j]+Str)
        print('Case #%d: %s'%(i,Str))
