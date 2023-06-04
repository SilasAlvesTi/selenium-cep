from selenium import webdriver
from selenium.webdriver.common.by import By

def inicia_driver():
    profile_path = '/home/silas/snap/firefox/common/.mozilla/firefox/1k23b9rh.Selenium'  
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('-profile')
    firefox_options.add_argument(profile_path)
    return webdriver.Firefox(options=firefox_options)

def busca_por_cep():

    driver = inicia_driver()

    driver.get("https://buscacepinter.correios.com.br/app/endereco/index.php")

    driver.implicitly_wait(0.5)

    text_box = driver.find_element(by=By.NAME, value="endereco")
    submit_button = driver.find_element(by=By.NAME, value="btn_pesquisar")

    text_box.send_keys("62360000")
    submit_button.click()

    localidade = driver.find_element(by=By.XPATH, value="/html/body/main/form/div[1]/div[2]/div/div[4]/table/tbody/tr/td[3]")
    print(localidade.text)
    
    driver.quit()


if __name__ == '__main__':
    busca_por_cep()