
'first rule -- string & numaric value can oprpate together with *'
a,b=2,3
txt="@"
print(2*txt*3)


'second rule -- string &string can oprate with +'
a,b="2",3
txt="@"
print((a+txt)*b)

'third rule -- numaric value can oprate with all arthimetic opraters'
a,b=2,3
c=4
print(a+b*c)

'fourth rule --- Arithmetic expression with integer and float will result in float'
a,b=2,3.6
c=a*b
print(c)
'five rule--  result of division oprator with two integer will be flot '
a,b=2,3
c=a/b
print(c)
'six rule --- integer division with float and inr will given int displayed as float   (// integer division and / division)'
a,b=2.4,3
c=a//b
print(c,a/b)
 
'seven rule -- ramainder is negative when denominator is negative'
a,b=-2,3
c=a%b
print(c)

a,b=2,3
c=a%b
print(c)

a,b=2,-3
c=a%b
print(c)