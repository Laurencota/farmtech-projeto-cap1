# FarmTech Solutions

## Descrição do Projeto

FarmTech Solutions é um projeto acadêmico que simula uma aplicação da startup de **Agricultura Digital**. O objetivo é criar uma solução para gerenciamento de dados de lavouras, com suporte a diferentes culturas (café e milho) e metodologias de plantio.

### Funcionalidades

- **Menu interativo** no terminal para navegação pelas opções do sistema
- **Cadastro de dados** de culturas (café e milho), com campos específicos para cada tipo:
  - **Café**: comprimento, largura, número de ruas e comprimento médio das ruas
  - **Milho**: raio do pivô (plantio via Pivô Central)
- **Armazenamento em listas** para manipulação dos dados cadastrados
- **Atualização e remoção** de registros no vetor
- **Estrutura modular** com separação de responsabilidades em `main.py`, `menu.py` e `dados.py`
- **Scripts em R** para análise estatística (média e desvio padrão)

---

## Estrutura de Pastas

```
farmtech-projeto-cap1/
├── README.md
├── src/
│   ├── python/
│   │   ├── main.py          # Ponto de entrada da aplicação
│   │   ├── menu.py          # Menu interativo e operações
│   │   ├── dados.py         # Armazenamento em listas
│   │   ├── calculos_area.py # Cálculos de área (futuro)
│   │   └── manejo_insumos.py # Manejo de insumos (futuro)
│   └── r/
│       ├── analise_estatistica.R  # Análise estatística (média, desvio padrão)
│       └── api_clima.R           # API de clima (futuro)
```

---

## Como Executar o Projeto

### Aplicação Python

1. Certifique-se de ter o Python instalado (versão 3.x).
2. Acesse a pasta do projeto e execute:

```bash
cd src/python
python main.py
```

3. Utilize o menu para:
   - Inserir dados da lavoura
   - Mostrar dados cadastrados
   - Atualizar dados em uma posição
   - Deletar dados
   - Sair do programa

### Scripts R

Para executar a análise estatística em R:

```bash
cd src/r
Rscript analise_estatistica.R
```

---

## Tecnologias Utilizadas

| Tecnologia | Uso |
|------------|-----|
| **Python 3** | Aplicação principal, lógica de negócio e menu |
| **R** | Análise estatística (média e desvio padrão) |

---

## Integrantes do Grupo

<!-- Preencha com os nomes dos integrantes do grupo -->

| Nome | RM | Turma |
|------|-----|-------|
| | | |
