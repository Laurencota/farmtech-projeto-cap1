# Documentação do Código - FarmTech Solutions

Este documento explica o funcionamento do projeto de forma simples e clara. Use-o como guia para entender o código, mesmo se você nunca programou.

---

## Arquivos do Projeto

| Arquivo | O que faz |
|---------|-----------|
| **main.py** | É o ponto de partida. Quando você roda o programa, é ele que inicia e mantém o menu funcionando em loop. |
| **menu.py** | Contém todo o menu interativo e as operações: inserir, mostrar, atualizar e deletar lavouras. |
| **dados.py** | Onde os dados ficam guardados. Define a lista de lavouras e as funções para adicionar, atualizar e remover registros. |
| **calculos_area.py** | Funções prontas para calcular área de plantio (café e milho). Os cálculos ainda serão implementados pelo grupo. |
| **manejo_insumos.py** | Funções prontas para calcular quantidade de insumos. Os cálculos ainda serão implementados pelo grupo. |

---

## Funções

### main.py

#### `main()`
- **Parâmetros:** Nenhum
- **Retorna:** Nada
- **Responsabilidade:** Inicia o programa, exibe a mensagem de boas-vindas e entra em um loop infinito que mostra o menu e processa a opção escolhida. O loop só termina quando o usuário escolhe "Sair" (opção 5).

---

### menu.py

#### `exibir_menu()`
- **Parâmetros:** Nenhum
- **Retorna:** Nada
- **Responsabilidade:** Mostra na tela o menu com as 5 opções do sistema.

#### `ler_numero(mensagem, tipo=float)`
- **Parâmetros:**
  - `mensagem` (str): Texto exibido para o usuário (ex.: "Digite o comprimento: ")
  - `tipo` (opcional): Tipo do número esperado. Pode ser `float` (número com vírgula) ou `int` (número inteiro). O padrão é `float`.
- **Retorna:** O número digitado pelo usuário, já convertido para o tipo correto
- **Responsabilidade:** Pede um número ao usuário e trata erros (ex.: se a pessoa digitar texto em vez de número). Evita que o programa quebre.

**Exemplo:**
```python
valor = ler_numero("Comprimento (metros): ")      # retorna um float, ex: 100.5
quantidade = ler_numero("Nº de ruas: ", int)      # retorna um int, ex: 20
```

#### `inserir_lavoura()`
- **Parâmetros:** Nenhum
- **Retorna:** Nada
- **Responsabilidade:** Pergunta ao usuário todos os dados da lavoura (cultura, nome da fazenda, dimensões) e salva na lista. Se for café, pergunta comprimento, largura, número de ruas e comprimento das ruas. Se for milho, pergunta apenas o raio do pivô.

#### `mostrar_lavouras()`
- **Parâmetros:** Nenhum
- **Retorna:** Nada
- **Responsabilidade:** Exibe na tela todas as lavouras cadastradas, com posição (índice) e todos os dados de cada uma.

#### `atualizar_lavoura_menu()`
- **Parâmetros:** Nenhum
- **Retorna:** Nada
- **Responsabilidade:** Permite alterar os dados de uma lavoura. O usuário informa a posição (índice) e depois pode modificar cada campo. Campos deixados em branco mantêm o valor anterior.

#### `deletar_lavoura()`
- **Parâmetros:** Nenhum
- **Retorna:** Nada
- **Responsabilidade:** Remove uma lavoura da lista. O usuário informa a posição (índice) da lavoura a ser removida.

#### `executar_opcao(opcao)`
- **Parâmetros:**
  - `opcao` (str): A opção digitada pelo usuário ("1", "2", "3", "4" ou "5")
- **Retorna:** `True` para continuar o menu; `False` para sair do programa
- **Responsabilidade:** Interpreta a opção escolhida e chama a função correspondente. Se a opção for 5 (Sair), retorna `False` para encerrar o loop do `main`.

---

### dados.py

#### `obter_lavouras()`
- **Parâmetros:** Nenhum
- **Retorna:** A lista `lavouras` (todas as lavouras cadastradas)
- **Responsabilidade:** Disponibiliza a lista de lavouras para outros arquivos.

#### `adicionar_lavoura(lavoura)`
- **Parâmetros:**
  - `lavoura` (dict): Um dicionário com todos os dados da lavoura (cultura, nome, dimensões etc.)
- **Retorna:** Nada
- **Responsabilidade:** Adiciona a nova lavoura ao final da lista.

#### `atualizar_lavoura(indice, lavoura)`
- **Parâmetros:**
  - `indice` (int): A posição da lavoura na lista (0, 1, 2...)
  - `lavoura` (dict): O dicionário com os dados atualizados
- **Retorna:** `True` se a atualização funcionou; `False` se o índice for inválido
- **Responsabilidade:** Substitui os dados da lavoura na posição indicada.

#### `remover_lavoura(indice)`
- **Parâmetros:**
  - `indice` (int): A posição da lavoura a ser removida
- **Retorna:** `True` se a remoção funcionou; `False` se o índice for inválido
- **Responsabilidade:** Remove a lavoura da lista na posição indicada.

---

### calculos_area.py

#### `calcular_area_retangular(comprimento, largura)`
- **Parâmetros:**
  - `comprimento` (float): Comprimento da área em metros
  - `largura` (float): Largura da área em metros
- **Retorna:** Área em m² (implementação pendente)
- **Responsabilidade:** Calcular a área de lavouras retangulares (usada para café). A fórmula será: `comprimento * largura`.

