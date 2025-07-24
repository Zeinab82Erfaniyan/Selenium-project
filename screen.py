from selenium import webdriver

#set path for driver
path = 'C://webdriver/screen.png'

b = webdriver.Chrome()

b.get("https://myninja.ai/")
print ("***************")
print (b.title)
print (b.current_url)
print ("***************")

#save screen
try:  
   b.save_screenshot(path)  
   print("successfully")

except Exception as e:  
   print(f"Error")
   

