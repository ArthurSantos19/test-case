## Pré-requisitos

Antes de começar, certifique-se de ter instalado os seguintes requisitos:
- [Python 3.11](https://www.python.org/downloads/)
- [Visual Studio Code (VSCode)](https://code.visualstudio.com/download/)


## Instalação

1. Clone o repositório:
    ```bash
    git clone https://github.com/ArthurSantos19/test-case.git
    ```

2. Navegue até o diretório do projeto:
    ```bash
    cd seu-projeto
    ```

3. Crie um ambiente virtual:
    ```bash
    python -m venv venv
    ```

4. Ative o ambiente virtual (Windows):
    ```bash
    .\venv\Scripts\Activate.ps1
    ```

    Ative o ambiente virtual (Linux/Mac):
    ```bash
    source venv/bin/activate
    ```

5. Instale as dependências:
    ```bash
    pip install selenium
    ```


## Executando Testes

### Executar Teste Específico

1. **Selecione o arquivo de teste desejado**
2. **Clique em Run no Vscode**
3. **Selecionae Python file**

---
---


# Teste Automatizado Adição de Produto ao Carrinho - Loja Intelbras

## Objetivo do Teste
Validar a funcionalidade de adicionar a Fechadura Intelbras FR 210 ao carrinho na Loja Intelbras (loja.intelbras.com.br) utilizando uma ferramenta de teste automatizado de ponta a ponta (E2E), preferencialmente executando no navegador Chrome.

## Cenário Testado
1. **Acessar a loja Intelbras:** Navegar até [loja.intelbras.com.br](https://loja.intelbras.com.br).
2. **Localizar a Fechadura Intelbras FR 210:** Procurar e selecionar o produto desejado.
3. **Adicionar ao carrinho:** Simular a adição da Fechadura Intelbras FR 210 ao carrinho.
4. **Validar a adição ao carrinho:** Confirmar se a Fechadura Intelbras FR 210 está corretamente no carrinho.

## Resultado do Teste
- **<span style="color: green;">✅ Sucesso:</span>** O teste foi executado com êxito, cumprindo o objetivo de adicionar a Fechadura Intelbras FR 210 ao carrinho.

## Observações
- A funcionalidade de adição ao carrinho foi verificada e está operando conforme esperado.
- **<span style="color: orange;">⚠️ Melhoria identificada:</span>** Notou-se um pequeno atraso na renderização do botão "Adicionar ao Carrinho", gerando momentaneamente a exibição como "Comprar" nos primeiros segundos após a seleção do produto.

## Ponto de Melhoria
- **🔧 Sugestão:** Avaliar a otimização da renderização do botão "Adicionar ao Carrinho" para uma transição mais rápida e consistente. Visando aprimorar a experiência do usuário, evitando confusões durante a interação.

## Conclusão
O teste automatizado foi concluído com sucesso, garantindo a adição da Fechadura Intelbras FR 210 ao carrinho. Recomenda-se a análise da sugestão de melhoria para otimizar a renderização do botão, visando uma experiência de compra mais fluida e intuitiva para o usuário. 🚀✨
