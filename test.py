#input
a=int(input('x = '))
#proses
ribuan=a//1000
a=a%1000
ratusan=a//100
a=a%100
puluhan=a//10
satuan=a%10
total=ribuan+ratusan+puluhan+satuan

#output
print('Total semua digit : ', total)
