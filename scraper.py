from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up Selenium WebDriver with options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode (no browser UI)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

# Load the webpage
url = 'https://www.worldaic.com.cn/wangjie?year=2023'
driver.get(url)

# Wait for the page to fully load and for JavaScript to populate the content
time.sleep(10)  # Increase or decrease this based on page load time

# Extract the rendered HTML
html = driver.page_source

# Parse the page source with BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Now find the dynamic content (attendance records)
# You will need to inspect the rendered page to locate the correct elements
attendance_records = soup.find_all('div')  # Adjust based on actual structure in rendered HTML

# Process and print attendance records
for record in attendance_records:
    print(record.text)  # Adjust as necessary to extract relevant information

# Close the WebDriver
driver.quit()
