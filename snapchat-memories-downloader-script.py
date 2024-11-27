import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


chrome_browser_path = input("Enter the full path to your Chrome browser executable (e.g., C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe): ")


chromedriver_path = input("Enter the full path to your ChromeDriver executable (e.g., C:\\path\\to\\chromedriver.exe): ")

# The memories_history.html file
html_file_path = input("Enter the full path to the HTML file you want to open (e.g., C:\\path\\to\\file.html): ")

options = Options()
options.binary_location = chrome_browser_path  # Point to the Chrome executable


service = Service(chromedriver_path)


driver = webdriver.Chrome(service=service, options=options)


driver.get("file://" + html_file_path)


time.sleep(2)  # You may need to adjust the wait time depending on the page load time


links = driver.find_elements(By.TAG_NAME, 'a')


for index, link in enumerate(links):
    href = link.get_attribute('href')
    
    # Filter to click only download links (those with 'downloadMemories' in the href)
    if href and 'downloadMemories' in href:
        print(f"Clicking link {index + 1}: {href}")
        link.click()
        
        # Wait a bit for the download to start (adjust based on the file size and server response)
        time.sleep(3)


driver.quit()
