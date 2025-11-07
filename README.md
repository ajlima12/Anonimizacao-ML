# 🧠 Projeto de Anonimização de Dados com Machine Learning

Este repositório apresenta um exemplo prático em **Python** de como aplicar **métodos estatísticos e machine learning** para **anonimizar dados pessoais** e **gerar novos registros sintéticos** mantendo características estatísticas próximas dos dados originais.

---

## 🚀 Objetivos do Projeto

1. **Anonimizar dados pessoais**: substituir informações identificáveis (como nome e conta bancária) por dados fictícios realistas.
2. **Proteger a privacidade**: aplicar métodos estatísticos (como média ponderada) para suavizar valores e reduzir riscos de reidentificação.
3. **Gerar registros sintéticos**: aumentar o número de registros de forma artificial com base em modelos estatísticos (Gaussian Mixture Model), mantendo a coerência dos dados.
4. **Exportar resultados**: salvar um novo arquivo CSV anonimizado e expandido, útil para testes, treinamentos de IA ou análises sem expor dados reais.

---

## 🧩 Estrutura do Repositório

```
├── anonymize.py          # Script principal para anonimização e geração de dados sintéticos
├── example_data.csv      # Exemplo de dados de entrada
├── requirements.txt      # Dependências necessárias
├── .gitignore            # Arquivos e pastas ignorados pelo Git
├── LICENSE               # Licença MIT (opcional)
└── README.md             # Este arquivo
```

---

## ⚙️ Tecnologias e Bibliotecas Utilizadas

* **Python 3.9+**
* **pandas** – Manipulação de dados
* **numpy** – Cálculos numéricos e estatísticos
* **faker** – Geração de dados falsos realistas (nomes, cidades, etc.)
* **scikit-learn** – Machine Learning (Gaussian Mixture Model)

Instalação das dependências:

```bash
pip install -r requirements.txt
```

---

## 📄 Exemplo de Dados de Entrada (`example_data.csv`)

| name        | age | income | gender | city           |
| ----------- | --- | ------ | ------ | -------------- |
| João Silva  | 34  | 4500   | M      | São Paulo      |
| Maria Lima  | 27  | 5200   | F      | Rio de Janeiro |
| Pedro Alves | 41  | 6100   | M      | Curitiba       |

---

## 🔧 Funcionamento do Script (`anonymize.py`)

O script realiza quatro etapas principais:

1. **Leitura dos dados originais**: carrega o CSV informado.
2. **Anonimização**:

   * Substitui nomes reais por falsos utilizando `Faker`.
   * Aplica **média ponderada** nas colunas numéricas para suavizar variações e reduzir rastreabilidade.
3. **Geração de dados sintéticos**:

   * Treina um **Gaussian Mixture Model (GMM)** sobre as colunas numéricas.
   * Gera novos registros com distribuição estatística semelhante.
   * Colunas categóricas são replicadas com base na frequência dos valores originais.
4. **Exportação**:

   * Gera dois arquivos CSV:

     * `anonymized.csv` → dados originais anonimizados
     * `synthetic_data.csv` → dados sintéticos gerados artificialmente

---

## ▶️ Como Executar o Projeto

1. Clone o repositório:

```bash
git clone https://github.com/SEU_USUARIO/Anonimizacao-ML.git
cd Anonimizacao-ML
```

2. Crie o ambiente virtual e instale as dependências:

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate     # Windows
pip install -r requirements.txt
```

3. Execute o script:

```bash
python anonymize.py --input example_data.csv --output anonymized.csv --augment 300 --alpha 0.6
```

### Parâmetros disponíveis

| Parâmetro   | Descrição                                  | Padrão             |
| ----------- | ------------------------------------------ | ------------------ |
| `--input`   | Caminho do arquivo CSV original            | `example_data.csv` |
| `--output`  | Nome do arquivo CSV de saída               | `anonymized.csv`   |
| `--augment` | Quantidade de registros sintéticos a gerar | `0`                |
| `--alpha`   | Peso da média ponderada (0 a 1)            | `0.5`              |

Exemplo:

```bash
python anonymize.py --input clientes.csv --output clientes_anon.csv --augment 500 --alpha 0.7
```

---

## 🧮 Explicação da Média Ponderada

A média ponderada é usada para suavizar valores e dificultar a rastreabilidade individual. A fórmula aplicada é:

[ x_{novo} = \alpha \times x_{original} + (1 - \alpha) \times \bar{x} ]

Onde:

* `α` (alpha) → peso de importância do valor original (entre 0 e 1)
* `x̄` → média da coluna

Quanto menor o `α`, mais os dados são suavizados (maior anonimização, menor precisão).

---

## 🧠 Machine Learning: Gaussian Mixture Model (GMM)

O modelo **GMM** é usado para aprender a distribuição estatística dos dados numéricos originais e gerar amostras sintéticas com as mesmas propriedades, preservando correlações entre variáveis.

```python
from sklearn.mixture import GaussianMixture

model = GaussianMixture(n_components=3, random_state=42)
model.fit(df_numeric)
synthetic_samples = model.sample(n_samples=500)
```

---

## 🧾 Licença

Este projeto está licenciado sob a **MIT License** – veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## 🧱 Commits e Tags Sugeridas

```bash
git add .
git commit -m "feat: adiciona pipeline de anonimização e geração sintética (GMM)"
git branch -M main
git remote add origin https://github.com/SEU_USUARIO/Anonimizacao-ML.git
git push -u origin main

# Criar tag de versão
git tag -a v1.0.0 -m "Versão inicial: anonimização e geração de dados sintéticos"
git push origin v1.0.0
```

---

## 📈 Possíveis Melhorias Futuras

* Implementar métricas de **privacidade diferencial (Differential Privacy)**.
* Adicionar **CTGAN / SDV** para geração sintética mais precisa.
* Criar **interface web (Streamlit)** para upload e visualização de dados anonimizados.
* Desenvolver **testes unitários** automáticos para validação de consistência dos dados.

---

## 👩‍💻 Autor

Desenvolvido por **Ana Julia Lima de Oliveira** ✨
📍 São Paulo - Brasil
📚 Projeto demonstrativo de aprendizado em **Machine Learning e Anonimização de Dados**.
