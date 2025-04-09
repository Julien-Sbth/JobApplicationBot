import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, ElementClickInterceptedException,
    NoSuchElementException, WebDriverException
)
from Configuration.config import LINKEDIN_JOB_URL, ENTERPRISES, CV_PATH

class CompanyDetection:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def detect_company_and_apply(self, job_url):
        for company, details in ENTERPRISES.items():
            if any(keyword.lower() in job_url.lower()
                   for keyword in details.get("url_keywords", [])):
                print(f"🔵 Entreprise détectée : {company.capitalize()}")

                try:
                    if hasattr(self, details["special_action"]):
                        method = getattr(self, details["special_action"])
                        return method(details.get("apply_button_selector"))

                    return self.default_application_flow(details.get("apply_button_selector"))

                except WebDriverException as e:
                    print(f"❌ Erreur WebDriver lors du traitement {company}: {str(e)}")
                    return False
                except Exception as e:
                    print(f"❌ Erreur inattendue avec {company}: {str(e)}")
                    return False

        print("🟡 Aucune entreprise reconnue - flux générique")
        return False

    def default_application_flow(self, selector=None):
        try:
            if selector:
                apply_btn = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, selector)))
                self.driver.execute_script("arguments[0].click();", apply_btn)
            else:
                apply_btn = self.wait.until(
                    EC.element_to_be_clickable(
                        (By.XPATH, "//button[contains(.,'Postuler') or contains(.,'Apply')]")))
                self.driver.execute_script("arguments[0].click();", apply_btn)

            time.sleep(2)
            return True
        except Exception as e:
            print(f"❌ Échec du flux par défaut: {str(e)}")
            return False

    def navigate_to_thales_application_page(self, apply_button_selector):
        print("🔵 Navigation vers la page de candidature de Thales...")

        try:
            apply_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, apply_button_selector))
            )
            self.driver.execute_script("arguments[0].click();", apply_button)
            print("✅ Clic sur 'Postuler' pour Thales")
            time.sleep(3)
            return True
        except TimeoutException:
            print("❌ Impossible de trouver le bouton de candidature pour Thales")
            return False
        except Exception as e:
            print(f"❌ Erreur Thales: {str(e)}")
            return False

    def navigate_to_bpce_application_page(self, apply_button_selector):
        print("🔵 Navigation vers la page de candidature BPCE...")
        try:
            apply_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, apply_button_selector)))
            self.driver.execute_script("arguments[0].click();", apply_button)
            print("✅ Clic sur 'Postuler' pour BPCE")

            self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, ".bpce-form")))

            print("🔵 Tentative d'import des données du CV...")
            try:
                cv_button = self.wait.until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, ".apply-cv-button"))
                )
                self.driver.execute_script("arguments[0].click();", cv_button)
                print("✅ Bouton d'import CV cliqué avec succès")

                # Upload automatique du CV
                file_input = self.driver.find_element(By.CSS_SELECTOR, ".extract-data-from-cv")
                file_input.send_keys(CV_PATH)
                print(f"📎 CV uploadé: {CV_PATH}")

            except TimeoutException:
                print("⚠️ Bouton d'import CV non trouvé (peut-être optionnel)")
            except Exception as e:
                print(f"⚠️ Erreur lors de l'upload du CV: {str(e)}")

            return True

        except TimeoutException as e:
            print(f"❌ Erreur lors de la navigation BPCE: {str(e)}")
            return False

    def navigate_to_sopra_steria_application_page(self, selector=None):
        print("🔵 Navigation vers la page de candidature de Sopra Steria...")

        try:
            apply_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'a#st-apply.button.js-oneclick'))
            )
            self.driver.execute_script("arguments[0].click();", apply_button)
            print("✅ Clic sur 'Je suis intéressé(e)' effectué")
            time.sleep(3)

            email = "julien.sabathe@ynov.com"
            email_input = self.wait.until(
                EC.visibility_of_element_located((By.ID, "email-input"))
            )
            email_input.send_keys(email)

            email_confirm_input = self.wait.until(
                EC.visibility_of_element_located((By.ID, "confirm-email-input"))
            )
            email_confirm_input.send_keys(email)

            self.driver.execute_script("arguments[0].scrollIntoView(true);", email_input)
            print("✅ Adresse e-mail remplie")

            drop_label = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "label[for='file-input'] span.c-spl-dropzone-label-browse"))
            )
            self.driver.execute_script("arguments[0].click();", drop_label)
            print("🖱️ Clic sur le label 'Choisissez un fichier' effectué")

            file_input = self.wait.until(
                EC.presence_of_element_located((By.ID, "file-input"))
            )
            file_input.send_keys(CV_PATH)
            print(f"📎 Fichier PDF envoyé : {CV_PATH}")

            submit_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.c-spl-button--primary"))
            )
            self.driver.execute_script("arguments[0].click();", submit_button)
            print("✅ Clic sur le bouton de soumission effectué")

            print("🎉 Candidature Sopra Steria terminée")
            return True

        except Exception as e:
            print(f"❌ Erreur Sopra Steria : {str(e)}")
            return False

    def navigate_to_orange_application_page(self, _=None):
        print("🔵 Traitement Orange...")
        try:
            apply_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "detail-apply")))

            try:
                apply_button.click()
            except ElementClickInterceptedException:
                self.driver.execute_script("arguments[0].click();", apply_button)

            partner_link = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, ".dropdown-menu .item a")))
            partner_href = partner_link.get_attribute("href")

            self.driver.execute_script(f"window.open('{partner_href}', '_blank');")
            self.driver.switch_to.window(self.driver.window_handles[-1])

            return True

        except (TimeoutException, NoSuchElementException) as e:
            print(f"❌ Échec du processus Orange: {str(e)}")
            return False

    def navigate_to_airbus_application_page(self, apply_button_selector):
        print("🔵 Traitement Airbus...")
        try:
            apply_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "a.css-9jcgd5[role='button']"))
            )
            self.driver.execute_script("arguments[0].click();", apply_button)
            print("✅ Clic sur 'Apply' effectué")
            time.sleep(3)

            email = "julien.sabathe@ynov.com"
            email_input = self.wait.until(
                EC.visibility_of_element_located((By.ID, "email-input"))
            )
            email_input.send_keys(email)

            email_confirm_input = self.wait.until(
                EC.visibility_of_element_located((By.ID, "confirm-email-input"))
            )
            email_confirm_input.send_keys(email)

            self.driver.execute_script("arguments[0].scrollIntoView(true);", email_input)
            print("✅ Adresse e-mail remplie")

            drop_label = self.wait.until(
                EC.element_to_be_clickable(
                    (By.CSS_SELECTOR, "label[for='file-input'] span.c-spl-dropzone-label-browse"))
            )
            self.driver.execute_script("arguments[0].click();", drop_label)
            print("🖱️ Clic sur le label 'Choisissez un fichier' effectué")

            file_input = self.wait.until(
                EC.presence_of_element_located((By.ID, "file-input"))
            )
            file_input.send_keys(CV_PATH)
            print(f"📎 Fichier PDF envoyé : {CV_PATH}")

            submit_button = self.wait.until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, "button.c-spl-button--primary"))
            )
            self.driver.execute_script("arguments[0].click();", submit_button)
            print("✅ Clic sur le bouton de soumission effectué")

            print("🎉 Candidature Sopra Steria terminée")
            return True
        except TimeoutException:
            print("❌ Échec du processus Airbus")
            return False

    def navigate_to_job(self):
        print("🔵 Chargement de l'offre LinkedIn...")
        try:
            self.driver.get(LINKEDIN_JOB_URL)
            self.wait.until(
                EC.presence_of_element_located((By.CSS_SELECTOR, ".jobs-apply-button")))
            return True
        except TimeoutException:
            print("❌ Impossible de charger l'offre")
            return False