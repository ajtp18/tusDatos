from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException

from database.base import SessionLocal
from app.models.defendant import Defendant

import time

class DefendantProvider:
    def __init__(self, driver):
        self.driver = driver

    def extract_actor_process(self, cc_actor):
        self.driver.implicitly_wait(1)

        cc_defendant_input = self.driver.find_element(
            By.CSS_SELECTOR, 'input[formcontrolname="cedulaDemandado"]')
        cc_defendant_input.clear()
        cc_defendant_input.send_keys(cc_actor)

        button_search = self.driver.find_element(
            By.XPATH, '//button[contains(.,"BUSCAR")]')
        button_search.click()

        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '.causa-individual')))
        list_of_process = []

        while True:
            rows = self.driver.find_elements(
                By.CSS_SELECTOR, '.causa-individual')

            for row in rows:
                process = {}
                process['numero'] = row.find_element(
                    By.CLASS_NAME, 'id').text.strip()
                process['fecha'] = row.find_element(
                    By.CLASS_NAME, 'fecha').text.strip()
                process['numero_proceso'] = row.find_element(
                    By.CLASS_NAME, 'numero-proceso').text.strip()
                process['accion_infraccion'] = row.find_element(
                    By.CLASS_NAME, 'accion-infraccion').text.strip()
                process['detalle'] = row.find_element(
                    By.CLASS_NAME, 'detalle').text.strip()

                list_of_process.append(process)

            try:
                button_next = self.driver.find_element(
                    By.XPATH, '//button[contains(@aria-label, "Página siguiente")]')

                if 'mat-paginator-disabled' in button_next.get_attribute('class'):
                    break

                button_next.click()

                time.sleep(0.5)

            except ElementClickInterceptedException:
                break

        db = SessionLocal()
        for process in list_of_process:
            db_process = Defendant(number=process['numero'], date=process['fecha'], process_number=process['numero_proceso'],
                               action_infraction=process['accion_infraccion'], detail=process['detalle'])
            db.add(db_process)
        db.commit()
        db.close()

        return list_of_process