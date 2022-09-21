x = int(input ( "Primul numar:" ))
y = int(input ( "Al doilea numar:" ))
 # (1)
def s(x , y ):
    return ( x + y )
print ( "Suma:" , s ( x , y ))
 # (2)
def  pr( x , y ):
    return ( x * y )
print ( "Produsul:" , pr ( x , y ))
 # (3)
def  med_arit ( x , y ):
    ma = ( x + y ) / 2
    return ( ma )
print ( "Media aritmetica a numerelor:" , med_arit ( x , y ))
 # (4)
 # (5)
def  cmmdc( m , n ):
    while  m != n :
        if  m > n : m = m - n
        altfel : n = n - m
        return ( m )
m = int(input ( "m=" ))
n = int(input ( " n=" ))
print ( "Cel mai mare divizor comun:" , cmmdc ( m , n ))
print ( "Cel mai mic multiplu comun:" , str ( m * n // cmmdc ( m , n )))
 # (6))
def  min ( x , y ):
    return ( min ( x , y ))
print ( "Numarul minim:" , min ( x , y ))
 # (7))
def  max( x , y ):
    return ( max ( x , y ))
print ( "Numarul maxim:" , max ( x , y ))
 # (8)
def  s2 ():
    x = int(input ( "introduceti nr.x:" ))
    y = int(input ( "introduceti nr.y:" ))
    c = 0
    c = x + y
    return ( c )
s = s2 ()
print ( "Suma sub forma x+y=c este:" , s )
 # (9)
def  pr2 ():
    x = int(input ( "introduceti nr.x:" ))
    y = int(input ( "introduceti nr.y:" ))
    c = 1
    c = x * y
    return ( c )
p = pr2 ()
print ( "Produsul sub forma x*y=c este:" , p )