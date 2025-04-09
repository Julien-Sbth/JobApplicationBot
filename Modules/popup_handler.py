from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
class PopupHandler:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def handle_popups(self):
        try:
            cookie_popup = self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".phs-widget-block-area")
                )
            )
            self.driver.execute_script("arguments[0].remove();", cookie_popup)
            print("🚫 Pop-up de cookies fermé")
        except:
            pass

        try:
            alert = self.wait.until(EC.alert_is_present())
            alert_text = alert.text
            print(f"🔔 Alerte détectée : {alert_text}")
            alert.accept()
            print("✅ Alerte fermée avec succès")
        except:
            pass
