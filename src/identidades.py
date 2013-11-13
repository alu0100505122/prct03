# -*- encoding: utf-8 -*-
#! /usr/bin/python

import os
import sys
from modulo_equal import *

# Constantes
A = -100.0
B = 100.0
numero_test = 500

if (len(sys.argv) == 6 ):
    expr1 = sys.argv[1]
    expr2 = sys.argv[2]
    min_value = float(sys.argv[3])
    max_value = float(sys.argv[4])
    numero_test = int(sys.argv[5]) 
    print "%s %s %f %f %d" % (expr1, expr2, min_value, max_value, numero_test)
    print "Porcentaje de fallos ", equal(expr1, expr2, min_value, max_value, numero_test) 
else:
    os.system('clear')
    print '-----------------------------------------------------------'
    print '--  La forma de uso es : '
    print '    ./equal.py expr1 expr2 min_value max_value numero_test'
    print '-----------------------------------------------------------'
    print '--        (se usan los valores por defecto)     --'
    print '-----------------------------------------------------------'
    print '-------------           Resultados           --------------'
    print '-----------------------------------------------------------'
    t1 = loadexpresions()
    print " %s\t\texpr1\t\texpr2\t\tmin_value\t\tmax_value\t\tnumero_test\t\tfallos" % (sys.argv[0])
    for i in t1:
        print "\n %s\t\t%s\t\t%s\t\t-100.0\t\t100.0\t\t500\t\t%g" % (sys.argv[0], i[0], i[1], equal(i[0], i[1], A, B, numero_test))
    t2 = loadlogexpresions()
    for i in t2:
        print "\n %s\t\t%s\t\t%s\t\t-100.0\t\t100.0\t\t500\t\t%g" % (sys.argv[0], i[0], i[1], equal(i[0], i[1], abs(A), abs(B), numero_test))
        

  

