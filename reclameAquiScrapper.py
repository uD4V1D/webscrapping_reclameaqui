import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class ReclameAqui:
    
    def __init__(self):
        self.url = 'https://www.reclameaqui.com.br'
        self.navegador = webdriver.Firefox()
        self.agent = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/118.0"}
        self.df = pd.DataFrame({
            'Empresa':[],
            'Reclamações Respondidas': [],
            'Voltaria a Fazer Negocio': [],
            'Indice de Solucao': [],
            'Nota do Consumidor': []
        })


    def ScrapperMelhoresEmpresas(self):
        df = self.df.copy()

        for i in range(1,4):
            
            WebDriverWait(self.navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '/html/body/section[2]/div/astro-island/div/div[3]/div/div[1]/a[1]')))
            empresa = self.navegador.find_element(By.XPATH, f'//*[@id="homeRankings"]/div/astro-island/div/div[3]/div/div[1]/a[{i}]')
            empresa.click()
            nomeEmp = self.navegador.find_element(By.XPATH,'//*[@id="hero"]/div[2]/div/div[2]/div[1]/h1')
            respondidas = self.navegador.find_element(By.XPATH,'//*[@id="newPerformanceCard"]/div[2]/div[2]/span/strong')
            negocioNovamente = self.navegador.find_element(By.XPATH, '//*[@id="newPerformanceCard"]/div[2]/div[5]/span/strong')
            indiceSolucao = self.navegador.find_element(By.XPATH,'//*[@id="newPerformanceCard"]/div[2]/div[6]/span/strong')
            notaConsumidor = self.navegador.find_element(By.XPATH, '//*[@id="ra-new-reputation"]/span/b')
            nova_linha = {
                'Empresa': nomeEmp.text,
                'Reclamações Respondidas': respondidas.text,
                'Voltaria a Fazer Negocio': negocioNovamente.text,
                'Indice de Solucao': indiceSolucao.text,
                'Nota do Consumidor': notaConsumidor.text
            }

            melhoresEmpresas = df.loc[len(df)] = nova_linha
            self.navegador.back()
            varejo = self.navegador.find_element(
                    By.XPATH, "//button[@class='inline text-[#4b5963] font-semibold whitespace-nowrap border-2 p-2 rounded-md border-gray-400 hover:border-green-800 hover:text-green-800 first:ml-2 last:mr-2 svelte-lxks97' and text()='Varejo']"
                )
            varejo.click()
            i+=1
        melhoresEmpresas = df.to_excel('melhoresEmpresas.xlsx', index=False)
        return melhoresEmpresas

    def ScrapperPioresEmpresas(self):
        df = self.df.copy()
        for i in range(1,4):
            
            WebDriverWait(self.navegador, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="homeRankings"]/div/astro-island/div/div[3]/div/div[2]/a[1]')))
            empresa = self.navegador.find_element(By.XPATH, f'//*[@id="homeRankings"]/div/astro-island/div/div[3]/div/div[2]/a[{i}]')
            empresa.click()
            nomeEmp = self.navegador.find_element(By.XPATH,'//*[@id="hero"]/div[2]/div/div[2]/div[1]/h1')
            respondidas = self.navegador.find_element(By.XPATH,'//*[@id="newPerformanceCard"]/div[2]/div[2]/span/strong')
            negocioNovamente = self.navegador.find_element(By.XPATH, '//*[@id="newPerformanceCard"]/div[2]/div[5]/span/strong')
            indiceSolucao = self.navegador.find_element(By.XPATH,'//*[@id="newPerformanceCard"]/div[2]/div[6]/span/strong')
            notaConsumidor = self.navegador.find_element(By.XPATH, '//*[@id="ra-new-reputation"]/span/b')
            nova_linha = {
                'Empresa': nomeEmp.text,
                'Reclamações Respondidas': respondidas.text,
                'Voltaria a Fazer Negocio': negocioNovamente.text,
                'Indice de Solucao': indiceSolucao.text,
                'Nota do Consumidor': notaConsumidor.text
            }

            df.loc[len(df)] = nova_linha
            self.navegador.back()
            varejo = self.navegador.find_element(
                    By.XPATH, "//button[@class='inline text-[#4b5963] font-semibold whitespace-nowrap border-2 p-2 rounded-md border-gray-400 hover:border-green-800 hover:text-green-800 first:ml-2 last:mr-2 svelte-lxks97' and text()='Varejo']"
                )
            varejo.click()
            i+=1
        pioresEmpresas = df.to_excel('pioresEmpresas.xlsx', index=False)
        return pioresEmpresas

    def ScrapperGeral(self):
        self.navegador.get(self.url)
        self.navegador.maximize_window()
        while True:
            try:
                varejo = self.navegador.find_element(
                        By.XPATH, "//button[@class='inline text-[#4b5963] font-semibold whitespace-nowrap border-2 p-2 rounded-md border-gray-400 hover:border-green-800 hover:text-green-800 first:ml-2 last:mr-2 svelte-lxks97' and text()='Varejo']"
                )
                WebDriverWait(self.navegador,10).until(EC.element_to_be_clickable(varejo))
                varejo.click()
                break
            except:
                self.navegador.execute_script('window.scrollBy(0,900)')
            
                WebDriverWait(self.navegador, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@class='inline text-[#4b5963] font-semibold whitespace-nowrap border-2 p-2 rounded-md border-gray-400 hover:border-green-800 hover:text-green-800 first:ml-2 last:mr-2 svelte-lxks97' and text()='Varejo']")))
        
        self.ScrapperMelhoresEmpresas()
        self.ScrapperPioresEmpresas()
        
        self.navegador.close()
        
   

reclame_aqui =  ReclameAqui()
reclame_aqui.ScrapperGeral()


diretorio_projeto = os.getcwd()
os.system(f'explorer {diretorio_projeto}')