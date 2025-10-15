from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

EMAIL = "3300dulcie@tiffincrane.com"
PASSWORD = "Securepassword123@"
LOGIN_URL = "https://app.staging.thebillstation.com/auth/login/"

def test_login_and_logout_flow():
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Uncomment if you want headless mode
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get(LOGIN_URL)

    wait = WebDriverWait(driver, 15)

    try:
        # ==== LOGIN PAGE ====

        email_xpath = "/html/body/div/main/section[2]/div/form/div[1]/div[2]/div/input"
        email_input = wait.until(EC.presence_of_element_located((By.XPATH, email_xpath)))
        email_input.clear()
        email_input.send_keys(EMAIL)

        password_xpath = "/html/body/div/main/section[2]/div/form/div[2]/div/input"
        password_input = wait.until(EC.presence_of_element_located((By.XPATH, password_xpath)))
        password_input.clear()
        password_input.send_keys(PASSWORD)

        login_button_xpath = "/html/body/div/main/section[2]/div/form/button"
        login_button = wait.until(EC.element_to_be_clickable((By.XPATH, login_button_xpath)))
        login_button.click()

        # ==== DASHBOARD PAGE ====
        wait.until(EC.url_contains("/dashboard"))
        print("✅ Dashboard is visible.")

        # === WALLET BALANCE ===
        wallet_balance_xpath = (
            "/html/body/div/main/section/div/div/div[1]/div[1]/div[2]/div[1]/p"
        )

        wallet_balance = wait.until(
            EC.visibility_of_element_located((By.XPATH, wallet_balance_xpath))
        )
        assert wallet_balance.is_displayed(), "Wallet balance is not visible."
        balance_text = wallet_balance.text
        print("✅ Wallet balance is visible. Value:", balance_text)


        # ==== LOGOUT ====

        logout_button_xpath = "/html/body/div/main/div/div[2]/a[8]"
        logout_button = wait.until(EC.element_to_be_clickable((By.XPATH, logout_button_xpath)))
        logout_button.click()

        # ==== LOGOUTFinal ====
        logoutFinal_button_xpath = "/html/body/div[3]/div[3]/button[2]"
        logoutFinal_button = wait.until(EC.element_to_be_clickable((By.XPATH, logoutFinal_button_xpath)))
        logoutFinal_button.click()

        wait.until(EC.presence_of_element_located((By.XPATH, email_xpath)))
        print("✅ Successfully logged out.")

    except Exception as e:
        print(f"❌ Test failed: {e}")
        raise

    finally:
        time.sleep(2)
        driver.quit()


if __name__ == "__main__":
    test_login_and_logout_flow()
