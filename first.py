import sys
import os
import functions

def cls():
    os.system(['clear','cls'][os.name == 'nt'])
 

reaction = {1:functions.alkani , 2:functions.alkeni , 3:functions.alkini}
def main():
	print 'airchiet tipi: '
	print '1 - alkani'
	print '2 - alkeni'
	print '3 - alkini'
	react = int(input('sheiyvanet ricxvi:'))
	if react in reaction:
		reaction[react]()
	else:
		print 'Error'
	menu()
def menu():
	print "\n-----------------------------"
	print '1 - Tavidan gashveba'
	print '2 - Gamosvla'
	choice = int(raw_input('Airchiet qmedeba: '))
	if choice == 1:
		cls()
		main()
	elif choice == 2:
		sys.exit()
 
main()