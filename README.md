# 🚀 Global Solution 2025 - Gestão LTAKN & Chatbot Laren

## 📝 Proposta e Funcionalidades

Este projeto implementa uma solução completa de **monitoramento de bem-estar corporativo**, desenvolvida como parte da Global Solution da FIAP (2025/2). O sistema foi projetado para coletar dados de jornada de trabalho, processar indicadores de risco com **Inteligência Artificial Generativa** e visualizar as informações em um portal administrativo, integrando um Backend Java Spring Boot com um microsserviço Python.

O objetivo principal é demonstrar uma arquitetura moderna de microsserviços aplicada ao tema "O Futuro do Trabalho", onde a IA atua como parceira na prevenção do burnout. A API Java gerencia a operação e o banco de dados, enquanto a API Python (Laren) fornece a inteligência analítica via Google Gemini.

---

## 🔧 Módulos e Funcionalidades

### 🟣 API Java (Spring Boot - Backend)
* Lê e grava os dados diretamente no banco de dados em nuvem.
* Oferece endpoints REST e uma interface web completa via **Thymeleaf**.
* Integra-se com a API Python para solicitar análises de IA em tempo real.
* Utiliza **RabbitMQ** para o processamento assíncrono de relatórios de risco.

### 🟠 API Python (Microsserviço IA - Laren)
* Recebe dados brutos dos funcionários enviados pelo Java.
* Utiliza o modelo **Google Gemini (LLM)** para gerar diagnósticos empáticos e recomendações de saúde mental.
* Retorna respostas em JSON para exibição no portal.

### 🟢 Banco de Dados (Azure SQL)
* Responsável pelo armazenamento relacional robusto na nuvem.
* Armazena os registros de departamentos, funcionários e usuários do sistema.

---

## 🏛️ Arquitetura do Projeto

O sistema segue o modelo de **Microsserviços e MVC**, com integração via REST e persistência em nuvem.

<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/ba502b8d-e908-4ee0-bb2c-195066f2d942" />


**🔄 Fluxo de Dados:**
1.  O Gestor acessa o Portal Java e visualiza a equipe.
2.  Ao solicitar uma análise, o Java envia os dados do funcionário para a API Python.
3.  A IA (Laren) processa o contexto e devolve uma recomendação personalizada.
4.  O resultado é exibido em tempo real via Modal no navegador.
5.  Relatórios pesados são enfileirados no **RabbitMQ** para processamento em segundo plano.

---

## 🧩 Componentes Utilizados

| Componente | Função |
| :--- | :--- |
| **API Java (Spring Boot)** | Núcleo do sistema, regras de negócio e interface Web (Thymeleaf) |
| **API Python (Flask)** | Microsserviço de IA responsável pela inteligência da "Laren" |
| **Google Gemini** | LLM utilizado para análise de sentimentos e geração de texto |
| **Azure SQL Database** | Banco de dados relacional na nuvem (PaaS) |
| **RabbitMQ (CloudAMQP)** | Broker de mensageria para processamento assíncrono |
| **Render & Azure** | Plataformas de Nuvem utilizadas para o deploy das aplicações |

---

## 👩‍💻 Integrantes do Grupo

* **Enzo Prado Soddano** — RM557937
* **Lucas Resende Lima** — RM556564
* **Vinicius Prates Altafini** — RM559183

---

## 🔗 Links do Projeto

* **Link do Vídeo:** [https://youtu.be/g5DaZzdIV5g)
* **Link do Repositório IA:** [https://github.com/vinicius945/GLOBAL_IA_LAREN](https://github.com/vinicius945/GLOBAL_IA_LAREN)
* **Deploy API IA:** [https://api-ia-laren.onrender.com](https://api-ia-laren.onrender.com)

---

## ▶️ Execução do Projeto

1.  Acesse o link do **Portal Java** (Hospedado no Azure).
2.  Faça login com as credenciais de administrador (`admin` / `adminpass`).
3.  Acesse a aba **Funcionários**.
4.  Clique no botão **"🤖 Laren"** para ver a integração com a IA em funcionamento.
