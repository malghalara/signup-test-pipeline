from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import random
import string

# Configure headless Chrome
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
driver = webdriver.Chrome(options=options)

BASE_URL = "http://13.60.169.207:8081/index.php"

def generate_random_user():
    suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=5))
    return {
        "first_name": f"Test{suffix}",
        "last_name": "User",
        "username": f"user{suffix}",
        "email": f"user{suffix}@example.com",
        "password": "Test@1234"
    }

def fill_form_and_submit(user):
    driver.get(BASE_URL)
    driver.find_element(By.NAME, "first_name").send_keys(user["first_name"])
    driver.find_element(By.NAME, "last_name").send_keys(user["last_name"])
    driver.find_element(By.NAME, "username").send_keys(user["username"])
    driver.find_element(By.NAME, "email").send_keys(user["email"])
    driver.find_element(By.NAME, "password").send_keys(user["password"])
    driver.find_element(By.NAME, "confirm_password").send_keys(user["password"])
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

def assert_success_message():
    try:
        time.sleep(2)
        success_element = driver.find_element(By.CLASS_NAME, "alert-success")
        assert "Account created successfully!" in success_element.text
        print("✅ Test Passed: Signup success message displayed.")
    except NoSuchElementException:
        print("❌ Test Failed: Success message not found.")

def test_successful_signup():
    user = generate_random_user()
    fill_form_and_submit(user)
    assert_success_message()

def run_tests():
    print("🚀 Starting automated signup tests...\n")
    for i in range(10):
        print(f"🧪 Running test #{i+1}")
        test_successful_signup()
    driver.quit()
    print("\n✅ All tests completed.")

if __name__ == "__main__":
    run_tests()
