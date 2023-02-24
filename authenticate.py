import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def lambda_handler(event, context):
    url = event['url']
    
    # Configure ChromeOptions to run headless and in a Lambda environment
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--window-size=1280,800')
    
    chrome_driver_path = os.path.join(os.getcwd(), 'bin', 'chromedriver')
    # Instantiate ChromeDriver
    driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)
    
    # Navigate to the login URL and wait for the user to manually authenticate
    driver.get(url)
    time.sleep(60)  # Wait for 60 seconds for the user to authenticate manually
    
    # Extract the authenticated URL from the browser and return it
    authenticated_url = driver.current_url
    
    # Clean up the ChromeDriver and return the authenticated URL
    driver.quit()
    return {'authenticated_url': authenticated_url}
