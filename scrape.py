import time
from selenium import webdriver
from selenium.webdriver.common.by import By

options = webdriver.ChromeOptions()
options.debugger_address = "127.0.0.1:9222"
driver = webdriver.Chrome(options=options)

elements = driver.find_elements(By.CSS_SELECTOR, "tr[id^='posting']")

for i, tr in enumerate(elements):
    try:
        td = tr.find_element(By.CSS_SELECTOR, "td.orgDivTitleMaxWidth.align--middle")
        a = td.find_element(By.TAG_NAME, "a")

        main_window = driver.current_window_handle  
        a.click()  
        time.sleep(5) 
        
        driver.switch_to.window(driver.window_handles[-1])
        
        posting = driver.find_element(By.ID, "postingDiv")

        with open(f"postings/posting_{i}.txt", "w") as f:
            f.write(posting.text)
        print(i/len(elements)*100)
        driver.close()
        
        driver.switch_to.window(main_window)
        time.sleep(2)  
            
    except Exception as e:
        print(f"Error finding elements in tr or handling windows: {e}")
            