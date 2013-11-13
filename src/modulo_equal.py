#! /usr/bin/python
import math
import random, sys

#constantes
A = -100.0
B = 100.0
numero_test = 500

def equal(expr1, expr2, A, B, n):
  i = 0
  fallos = 0
  while (i <= n): 
   a = random.uniform(A,B)
   b = random.uniform(A,B)
   if eval(expr1) != eval(expr2): 
     fallos = fallos + 1
   i = i + 1
  return (fallos*100/n)
  
if __name__ == '__main__':
  if (len(sys.argv) == 6 ):
    expr1 = sys.argv[1]
    expr2 = sys.argv[2]
    min_value = float(sys.argv[3])
    max_value = float(sys.argv[4])
    numero_test = int(sys.argv[5]) 
    print "%s %s %f %f %d" % (expr1, expr2, min_value, max_value, numero_test)
    print "Porcentaje de fallos ", equal(expr1, expr2, min_value, max_value, numero_test) 
  else: 
    print "La forma de uso es ./equal.py expr1 expr2 min_value max_value numero_test"
    print "Se usan los valores por defecto:" 
    print " %s\t\texpr1\t\texpr2\t\tmin_value\t\tmax_value\t\tnumero_test\t\tfallos" % (sys.argv[0])
    
    t1 = [['(a*b)**3','(a**3)*(b**3)'],
        ['(a/b)','1/(b/a)'],
        ['math.e**(a+b)','(math.e**a) + (math.e**b)'],

        ['a-b','(-1)*(b-a)'],
        ['(a*b)**4','(a**4) * (b**4)'],
        ['(a+b)**2','a**2 + 2*a*b + b**2'],
        ['(a+b)*(a-b)','a**2 - b**2'],]

    for i in t1:
        print " %s\t\t%s\t\t%s\t\t-100.0\t\t100.0\t\t500\t\t%g" % (sys.argv[0], i[0], i[1], equal(i[0], i[1], A, B, numero_test))

    t2 = [['math.log (a**b)','b*math.log(a)'],
         ['math.log(a*b)','(math.log(a))+(math.log(b))']]
    
        
    for i in t2:
        print " %s\t\t%s\t\t%s\t\t-100.0\t\t100.0\t\t500\t\t%g" % (sys.argv[0], i[0], i[1], equal(i[0], i[1], abs(A), abs(B), numero_test))
        