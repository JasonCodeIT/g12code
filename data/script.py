from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

steps = json.loads('{{{ steps }}}')

counter = 0
for step in steps:
    url = step['url']
    form_fields = step['formFields']
    cookies = step['cookies']

    driver = webdriver.Firefox()

    driver.get(url)

    if counter == 0:
        driver.delete_all_cookies()

        if cookies:
            driver.add_cookie(cookies)

        driver.get(url)

    if form_fields:
        for name, value in form_fields.items():
            elem = driver.find_element_by_name(name)
            driver.execute_script('''
                var elem = arguments[0];
                var value = arguments[1];
                elem.value = value;
            ''', elem, value)
        elem.submit()
