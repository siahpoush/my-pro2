myString = {" mohamad", " ali" , " hasan" ," hossein"} 
for i , j  in enumerate ( myString):
    print(' {} :{}'.format( i,j))
print( ' =' *40)
print( list(enumerate( myString , 1)))
print( ' =' *40)
myString2 = ' " mohamad" , " ali" '
print( list( enumerate( myString2)))
print( ' =' *40)
for i , j in enumerate( myString2):
    print( '{} : {}'.format(i,j))
print( ' =' *40)
