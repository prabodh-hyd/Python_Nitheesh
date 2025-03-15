from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

url = "https://developer.hdfcsec.com/ir-docs/docs/fetch_access_token_via_api/token_id"

try:
    # Use Selenium to handle potential dynamic content
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(url)

    # Wait for the element to load (you might need to adjust the wait time)
    driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to load

    # Find the element using the provided XPath
    code_element = driver.find_element(By.XPATH, "/html/body/div/div[2]/div/div/main/div/div/div/div/article/div[2]/div[1]/div/pre/code")

    api_url = code_element.text.strip()
    print("API URL:", api_url)

    with open("api_url.txt", "w") as f:
        f.write(api_url)
    print("API URL saved to 'api_url.txt'")

    driver.quit()  # Close the browser

except Exception as e:
    print(f"Error: {e}")
    if 'driver' in locals():
        driver.quit()  # Ensure the browser is closed even if an error occurs