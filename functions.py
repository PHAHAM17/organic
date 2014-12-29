def alkani():
	n=int(input('sheiyvanet C -s indeqsi: '))
	n4 = n
	n1 = n4+1
	n3 = n4
	o = (3*n+1)
	n2 = ""
	if n == 1:
		n  = ""
		n3 = ""
 
	if o%2 == 0:
		o = o
	elif o%2!=0:
		o = 2*o
		n1 = 2*n1
		n2 = 2
		n3 = 2*n4
	print n2,'C',n,'H',2*n4+2,'+',o/2,'O2''------>',n3,'CO2','+',n1,'H2O'
 
 
 
 
def alkeni():
	n=int(input('sheiyvanet C -s indeqsi: '))
	n1 = n
	o = (3*n)
	n2 = ""
 	if n == 1:
 		print 'Error'
 	else:
		if o%2 == 0:
			o = o
		elif o%2!=0:
			o = 2*o
			n1 = 2*n
			n2 = 2
		print n2,'C',n,'H',2*n,'+',o/2,'O2''------>',n1,'CO2','+',n1,'H2O'
 
def alkini():
	n=int(input('sheiyvanet C -s indeqsi: '))
	n1 = n-1
	n3 = n
	o = (3*n-1)
	n2 = ""
	if n == 1:
 		print 'Error'
 	else:
		if o%2 == 0:
			o = o
		elif o%2!=0:
			o = 2*o
			n1 = 2*n1
			n2 = 2
			n3 = 2*n
		print n2,'C',n,'H',2*n-2,'+',o/2,'O2''------>',n3,'CO2','+',n1,'H2O'
 
 
