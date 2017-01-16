# **CrunchyrollChecker**
A simple Python script that checks a list of Crunchyroll accounts for working/premium ones.
It's multithreaded and uses a Cloudflare bypass on each thread so there's no interruption.

---
###**Account list example**

	account1@email.com:password1
	account2@email.com:password2
	account3@email.com:password3
	...
	
---
###**Usage**
	crunchyrollchecker.py [accountlistfile] [numberofthreads]

It will start running and will save all working accounts on the **justworking.txt** file and premium accounts on the **workingandpremium.txt** file.

---
###**Dependencies**
	Tested and working on Python 3.5.2
	
	Requests:
	pip install requests
	
	CFscrape:
	pip install cfscrape
	
	BeautifulSoup:
	pip install beautifulsoup4

---
###**Pre-packaged Executable**
CrunchyrollChecker is also avaliable as a pre-packaged self extracting executable, so you don't need to install Python or any one of the dependencies.
Download the latest executable version here: [click here to download](http://files.joaovitorbf.net/CrunchyrollChecker.exe)
>**Warning: place the executable on a empty folder, it will unpackage everything automatically once you run it, throwing files everywhere.**

---
###**License**
The software is licensed under the MIT License.
You can also find it inside the license file.

    Copyright 2017 João Vitor B. F.

	Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated 
	documentation files (the "Software"), to deal in the Software without restriction, including without limitation the 
	rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
	and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
	
	The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
	
	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT 
	NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. 
	IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION 
	WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
