# WebScrapping Reclame Aqui

Automação web para extração de dados das piores e melhores empresas cadastradas no site reclame aqui feita com Python 3, utilizando as bibliotecas pandas, selenium e openpyxl.

# Atenção

Se sua máquina não possuir as dependências listadas em requirements.txt, navegue até o diretório do projeto no prompt de comando usando:

**cd 'caminho_do_seu_projeto'**

E logo em seguida utilize o comando:

**pip install -r requirements.txt**

Ademais, verifique se o WebDriver do navegador está no local correto. Neste projeto, foi utilizado o geckoDriver, webdriver do **Firefox**, o mesmo pode ser encontrado em [https://github.com/mozilla/geckodriver/releases](https://github.com/mozilla/geckodriver/releases).


# Instruções de Uso

Utilize o Navegador Firefox e certifique-se que ele esteja atualizado.

Após todas as dependências instaladas e em perfeito funcionamento, basta executar o código constado no arquivo reclameAquiScrapper.py e esperar até que ele finalize e abra o diretório local do projeto e lá você encontrará dois arquivos, melhoresEmpresas.xlsx e pioresEmpresas,xlsx. 
