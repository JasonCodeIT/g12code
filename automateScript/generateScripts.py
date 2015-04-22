import json
import time
import os
import random

#open json file

inputFileName = "../output/exploits.json"
scriptFolder = "scripts"+str(int(time.time()))
if not os.path.exists(scriptFolder):
    os.makedirs(scriptFolder)
scriptFileName = "scriptNames.txt"
scriptFile = open(os.path.join(scriptFolder,scriptFileName),'a')


with open(inputFileName) as inputFile:
	inputData = json.load(inputFile)

#extract data from json file
for exploit in inputData:
    scriptName = exploit["name"]
    if not scriptName:
        scriptName = str(int(time.time()+random.randrange(0,int(time.time()))))
    scriptName+=".py"
    scriptPath = os.path.join(scriptFolder,scriptName)
    script = open(scriptPath,"w+")
    func = open('post.py', 'r').readlines()

    script.write("from selenium import webdriver\n")
    script.write("from selenium.webdriver.common.keys import Keys\n\n")
    script.write("driver = webdriver.Firefox()\n\n")

    exploitSteps = exploit["exploit"]
    firstLink = True
    for step in exploitSteps:
        url = step["url"]
        formFields = step["formFields"]
        cookies = step["cookies"]
        if "app8" not in url:
            script.write("driver.get('"+url+"')\n\n")
            script.write("driver.delete_all_cookies()\n\n")
            if cookies:
                for key, value in cookies.items():
                    cookieName = key
                    cookieValue = cookies.get(key)
                    script.write("driver.add_cookie({'name':'"+cookieName+"','value':'"+cookieValue+"'})\n")
                script.write("driver.get('"+url+"')\n\n")
            if formFields:
                fieldName = ""
                fieldValue =""
                for key, value in formFields.items():
                    fieldName = key
                    fieldValue = formFields.get(key)
                    script.write("driver.execute_script('document.getElementsByName(\""+fieldName+"\").value+=\""+fieldValue+"\"')\n")
                script.write("driver.find_element_by_name('"+fieldName+"').submit()\n\n")

        else:
            fieldName = ""
            fieldValue = ""
            for key, value in formFields.items():
                fieldName = key
                fieldValue = formFields.get(key)
                data = "{\""+fieldName+"\":\""+fieldValue+"\"}"
            for key, value in cookies.items():
                cookieName = key
                cookieValue = cookies.get(key)
                cookie = "{\""+cookieName+"\":\""+cookieValue+"\"}"
            script.write("".join(func) + "\n\n")
            script.write("post('"+url+"','"+data+"','"+cookie+"')")

        if (firstLink):
            scriptFile.write("url:"+url+" =>"+scriptName+"\n\n")
            firstLink = False

    script.close()

scriptFile.write("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
scriptFile.close()
