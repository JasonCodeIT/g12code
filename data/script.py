from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import json

steps = json.loads('{{{ steps }}}')

driver = webdriver.Firefox()

counter = 0
for step in steps:
    method = step['method']
    url = step['url']
    form_fields = step['formFields']
    cookies = step['cookies']

    driver.get(url)

    '''
    if counter == 0:
        driver.delete_all_cookies()

        if cookies:
            for name, value in cookies.items():
                driver.add_cookie({'name': name, 'value': value})

        driver.get(url)
    '''

    if method in ['GET', 'POST'] and form_fields:
        submit = None
        for name, value in form_fields.items():
            elem = driver.find_element_by_name(name)
            input_type = elem.get_attribute('type')

            if input_type in ['text']:
                submit = elem

            if input_type == 'file':
                elem.send_keys(value)
            else:
                driver.execute_script('''
                    var elem = arguments[0];
                    var value = arguments[1];
                    elem.value = value;
                ''', elem, value)
        submit.send_keys(Keys.RETURN)

    elif method in ['COOKIE'] and form_fields:
        for name, value in form_fields.items():
            driver.delete_cookie(name)
            driver.add_cookie({'name': name, 'value': value})
