from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

# Acessando Loja Intelbras
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://loja.intelbras.com.br/")

time.sleep(3)
driver.find_element(By.ID, 'dm876A').click()

# Preencher CEP
campo_cep = driver.find_element(By.ID, 'zipcode')
campo_cep.send_keys("88090080")

# Clicar no botão Verificar CEP
botao_submit_cep = driver.find_element(By.XPATH, '//button[@type="submit" and .//img[@src="/arquivos/icon-right-arrow2.svg"]]')
botao_submit_cep.click()

# Adicione um tempo de espera para garantir que a página seja totalmente carregada
time.sleep(5)
campo_input = driver.find_element(By.XPATH, '//input[@type="search" and @class="search__input"]')
campo_input.send_keys("FR 210")


# Clicar no botão de pesquisa
botao_submit = driver.find_element(By.XPATH, '//button[@type="submit" and @class="search__submit"]')
botao_submit.click()
time.sleep(5)


# Adicionar o produto ao carrinho
selecionar_elemento = driver.find_element(By.XPATH, '//a[@title="Fechadura Digital de Sobrepor Intelbras FR 210" and @href="https://loja.intelbras.com.br/fechadura-digital-fr210/p" and @class="shelf-item__title-link"]')
selecionar_elemento.click()
time.sleep(4)
botao_add_carrinho = driver.find_element(By.XPATH, '//button[@class="itb-custom-buy-btn" and @data-installation-type="without service"]')
botao_add_carrinho.click()
time.sleep(3)
ver_carrinho = driver.find_element(By.XPATH, '//a[@href="/checkout" and contains(@class, "minicart-checkout") and contains(@class, "button--medium") and contains(@class, "button--black")]')
ver_carrinho.click()

# Validar se a fechadura foi adicionada ao carrinho
titulo_produto_carrinho = driver.find_element(By.XPATH, '//td[@class="product-name" and contains(@data-bind, "window.cart.loadingItem()")]//a[starts-with(@href, "//loja.intelbras.com.br/fechadura-digital-fr210/p")]')

# Verificar se o título do produto na página do carrinho corresponde ao esperado
assert "Fechadura Digital de Sobrepor Intelbras FR 210" in titulo_produto_carrinho.text, "Produto não encontrado no carrinho"
print("Produto encontrado no carrinho!")

time.sleep(10)