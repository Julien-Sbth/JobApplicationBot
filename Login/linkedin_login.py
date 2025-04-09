from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import os
from dotenv import load_dotenv

load_dotenv()
EMAIL = os.getenv("LINKEDIN_EMAIL")
PASSWORD = os.getenv("LINKEDIN_PASSWORD")


def linkedin_login(app):
    print("🔵 Tentative de connexion à LinkedIn...")
    try:
        app.driver.get("https://www.linkedin.com/login")

        username_input = app.wait.until(
            EC.presence_of_element_located((By.ID, "username"))
        )
        password_input = app.driver.find_element(By.ID, "password")

        username_input.clear()
        username_input.send_keys(EMAIL)
        password_input.clear()
        password_input.send_keys(PASSWORD + Keys.RETURN)

        app.wait.until(EC.url_contains("/feed"))
        print("✅ Connecté à LinkedIn avec succès")
        return True

    except TimeoutException:
        print("❌ Échec de la connexion à LinkedIn: Timeout")
    except NoSuchElementException as e:
        print(f"❌ Élément introuvable : {e}")
    except Exception as e:
        print(f"❌ Erreur inattendue : {e}")

    return False
