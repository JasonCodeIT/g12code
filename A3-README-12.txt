VM1
Contains:	scanner, results + outputs on public benchmark & own benchmark

MD5-Hash:	

Credentials:
	Username:
	Password:

Scanner Details:
	Source code location:
	
	How to compile:
		No compilation needed
	
	How to use:
		To enter start_url, account credentials, after_login_url and name of exploit file:
			Please proceed to settings.py under the folder "Scrape" and fill in those information. An example for the format is commented out in settings.py for your convienence
		
		To run:
			Please run the python file:
		
		To view/run the generated exploit scripts:
			Please proceed to the "Scriptsxxxxxxxxxx" folder, under the scripts folder, there will be a scriptsNames.txt file alone with numerous python scripts.
				Note that a different "Scriptsxxxxxxxxxx" folder will be auto generated whenever the user run the scanner

			Each python script is an exploit for an application. Simply run the python script to view the automated exploit.
			
			The scriptNames.txt file will contain the first url to script name mapping of each exploit.
			If the exploit name is not provided	(empty string), a random name will generated for that exploit.
			For instance, in the public benchmark, the first url for app7 is "url:https://app7.com/oc-admin/index.php?page=login".
			If an exploit name if provided for instance exploit-1, the mapping will be:
				"url:https://app7.com/oc-admin/index.php?page=login =>exploit-1.py"
			else, it will look something like this:
				"url:https://app7.com/oc-admin/index.php?page=login =>2142579065.py"

	Other requirements:
		Please ensure that the following programs are downloaded:
			Python version 2.7.x
			Selenium
			Scrapy




VM2
Contains:	group 12 benchmark and documentation

MD5-Hash:

Credentials:
	Username:
	Password:


