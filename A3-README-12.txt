VM1
Contains:	scanner, results + outputs on public benchmark & own benchmark

MD5-Hash:	

Credentials:
	Username:auditor
	Password:auditor

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
	Username:user
	Password:user

Details:
	Each benchmark is located under an "ownX" folder in /var/www/, "X" represents the number of the benchmark.
	We have 11 benchmark in total, hence in /var/www/ there will be "own1" to "own11" folders.
	The vulnerability of each benchmark is in a README file under their specific folders, for instance:
		own1 vulnerability is under /var/www/own1.com/public_html/README
	We also included the vulnerability for each benchmark below for reference:
		own1:
			To get passwd:	..././..././..././..././..././/etc/passwd
		
		own2:
			Front-end JavaScript blocks ../, but the DT is through the Language. (../../../../etc/passwd)
	
		own3:
			The 2 variables append to each other: (GET REQUEST)
			path=../../../../
			file=/etc/passwd
	

		own5:
			passwd file printed in iframe. The form input is:
			../../../../etc/passwd
		
		own6:
			No DT here. Test-case for False positive
		
		own7:	
			Username: own7
			Password: own7
			$_COOKIE["UserDetails"] = '../../../../..//etc/passwd';
		
		own8:
			Hidden Variable in form:
			hiddenvalue
			Value:
			../../../../..//etc/passwd
		
		own9:
			Post Variables:
			$_POST['FILE_PATH'] = "../../../../../..//etc/passwd";
			$_FILES['file']['name'] = "";

		own10:
			Cannot use '../'
			Use '..%2F' instead
			..%2F..%2F..%2F..%2F..%2Fetc%2Fpasswd

		own11:
			Log into admin to do file traversal
			User: admin
			Password: admin
			Other account:
			User: user
			Password: user
			../../../../../etc/passwd
			


		


			

			

	


