import time
from Configuration.config import LINKEDIN_JOB_URL, CV_PATH
from Configuration.browser_setup import initialize_driver
from AutomationCore.company_detection import CompanyDetection
from Modules.popup_handler import PopupHandler
from Modules.cv_upload import CVUpload
from Login.linkedin_login import linkedin_login
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class LinkedInJobApplication:
    def __init__(self):
        self.driver, self.wait = initialize_driver()
        self.company_detection = CompanyDetection(self.driver, self.wait)
        self.popup_handler = PopupHandler(self.driver, self.wait)
        self.cv_upload = CVUpload(self.driver, self.wait, CV_PATH)

    def navigate_to_job(self):
        print("🔵 Navigation vers l'offre d'emploi...")
        self.driver.get(LINKEDIN_JOB_URL)

        try:
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".jobs-apply-button"))
            )
            return True
        except TimeoutException:
            print("❌ Impossible d'accéder à l'offre d'emploi")
            return False

    def handle_application(self):
        try:
            apply_button = self.driver.find_element(
                By.CSS_SELECTOR, ".jobs-apply-button"
            )
            self.driver.execute_script("arguments[0].click();", apply_button)
            print("✅ Clic sur 'Postuler' dans LinkedIn")
            time.sleep(3)

            self.driver.switch_to.window(self.driver.window_handles[-1])
            print(f"🔵 Nouvel onglet ouvert : {self.driver.current_url}")

            self.popup_handler.handle_popups()

            if not self.company_detection.detect_company_and_apply(self.driver.current_url):
                if not self.access_application_page():
                    return False

            if not self.verify_application_form():
                return False

            return self.cv_upload.handle_cv_upload()

        except Exception as e:
            print(f"❌ Erreur lors du processus de candidature: {str(e)}")
            return False

    def access_application_page(self):
        try:
            apply_url = self.company_detection.get_apply_url()
            self.driver.get(apply_url)
            print("🔗 Accès direct à la page de candidature")
            return True
        except:
            try:
                apply_now_button = self.wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//a[@data-ph-at-id='apply-link']")
                    )
                )
                self.driver.execute_script("arguments[0].click();", apply_now_button)
                print("✅ Clic forcé sur 'Apply Now'")
                return True
            except Exception as e:
                print(f"❌ Impossible d'accéder à la page de candidature: {str(e)}")
                return False

    def verify_application_form(self):
        try:
            self.wait.until(EC.presence_of_element_located((By.TAG_NAME, "form")))
            print("🔵 Formulaire de candidature détecté")
            return True
        except TimeoutException:
            print("❌ Formulaire de candidature non détecté")
            return False

    def run(self):
        try:
            if not linkedin_login(self):
                return

            if not self.navigate_to_job():
                return

            if self.handle_application():
                print("✨ Candidature envoyée avec succès !")
            else:
                print("❌ Échec lors du processus de candidature")

        except Exception as e:
            print(f"❌ Erreur critique: {str(e)}")

        finally:
            time.sleep(5)
            self.driver.quit()