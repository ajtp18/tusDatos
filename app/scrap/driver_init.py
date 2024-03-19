from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver

def init_chrome(url):
    ruta = ChromeDriverManager().install()
    options = Options()
    user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    options.add_argument(f'user-agent={user_agent}')
    options.add_argument("--disable-web-security")
    options.add_argument("--disable-extension")
    options.add_argument("--disable-notifications")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--no-sandbox")
    options.add_argument("--log-level=3")
    options.add_argument("--allow-running-insecure-content")
    options.add_argument("--no-default-browser-check")
    options.add_argument("--no-first-run")
    options.add_argument("--no-proxy-server")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--headless")

    exp_opt = [
        'enable-automation',
        'ignore-certificate-errors',
        'enable-logging',
    ]

    options.add_experimental_option("excludeSwitches", exp_opt)
    preference = {
        'profile.default_content_setting_values.notifications': 2,
        'intl.accept_languages': ['es-ES', 'es'],
        'credentials_enable_service': False,
    }
    options.add_experimental_option("prefs", preference)

    s = Service(ruta)

    driver = webdriver.Chrome(service=s, options=options)
    driver.get(url)

    return driver