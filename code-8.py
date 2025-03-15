import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# List of URLs to scrape
urls = [
    "https://developer.hdfcsec.com/ir-docs/docs/fetch_access_token_via_api/token_id",
    "https://developer.hdfcsec.com/ir-docs/docs/fetch_access_token_via_api/validate",
    "https://developer.hdfcsec.com/ir-docs/docs/fetch_access_token_via_api/2FA",
    "https://developer.hdfcsec.com/ir-docs/docs/fetch_access_token_via_api/resend2fa",
    "https://developer.hdfcsec.com/ir-docs/docs/fetch_access_token_via_api/authorize",
    "https://developer.hdfcsec.com/ir-docs/docs/fetch_access_token_via_api/access_token",
    "https://developer.hdfcsec.com/ir-docs/docs/user_profile",
    "https://developer.hdfcsec.com/ir-docs/docs/place_order",
    "https://developer.hdfcsec.com/ir-docs/docs/modify_order",
    "https://developer.hdfcsec.com/ir-docs/docs/cancel_order",
    "https://developer.hdfcsec.com/ir-docs/docs/order_status",
    "https://developer.hdfcsec.com/ir-docs/docs/single_order",
    "https://developer.hdfcsec.com/ir-docs/docs/trade_book",
    "https://developer.hdfcsec.com/ir-docs/docs/trade_book_single_trading",
    "https://developer.hdfcsec.com/ir-docs/docs/overall_position",
    "https://developer.hdfcsec.com/ir-docs/docs/holdings",
    "https://developer.hdfcsec.com/ir-docs/docs/fetchltp",
    "https://developer.hdfcsec.com/ir-docs/docs/funds_and_margins",
]

try:
    # Initialize Selenium WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(10)  # Wait for elements to load

    all_api_urls = []  # Store all extracted API URLs

    for url in urls:
        print(f"Scraping: {url}")
        driver.get(url)

        time.sleep(2)  # Add a small delay to allow content to load properly

        # Find all elements containing API URLs
        code_elements = driver.find_elements(By.XPATH, "//pre/code")

        for code_element in code_elements:
            text = code_element.text.strip()
            if "http" in text:  # Filter only API URLs
                all_api_urls.append(f"URL: {url}\n{text}\n")

    # Save extracted API URLs to a file
    with open("all_api_urls.txt", "w") as f:
        f.writelines("\n".join(all_api_urls))

    print("Extracted API URLs saved to 'all_api_urls.txt'")

    driver.quit()  # Close the browser

except Exception as e:
    print(f"Error: {e}")
    if 'driver' in locals():
        driver.quit()  # Ensure the browser is closed even if an error occurs