#### `calcular_area_circular(raio)`
- **Parâmetros:**
  - `raio` (float): Raio do pivô em metros
- **Retorna:** Área em m² (implementação pendente)
- **Responsabilidade:** Calcular a área de lavouras circulares (usada para milho com Pivô Central). A fórmula será: π × raio².

---

### manejo_insumos.py

#### `calcular_insumos_cafe(ml_por_metro, numero_ruas, comprimento_medio_rua)`
- **Parâmetros:**
  - `ml_por_metro` (float): Mililitros de insumo por metro linear
  - `numero_ruas` (int): Quantidade de ruas da lavoura
  - `comprimento_medio_rua` (float): Comprimento médio de cada rua em metros
- **Retorna:** Quantidade total de insumo em ml (implementação pendente)
- **Responsabilidade:** Calcular o total de insumo para lavoura de café. A fórmula será: `ml_por_metro * numero_ruas * comprimento_medio_rua`.

#### `calcular_insumos_milho(ml_por_metro, raio_pivo)`
- **Parâmetros:**
  - `ml_por_metro` (float): Mililitros de insumo por metro
  - `raio_pivo` (float): Raio do pivô em metros
- **Retorna:** Quantidade total de insumo em ml (implementação pendente)
- **Responsabilidade:** Calcular o total de insumo para lavoura de milho (Pivô Central). Uma opção é usar a circunferência (2 × π × raio) como referência de metros lineares.

---

## Variáveis

### Variáveis globais (dados.py)

| Variável | Tipo | Descrição |
|----------|------|-----------|
| `lavouras` | lista | Lista que armazena todas as lavouras cadastradas. Cada elemento é um dicionário. |
| `CULTURAS_SUPORTADAS` | lista | Lista com as culturas permitidas: `["café", "milho"]`. Usada para validar a entrada do usuário. |

### Estrutura de uma lavoura (dicionário)

**Lavoura de café:**
```python
{
    "cultura": "café",
    "nome_fazenda": "Fazenda Santa Maria",
    "comprimento_area": 100.0,      # metros
    "largura_area": 50.0,           # metros
    "numero_ruas": 20,
    "comprimento_medio_rua": 50.0   # metros
}
```

**Lavoura de milho:**
```python
{
    "cultura": "milho",
    "nome_fazenda": "Talhão Norte",
    "raio_pivo": 400.0              # metros
}
```

### Variáveis locais comuns (usadas dentro das funções)

| Variável | Significado |
|----------|-------------|
| `opcao` | Número escolhido pelo usuário no menu (1 a 5) |
| `cultura` | Tipo da cultura: "café" ou "milho" |
| `nome_fazenda` | Nome da fazenda ou talhão |
| `indice` | Posição da lavoura na lista (0 = primeira, 1 = segunda, etc.) |
| `lavoura` / `lav_atual` | Dicionário com os dados de uma lavoura |
| `nova_lavoura` | Dicionário com os dados atualizados ao editar |

---

## Fluxo do Sistema

### 1. Início do programa

```
Usuário executa: python main.py
        ↓
main() é chamada
        ↓
Mensagem de boas-vindas é exibida
        ↓
Entra no loop (while True)
```

### 2. Loop do menu

```
exibir_menu() → Mostra as 5 opções
        ↓
input() → Usuário digita a opção (1, 2, 3, 4 ou 5)
        ↓
executar_opcao(opcao) → Chama a função correspondente
        ↓
   Se opção 1: inserir_lavoura()
   Se opção 2: mostrar_lavouras()
   Se opção 3: atualizar_lavoura_menu()
   Se opção 4: deletar_lavoura()
   Se opção 5: retorna False → loop termina, programa encerra
        ↓
Se não for opção 5: retorna True → menu é exibido novamente
```

### 3. Exemplo: Inserir lavoura

```
inserir_lavoura() é chamada
        ↓
Pergunta: cultura (café ou milho)
        ↓
Pergunta: nome da fazenda
        ↓
Se café: pergunta comprimento, largura, nº ruas, comprimento das ruas
Se milho: pergunta raio do pivô
        ↓
Cria o dicionário com os dados
        ↓
adicionar_lavoura(lavoura) → adiciona na lista
        ↓
Exibe "Lavoura cadastrada com sucesso!"
```

### 4. Exemplo: Mostrar lavouras

```
mostrar_lavouras() é chamada
        ↓
Verifica se a lista está vazia
        ↓
Para cada lavoura na lista:
   - Exibe posição [0], [1], [2]...
   - Exibe os campos (cultura, fazenda, dimensões)
   - Se milho: mostra raio do pivô
   - Se café: mostra comprimento, largura, ruas
```

---

## Dicas para quem está começando

1. **Lista e índices:** A primeira lavoura está na posição 0, a segunda na posição 1, e assim por diante. Isso é o "índice" ou "posição".

2. **Dicionário:** É uma estrutura que guarda pares "chave: valor". Ex.: `{"cultura": "café", "nome_fazenda": "Fazenda X"}`. Acessamos com `lavoura["cultura"]`.

3. **Parâmetro opcional:** Em `ler_numero(mensagem, tipo=float)`, o `tipo` tem valor padrão `float`. Se não informar, será usado `float`. Para inteiro: `ler_numero("Nº: ", int)`.

4. **`if __name__ == "__main__":`** Garante que `main()` só seja executada quando o arquivo é rodado diretamente, não quando é importado por outro arquivo.
