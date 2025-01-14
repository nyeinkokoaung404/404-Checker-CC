import re
def reg(cc):
	import requests
	cc=cc.strip()
	n = cc.split("|")[0]
	mm = cc.split("|")[1]
	yy = cc.split("|")[2]
	cvc = cc.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()
	return cc
	