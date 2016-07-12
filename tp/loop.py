# Loops

num = count = 0 
out = ''
while (count <= 20 ):
    num = num + 2
    if (count == 10):
        out = out + str(num) + ' '
    elif(count == 20):
        out = out + str(num) + ' '
    else:
        out = out + str(num) + ', '
    count = count + 1
print('*******************************')
print(out)
print('%d digits printed\n' % count)
