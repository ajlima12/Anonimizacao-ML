# 🧠 Projeto de Anonimização e Geração de Dados com Machine Learning

Este projeto tem como objetivo demonstrar técnicas de **anonimização de dados** e **geração de novos registros artificiais** utilizando métodos estatísticos e de aprendizado de máquina.  
Ele simula um cenário de banco de dados bancário contendo informações sensíveis como **nome**, **agência**, **conta corrente**, **telefone** e **endereço**.  

A aplicação permite:
- 🔍 Buscar uma pessoa específica no dataset original;  
- 🔒 Aplicar anonimização, embaralhando os dados e protegendo a identidade;  
- 🧬 Gerar novos registros artificiais (data augmentation), mantendo a coerência estatística.  

Dessa forma, é possível trabalhar com dados sensíveis de forma **segura e ética**, garantindo privacidade sem perder a utilidade analítica do conjunto.

---

## 🚀 Como Executar

Após instalar o **Python 3.10+** e configurar o ambiente virtual com as dependências do arquivo `requirements.txt`, execute os comandos abaixo **dentro da pasta principal do projeto**:

---

### 🔍 Buscar uma pessoa específica

```bash
python project/main.py --data data/dataset_original.xlsx --action search --name "Ana Júlia Rocha"
```

---

### 🔒 Anonimizar (embaralhar) os dados

```bash
python project/main.py --data data/dataset_original.xlsx --action anonymize --method swap --out data/dataset_anonimizado.xlsx
```

---

### 🧬 Gerar novos registros artificiais

```bash
python project/main.py --data data/dataset_original.xlsx --action augment --out data/dataset_aumentado.xlsx
```

---

👩‍💻 **Desenvolvido por:** Ana Júlia e Giovanna  
📍 Projeto demonstrativo de anonimização e geração de dados com Python e técnicas estatísticas.
