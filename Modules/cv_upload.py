from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
class CVUpload:
    def __init__(self, driver, wait, cv_path):
        self.driver = driver
        self.wait = wait
        self.cv_path = cv_path

    def handle_cv_upload(self):
        print("🔄 Traitement de l'upload de CV...")

        current_url = self.driver.current_url
        print(f"🌐 URL actuelle : {current_url}")

        try:
            self.handle_linkedin_apply_option()

            if "soprasteria" in current_url:
                print("🏢 Entreprise détectée : Sopra Steria")

                label = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "label[for='file-input']"))
                )
                self.driver.execute_script("arguments[0].click();", label)
                print("🖱️ Clic sur la zone de dépôt effectué (Sopra Steria)")

                file_input = self.wait.until(
                    EC.presence_of_element_located((By.ID, "file-input"))
                )
                file_input.send_keys(self.cv_path)
                print(f"✅ CV envoyé (Sopra Steria) : {self.cv_path}")

            elif "thales" in current_url:
                print("🏢 Entreprise détectée : Thales")

                wrapper = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "div.resume-upload-wrapper"))
                )
                file_input = wrapper.find_element(By.CSS_SELECTOR, "input[type='file']")
                upload_button = wrapper.find_element(By.CSS_SELECTOR, "button.upload-resume-btn")

                self.scroll_into_view(upload_button)
                upload_button.click()
                time.sleep(1)
                file_input.send_keys(self.cv_path)
                print(f"✅ CV uploadé (Thales) : {self.cv_path}")

            elif "bpce" in current_url:
                print("🏢 Entreprise détectée : BPCE")

                file_input = self.wait.until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, "input#cv-upload"))
                )
                file_input.send_keys(self.cv_path)
                print(f"✅ CV uploadé (BPCE) : {self.cv_path}")

            else:
                print("❓ Aucune entreprise connue détectée dans l'URL. Upload ignoré.")
                return False

            try:
                alert = self.driver.switch_to.alert
                alert_text = alert.text
                print(f"🔔 Alerte détectée : {alert_text}")
                alert.accept()
                print("✅ Alerte fermée avec succès")
            except:
                pass

            return self.verify_upload_success()

        except Exception as e:
            print(f"❌ Erreur lors de l'upload: {str(e)}")
            self.driver.save_screenshot("upload_error.png")
            return False

    def handle_linkedin_apply_option(self):
        try:
            apply_linkedin_btn = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "button#apply-with-linkedin")
                )
            )
            self.scroll_into_view(apply_linkedin_btn)
            apply_linkedin_btn.click()
            print("✅ Clic sur 'Apply With LinkedIn'")
            time.sleep(3)
        except TimeoutException:
            print("ℹ️ Bouton 'Apply With LinkedIn' non trouvé, poursuite du processus")

    def scroll_into_view(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});",
            element,
        )
        time.sleep(1)

    def verify_upload_success(self):
        try:
            self.wait.until(
                EC.presence_of_element_located(
                    (By.CSS_SELECTOR, ".resume-upload-wrapper .file-name")
                )
            )
            print("✨ CV correctement uploadé et validé")
            return True
        except TimeoutException:
            print("⚠️ Upload peut-être réussi mais confirmation non détectée")
            return True
