import time
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_and_click(driver, by, value, timeout=10):
    try:
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((by, value)))
        element.click()
    except TimeoutException:
        print(f"Elemento {value} não encontrado após {timeout} segundos.")

start_time = time.time()

# Inicializando o WebDriver do Chrome
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://loja.intelbras.com.br/")

# Clicar no botão
wait_and_click(driver, By.ID, 'dm876A')

# Preencher CEP
campo_cep = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'zipcode')))
campo_cep.send_keys("88090080")

# Clicar no botão Verificar CEP
wait_and_click(driver, By.XPATH, '//button[@type="submit" and .//img[@src="/arquivos/icon-right-arrow2.svg"]]')

time.sleep(2)

# Aguardar até que o campo de pesquisa esteja presente
campo_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//input[@type="search" and @class="search__input"]')))

# Preencher pesquisa
campo_input.send_keys("FR 210")

# Clicar no botão de pesquisa
wait_and_click(driver, By.XPATH, '//button[@type="submit" and @class="search__submit"]')

# Aguardar até que o produto esteja presente
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//a[@title="Fechadura Digital de Sobrepor Intelbras FR 210" and @href="https://loja.intelbras.com.br/fechadura-digital-fr210/p" and @class="shelf-item__title-link"]'))
)

# Adicionar o produto ao carrinho
wait_and_click(driver, By.XPATH, '//a[@title="Fechadura Digital de Sobrepor Intelbras FR 210" and @href="https://loja.intelbras.com.br/fechadura-digital-fr210/p" and @class="shelf-item__title-link"]')

# Aguardar até que o botão de adicionar ao carrinho esteja presente
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//button[@class="itb-custom-buy-btn" and @data-installation-type="without service"]'))
)

# Adicionar o produto ao carrinho
wait_and_click(driver, By.XPATH, '//button[@class="itb-custom-buy-btn" and @data-installation-type="without service"]')

# Aguardar até que o botão de ver carrinho esteja presente
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//a[@href="/checkout" and contains(@class, "minicart-checkout") and contains(@class, "button--medium") and contains(@class, "button--black")]'))
)

# Ver carrinho
wait_and_click(driver, By.XPATH, '//a[@href="/checkout" and contains(@class, "minicart-checkout") and contains(@class, "button--medium") and contains(@class, "button--black")]')

# Validar se a fechadura foi adicionada ao carrinho
titulo_produto_carrinho = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, '//td[@class="product-name" and contains(@data-bind, "window.cart.loadingItem()")]//a[starts-with(@href, "//loja.intelbras.com.br/fechadura-digital-fr210/p")]'))
)

# Verificar se o título do produto na página do carrinho corresponde ao esperado
assert "Fechadura Digital de Sobrepor Intelbras FR 210" in titulo_produto_carrinho.text, "Produto não encontrado no carrinho"
print("Produto encontrado no carrinho!")

# Aguarda até que o elemento esteja presente antes de obter a quantidade inicial
campo_quantidade = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.XPATH, "//input[@id='item-quantity-4670210']"))
)
quantidade_inicial = int(campo_quantidade.get_attribute('value'))

# Aumentar produto do carrinho
increment_locator = (By.XPATH, "//a[@id='item-quantity-change-increment-4670210']")
increment = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(increment_locator))
increment.click()

# Aguardar até que a quantidade seja atualizada após o incremento
WebDriverWait(driver, 10).until(
    lambda driver: int(driver.find_element(By.XPATH, "//input[@id='item-quantity-4670210']").get_attribute('value')) == quantidade_inicial + 1
)

# Obtém a quantidade após o incremento
quantidade_apos_incremento = int(driver.find_element(By.XPATH, "//input[@id='item-quantity-4670210']").get_attribute('value'))

# Verifica se a quantidade foi incrementada corretamente usando assert
assert quantidade_apos_incremento == quantidade_inicial + 1, "A quantidade não foi incrementada corretamente"
print(f"Quantidade após incremento: {quantidade_apos_incremento}")

# TEMPO
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Tempo de execução: {elapsed_time} segundos")

# Fechar o navegador
driver.quit()
