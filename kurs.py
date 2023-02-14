#input
a=int(input('dalam rupiah = '))
#proses
b=a/14900
b=round(b,2)
c=a/130
c=round(c,2)
d=a/16700
d=round(d,2)
e=a/11500
e=round(e,2)
#output
print('Rp.',a, 'dalam USD : ', b,'dolar')
print('Rp.',a, 'dalam Yen : ', c,'yen')
print('Rp.',a, 'dalam Eur : ', d,'euro')
print('Rp.',a, 'dalam AUD : ', e,'dolar Australia')
