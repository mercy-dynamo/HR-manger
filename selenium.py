from selenium import webdriver

# Launch a browser
driver = webdriver.Chrome()  # You may need to specify the path to your Chrome driver

# Open a webpage
driver.get("D:\CODES\myenv\Scripts\flaskiee\templates\index.html")  # Replace "/path/to/your/index.html" with the actual path

# Call a JavaScript function
js_code = "sendMessage();"  # Replace "sendMessage();" with the actual function call you want to execute
driver.execute_script(js_code)
js_code_ = "displayResponse(response);"  # Replace "sendMessage();" with the actual function call you want to execute
driver.execute_script(js_code_)
# Close the browser
driver.quit()