from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

servico = Service(ChromeDriverManager().install())

navegador = webdriver.Chrome(service=servico)

navegador.get("https://www.vivoplanocorporativo.com.br/")

navegador.find_element('xpath', '//*[@id="tipo"]').click()
navegador.find_element('xpath','//*[@id="empresa"]').send_keys("teste automacao 1")
navegador.find_element('xpath', '//*[@id="contato"]').send_keys("teste automacao 1")
navegador.find_element('xpath', '//*[@id="email"]').send_keys("automacao@automacao.com.br")
navegador.find_element('xpath', '//*[@id="telefone"]').send_keys("11999914187")
navegador.find_element('xpath', '//*[@id="mensagem"]').send_keys("teste automacao texto")
navegador.find_element('xpath', '//*[@id="formulario_contato"]/div[9]/input').click()


