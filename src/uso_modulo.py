#! /usr/bin/python
import sys
from modulo_equal import equal 

#constantes
A = -100.0
B = 100.0
numero_test = 500

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
    print "La forma de uso es %s expr1 expr2 min_value max_value numero_test" %(sys.argv[0])
    print "Se usan los valores por defecto:" 
    print " %s expr1    expr2         min_value  max_value numero_test fallos" % (sys.argv[0])

     t1 = [['(a*b)**3','(a**3)*(b**3)'],
         ['(a/b)','1/(b/a)'],
         ['math.e**(a+b)','(math.e**a) + (math.e**b)'],
         ['a-b','(-1)*(b-a)'],
         ['(a*b)**4','(a**4) * (b**4)'],
         ['(a+b)**2','a**2 + 2*a*b + b**2'],
         ['(a+b)*(a-b)','a**2 - b**2'],
	 ['math.log (a**b)','b*math.log(a)'],
         ['math.log(a*b)','(math.log(a))+(math.log(b))'],
	 ['(a*b)','math.e**(math.log(a)+math.log(b))'],
	 ['1/(1/a+1/b)','(a*b)/(a+b)'],
	 ['a*((math.sin(b)**2)+(math.cos(b)**2))','a'],
	 ['math.sinh(a+b)','(math.e**a*math.e**b)-(math.e**(-a)*math.e**(-b))'],
	 ['math.tan(a+b)','math.sin(a+b)/math.cos(a+b)'],
	 ['math.sin(a+b)','(math.sin(a)*math.cos(b))+(math.sin(b)*math.cos(a))']]
    

