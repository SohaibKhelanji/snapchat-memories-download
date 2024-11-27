import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Ask the user for the path to Chrome browser executable
chrome_browser_path = input("Enter the full path to your Chrome browser executable (e.g., C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe): ")

# Ask the user for the path to ChromeDriver executable
chromedriver_path = input("Enter the full path to your ChromeDriver executable (e.g., C:\\path\\to\\chromedriver.exe): ")

# Ask the user for the path to the local HTML file
html_file_path = input("Enter the full path to the HTML file you want to open (e.g., C:\\path\\to\\file.html): ")

# Setup Chrome options for Chrome
options = Options()
options.binary_location = chrome_browser_path  # Point to the Chrome executable

# Setup Selenium WebDriver with custom ChromeDriver path for Chrome
service = Service(chromedriver_path)

# Initialize WebDriver with the custom driver path
driver = webdriver.Chrome(service=service, options=options)

# Open the local HTML file in Chrome
driver.get("file://" + html_file_path)

# Wait for the page to fully load
time.sleep(2)  # You may need to adjust the wait time depending on the page load time

# Find all <a> tags on the page
links = driver.find_elements(By.TAG_NAME, 'a')

# Click each link
for index, link in enumerate(links):
    href = link.get_attribute('href')
    
    # Filter to click only download links (those with 'downloadMemories' in the href)
    if href and 'downloadMemories' in href:
        print(f"Clicking link {index + 1}: {href}")
        link.click()
        
        # Wait a bit for the download to start (adjust based on the file size and server response)
        time.sleep(3)

# Close the browser after processing all links
driver.quit()
