# 🛒 Automation Ecommerce E2E — Python + Selenium

Automação E2E de um fluxo realista de e-commerce, construída com foco em qualidade profissional, clareza e entrega de valor.  
Este projeto automatiza a jornada de um usuário real: do login ao checkout final — com código limpo, estrutura escalável e relatórios HTML visuais.

---

## 🎯 Objetivos principais

- ✅ Dominar testes automatizados de ponta a ponta com **Python + Selenium**
- ✅ Aplicar o padrão de arquitetura **Page Object Model (POM)**
- ✅ Criar uma automação realista, similar ao que empresas exigem para vagas de QA/Automação Jr
- ✅ Deixar um projeto de portfólio **funcional, rastreável e com documentação clara**

---

## 🚀 Tecnologias e Ferramentas

- `Python 3.13`
- `Selenium WebDriver`
- `Pytest`
- `Pytest-HTML`
- `Page Object Model (POM)`
- `LambdaTest Playground` como ambiente web de testes

---

## 🧪 Testes incluídos

- Login com sucesso
- Busca por produtos
- Adição ao carrinho
- Checkout completo: preenchimento de billing, aceite dos termos e confirmação do pedido

> O fluxo de checkout lida com DOMs instáveis, elementos dinâmicos e botões quebrando — com técnicas avançadas para garantir estabilidade real.

---

## 📂 Estrutura do projeto
```
.
├── src/
│   └── pages/                # Page Objects (HomePage, ProductPage, etc.)
├── tests/                    # Testes organizados por funcionalidade
├── reports/                 # Relatórios HTML gerados automaticamente
├── run_tests.py             # Runner de testes customizado
├── requirements.txt
└── README.md
```
---

## ▶️ Como rodar

1. Instale os requisitos:
   ```bash
   pip install -r requirements.txt
   ```

2. Execute o runner:
   ```bash
   python run_tests.py
   ```

3. Acesse o relatório:
   Abra o arquivo `.html` mais recente em `/reports/` com o navegador.

---

## ⚠️ Observação sobre o ambiente

Este projeto utiliza o ambiente público da LambdaTest:  
https://ecommerce-playground.lambdatest.io

> Sendo um ambiente compartilhado e não-controlado, instabilidades podem acontecer.  
> O projeto já prevê esses cenários e trata falhas como ausência de métodos de pagamento ou DOM intermitente de forma segura.

---

## 📊 Relatórios gerados

A cada execução, um novo relatório HTML com timestamp é salvo em `/reports/`.  
Ele inclui:

- Nome e status de cada teste
- Logs capturados no terminal
- Rastreamento de exceções e mensagens
- Total de testes, tempo e ambiente

---

## 🛤️ Jornada e aprendizados

Durante o desenvolvimento:

- Enfrentei falhas reais no ambiente (DOM quebrando, métodos ausentes, radio buttons ocultos).
- Adicionei manipulação via JavaScript para aceitar termos mesmo com `z-index` travando o clique.
- Escrevi código resiliente com `try/except`, waits sob medida e fallback para falhas do front-end.

O projeto reflete o dia a dia da automação moderna:  
💬 “Testar é validar o que funciona, mas automatizar é sobreviver ao que quebra.”

---

## 🔭 Como esse projeto pode ser expandido

Esse projeto atinge seus objetivos com clareza — mas ele pode evoluir para gerar ainda mais impacto com pouco esforço. Algumas ideias:

### Funcionalidades extras

- [ ] Adicionar múltiplos produtos no carrinho
- [ ] Verificar subtotal, frete e valor total
- [ ] Aplicar e validar cupons de desconto
- [ ] Verificar produtos esgotados e exibir botão "Indisponível"

### Testes negativos essenciais

- [ ] Login com senha inválida
- [ ] Checkout sem aceitar termos
- [ ] Busca por produto inexistente

### Infraestrutura

- [ ] Centralizar configuração com `conftest.py`
- [ ] Usar `markers` para agrupar testes por tipo
- [ ] Gerar capturas de tela em falhas (`pytest-html`)
- [ ] Rodar em pipeline com GitHub Actions

---

## ✅ Conclusão

Este repositório entrega o que promete:

- Estrutura limpa com Page Object Model
- Testes E2E funcionais e resilientes
- Logs claros e relatórios acessíveis
- Pronto para ser apresentado em qualquer vaga de QA/Automação

---

**Desenvolvido por:** Lucas | [GitHub](https://github.com/lucasprog18)


