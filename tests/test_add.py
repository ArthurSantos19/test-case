import time
from selenium.common.exceptions import StaleElementReferenceException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Inicializando o WebDriver do Chrome
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://loja.intelbras.com.br/")

# Clicar no botão
driver.find_element(By.ID, 'dm876A').click()

# Preencher CEP
# campo_cep = driver.find_element(By.ID, 'zipcode')
campo_cep = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'zipcode'))
)
campo_cep.send_keys("88090080")

# Clicar no botão Verificar CEP
botao_submit_cep = driver.find_element(By.XPATH, '//button[@type="submit" and .//img[@src="/arquivos/icon-right-arrow2.svg"]]')
botao_submit_cep.click()

time.sleep(1)

# Aguardar até que o campo de pesquisa esteja presente
campo_input = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//input[@type="search" and @class="search__input"]'))
)

# Preencher pesquisa
campo_input.send_keys("FR 210")

botao_submit = driver.find_element(By.XPATH, '//button[@type="submit" and @class="search__submit"]')
botao_submit.click()


# Aguardar até que o produto esteja presente
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//a[@title="Fechadura Digital de Sobrepor Intelbras FR 210" and @href="https://loja.intelbras.com.br/fechadura-digital-fr210/p" and @class="shelf-item__title-link"]'))
)

# Adicionar o produto ao carrinho
selecionar_elemento = driver.find_element(By.XPATH, '//a[@title="Fechadura Digital de Sobrepor Intelbras FR 210" and @href="https://loja.intelbras.com.br/fechadura-digital-fr210/p" and @class="shelf-item__title-link"]')
selecionar_elemento.click()

# Aguardar até que o botão de adicionar ao carrinho esteja presente
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//button[@class="itb-custom-buy-btn" and @data-installation-type="without service"]'))
)

# Adicionar o produto ao carrinho
botao_add_carrinho = driver.find_element(By.XPATH, '//button[@class="itb-custom-buy-btn" and @data-installation-type="without service"]')
botao_add_carrinho.click()

# Aguardar até que o botão de ver carrinho esteja presente
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//a[@href="/checkout" and contains(@class, "minicart-checkout") and contains(@class, "button--medium") and contains(@class, "button--black")]'))
)

# Ver carrinho
ver_carrinho = driver.find_element(By.XPATH, '//a[@href="/checkout" and contains(@class, "minicart-checkout") and contains(@class, "button--medium") and contains(@class, "button--black")]')
ver_carrinho.click()

# Validar se a fechadura foi adicionada ao carrinho
titulo_produto_carrinho = driver.find_element(By.XPATH, '//td[@class="product-name" and contains(@data-bind, "window.cart.loadingItem()")]//a[starts-with(@href, "//loja.intelbras.com.br/fechadura-digital-fr210/p")]')

# Verificar se o título do produto na página do carrinho corresponde ao esperado
assert "Fechadura Digital de Sobrepor Intelbras FR 210" in titulo_produto_carrinho.text, "Produto não encontrado no carrinho"
print("Produto encontrado no carrinho!")

# Fechar o navegador
driver.quit()
