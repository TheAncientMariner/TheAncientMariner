#Kataskeui sinartisis i opoia psaxnei pia imera tis ebdomadas einai i imerominia pou dinei o xristis

def Imerominia(mera,minas,xronia):
	""" Tin formula me tin opoia tha ipologiso tin imera tis ebdomadas tin vrika sto wikipedia 
		kai sigkekrimena https://en.wikipedia.org/wiki/Zeller%27s_congruence"""

	q = mera
	
	"""minas 3=Martios ... 14=Febrouarios, 
		auto isxuei gia tin formula,
		o xristis pliktrologei kanonika, p.x gia ton xristi o febrouarios einai to 2"""
		
	if minas == 1:
		minas = 13
		xronia = xronia - 1
	elif minas == 2:
		minas = 14
		xronia = xronia - 1
	
	#K einai year mod 100
	K = xronia % 100
	J = xronia // 100
	#h einai i formula 
	h = (q + int(13*(minas + 1)/5.0) + K + int(K/4.0) + int(J/4.0) - 2 * J) % 7
	
	if h == 0:
		h = 7
		
	return h	
	

#Kataskeui kiriou programmatos

mera, minas, xronia = [int(x) for x in raw_input("Pliktrogiste tin imerominia pou thelete, me morfi mera/minas/xronia, gia na sas epistrepsoume ti mera ebdomadas: ").split('/')]

#Klisi sinartisis
h = Imerominia(mera,minas,xronia)

if h==1:
	h = "KYRIAKH"
elif h==2:
	h = "DEYTERA"
elif h==3:
	h = "TRITH"
elif h ==4:
	h = "TETARTH" 	
elif h==5:
	h = "PEMPTH"
elif h==6:
	h = "PARASKEYH"
else:
	h = "SABBATO"

if minas==0 or mera==0 or xronia==0:
	print """Den iparxei minas, mera, i xronia pou na antistoixei sto noumero '0'"""
	
elif minas>12 or mera>31:
	print "I imerominia auti den iparxei"

else:
	print h
		
		
