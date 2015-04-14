import json
import time
import os
import random
import re

#open json file

inputFileName = "exploitData.json"
scriptFileName = "scriptNames.txt"
if not os.path.exists("scripts"):
    os.makedirs("scripts")
scriptFile = open(os.path.join("scripts",scriptFileName),'a')

with open(inputFileName) as inputFile:
	inputData = json.load(inputFile)

#extract data from json file
exploits = inputData['exploits']

for exploit in exploits:
    url = exploit["url"]
    loginCredentials = exploit["loginCredentials"]
    credentialsFields = exploit["credentialFields"]
    exploitUrl =exploit["exploiturl"]
    if "exploitName" in exploit:
        scriptName = exploit["name"]
    else:
        scriptName = str(int(time.time()+random.randrange(1,int(time.time()))))   #name of script is timestamp to ensure uniqueness


    for cred in loginCredentials:
        username = cred['username']
        password = cred['password']

    for field in credentialsFields:
        usernameBox = field['usernameBox']
        passwordBox = field['passwordBox']

    if username != "":
        needLogin = True
    else:
        needLogin = False

    importString = "import json\nfrom selenium import webdriver\nfrom selenium.webdriver.common.keys import Keys\n"
    url = "'"+url+"'"
    openBrowser = "driver = webdriver.Firefox()\ndriver.get("+url+")\n"
    username = "'"+username+"'"
    password = "'"+password+"'"
    login = "usernameField.send_keys("+username+")\npasswordField.send_keys("+password+")\nusernameField.send_keys(Keys.RETURN)\n"
    exploitUrl = "'"+exploitUrl+"'"
    attack = "driver.get("+exploitUrl+")\n"
    scriptName = scriptName+".py"

    scriptPath = os.path.join("scripts",scriptName)
    with open(scriptPath,"w+") as script:
        script.write(importString)
        script.write(openBrowser)
        if needLogin:
	    script.write(login)
        script.write(attack)
        script.close()
    scriptFile.write("url:"+url+" =>"+scriptName+"\n")

scriptFile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
scriptFile.close()
