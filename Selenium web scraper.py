from bs4 import BeautifulSoup
import json
from bs4 import BeautifulSoup
from selenium import webdriver
import selenium
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import json
import requests

options = webdriver.ChromeOptions()

options.add_argument('--disable-blink-features=AutomationControlled')
options.add_argument("--headless") #allows the execution of a full version of the Chrome Browser
options.add_argument("--enable-javascript")


final_data = []
with open('data.json', 'w') as json_file:
    for page in range(1,15): #number of pages to check
           
      url = f"https://example site/{page}"
      
      #site was camplace.com, but it redirects to this site
      response = requests.get(url)
      if response.status_code == 200:
            options = webdriver.Chrome()
            #use Chrome as the main browser

            options.get(url)
            print(f"Page {page} loaded successfully")
            options.quit()
      else:
            print(f"Page {page} did not return a status code of 200")
            break
      
      bt = options.find_element(By.XPATH, '//*[@id="app"]/div/div/div/div/div[3]/button')
      bt.click()
      #Finds the location of a necessary button and clicks it


      
      wait = WebDriverWait(options, 15)
      #not necessary to wait that much, but my pc is slow

      bs = BeautifulSoup(options.page_source,'html.parser') 
      #get the web page as html string
      
      divs = bs.find('div', id="app" ) #find where the data is

      string = divs.get_text(" ", strip=True)
      data_list = string.split()
      #split the data from the html into an list of strings
      
      for i in range(0,len(data_list)):      
      #parse the unnecessary data

        if data_list[i] == "X" and data_list[i+1]=="Y":        
            start=i+2   # where the desired Data start
         
        if data_list[i] == "1" and data_list[i+1]=="2":      
            end = i-2  # where the desired Data ends
         
            for i in range(start, end):
               #what will be sent to the json file

               if  data_list[i+2] == "Example1" and data_list[i+3] == "Example2":
                  
                  final_data.append(str(data_list[i]) + " - Example1+Example2 ")
                  StopIteration

               elif data_list[i].isdigit() or data_list[i] == "Example1" or data_list[i] == "Example2":
                  pass
               
               else:
                  
                  final_data.append(str(data_list[i]) + " - Appended correctly")         
   
    json.dump((final_data), json_file,  separators=(',\n', ': '),indent=2)
    #send the data in a more readable manner

json_file.close()