f=lambda x:'{:02d}'.format(int(x))
p=print
k=int(input())/1000
if k<0.1:p('00')
elif k<6:p(f(k*10))
elif k<35:p(f(k+50))
elif k<=70:p(f((k-30)/5+80))
else:p(89)
