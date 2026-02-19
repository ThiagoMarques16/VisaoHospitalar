# 🏥 Hospital Data Analytics – ETL com Python + Power BI

Projeto de tratamento e análise de dados hospitalares utilizando **Python (Pandas)** para ETL e **Power BI** para visualização e construção de indicadores estratégicos.
<img width="821" height="478" alt="image" src="https://github.com/user-attachments/assets/15fcb466-81b5-4380-ad5f-4b74ccac563d" />


---

## 📌 Objetivo

Demonstrar habilidades em:

- Limpeza e transformação de dados (ETL)
- Tratamento de valores nulos
- Padronização de informações
- Correção de inconsistências
- Engenharia de atributos
- Criação de indicadores (KPIs)
- Construção de Dashboard analítico

---

## 📂 Estrutura do Projeto
📦 hospital-data-analytics
┣ 📂 .venv
┣ 📂 data
┃ ┣ pacientes_hospitalar.csv
┃ ┗ pacientes_hospitalar_tratado.csv
┣ 📂 powerBI
┃ ┗ dashboard_hospitalar.pbix
┣ 📂 python
┃ ┗ etl_pacientes.py
┣ requirements.txt
┗ README.md

---

## 📊 Dataset

Dataset obtido em:

https://www.kaggle.com/datasets/nudratabbas/hospital-records-for-data-cleaning-medium

O dataset contém informações como:

- Idade
- Gênero
- Diagnóstico
- Data de admissão
- Data de alta
- Tempo de permanência

---

## ⚙️ Processo de ETL (Python)

Arquivo: `python/etl_pacientes.py`

### 🔹 1. Tratamento de Tipos de Dados

- Conversão de idade para tipo numérico
- Conversão de datas para datetime
- Tratamento de erros com `errors='coerce'`

### 🔹 2. Padronização de Gênero

- Substituição de valores nulos por **"Não Informado"**
- Tradução:
  - Male → Homem
  - Female → Mulher
- Padronização de "Other" e "Unknown"

### 🔹 3. Padronização de Diagnósticos

- Remoção de espaços
- Conversão para maiúsculas
- Tradução para português
- Substituição de nulos por "Não Informado"

### 🔹 4. Correção de Datas

Se a data de alta for menor que a data de admissão:

- Inversão automática das datas  
- Criação da flag `Flag_DataError`

### 🔹 5. Engenharia de Atributos

Criação da coluna:
- Criação de flags de qualidade:
- Flag_DataError → Datas invertidas
- Flag_AgeMissing → Idade ausente
- Flag_DiadnosisMissing → Diagnóstico não informado

```python
LengthOfStay = (DischargeDate - AdmissionDate).dt.days
```
## ▶️  Como Executar o Projeto
### 1️⃣  Clonar o repositório
```bash
git clone https://github.com/ThiagoMarques16/VisaoHospitalar
cd AnaliseDePaciente
```
### 2️⃣ Criar o ambiente virtual
```bash
python -m venv venv
```
### 3️⃣ Ativar o ambiente
Windows:
```
venv\Scripts\activate
```
Mac/Linux:
```
source venv/bin/activate
```
### 4️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```
### 5️⃣ Executar o script
```bash
python python/etl_pacientes.py
```

## 📈 Dashboard Power BI

O dashboard contém:

### 🔹 KPIs Principais

- **Total de Pacientes**
- **Tempo Médio de Internação**
- **Idade Média**
- **Total de Diagnósticos**

### 🔹 Indicadores de Qualidade de Dados

- **% Diagnósticos não informados**
- **% Idades com erro**
- **% Datas com erro**

### 🔹 Análises Visuais

- **Tempo médio de permanência por diagnóstico**
- **Contagem por gênero**
- **Pacientes por mês**
- **Top 10 diagnósticos**

---

## 🎯 Competências Demonstradas

- Python para Data Analytics
- Manipulação de dados com Pandas
- Tratamento de dados inconsistentes
- Criação de métricas hospitalares
- Modelagem para Power BI
- Construção de dashboard executivo

---

## 👨🏻‍💻 Autor

**Thiago Marques**  
Engenharia de Software – Data Analytics | Python | Power BI  

🔗 Portfólio: [https://thiagomarques.netlify.app/](https://thiagomarques.netlify.app/)
