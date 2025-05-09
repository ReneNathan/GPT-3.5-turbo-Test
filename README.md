# 🐾 GPT-3.5 Turbo - Geração de Textos para Adoção de Animais

Este projeto demonstra como gerar textos dinâmicos e descritivos para adoção de animais em tempo real, utilizando a API do **GPT-3.5-turbo** da OpenAI. A ideia é automatizar a criação de descrições carinhosas e envolventes a partir de informações básicas fornecidas pelo usuário.

---

## 🚀 Requisitos

1. Acesso à internet  
2. Conta ativa na [OpenAI](https://platform.openai.com/)  
3. Saldo disponível na conta OpenAI

---

## ⚙️ Instruções de Uso

1. Clone este repositório:
   ```bash
   git clone https://github.com/seu-usuario/GPT-3.5-turbo-Test.git
   ```
2. Crie um ambiente virtual:
   ```bash
   python -m venv env
   ```
3. Ative o ambiente virtual:  
   - Windows: `env\Scripts\activate`  
   - macOS/Linux: `source env/bin/activate`
4. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
5. Gere sua **API Key** em:  
   [https://platform.openai.com/settings/organization/api-keys](https://platform.openai.com/settings/organization/api-keys)

6. Crie um arquivo `.env` na raiz do projeto com o conteúdo:
   ```
   OPENAI_API_KEY=SUA_CHAVE_AQUI
   ```

7. Inicie a aplicação:
   ```bash
   python app.py
   ```

8. Acesse no navegador:  
   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 📄 Descrição do Projeto

Este projeto gera automaticamente descrições de animais para adoção com base em inputs fornecidos pelo usuário, como nome, idade, porte e comportamento. A IA transforma esses dados em um texto afetuoso e atrativo, ideal para divulgação em sites ou redes sociais de ONGs e protetores independentes.

---

## 🖼 Exemplos de Geração

### Exemplo 1
![Exemplo_1](https://github.com/user-attachments/assets/00707e54-ed79-48b6-82f8-ff906d2cfc58)

### Exemplo 2
![Exemplo_2](https://github.com/user-attachments/assets/94fabe99-8d02-42cf-ae4e-8fd66b576177)

---

## 💵 Importante: Custos

> Este serviço **não é gratuito**. O uso da API da OpenAI gera custos conforme a quantidade de tokens processados.

Em 09/05/2025, o custo era aproximadamente o seguinte:

![Tabela de preços](https://github.com/user-attachments/assets/d28e0063-e402-48b7-9db3-c2c7f59144f0)

Nos exemplos acima, o total de tokens utilizados foi **288**, o que representa um consumo inferior a **$0,01**.

![Relatório de uso](https://github.com/user-attachments/assets/c6ccd710-8c19-4851-a81d-d81517a332d1)
