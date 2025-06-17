# Agente de Consulta de Notas Fiscais

Este projeto contém um agente em Python aprimorado para consultar informações de arquivos CSV de notas fiscais (cabeçalho e itens), agora com suporte a diversas consultas avançadas e integração com WhatsApp via N8N.

## Funcionalidades

O agente permite realizar uma variedade de consultas sobre os dados das notas fiscais, incluindo:

*   Calcular o valor total de todas as notas fiscais.
*   Identificar a nota fiscal com o maior valor individual.
*   Calcular o valor médio das notas fiscais.
*   Listar os N principais fornecedores por valor total faturado (padrão N=5).
*   Listar os N principais destinatários por valor total comprado (padrão N=5).
*   Identificar o item que gerou a maior receita total.
*   Listar os N itens mais vendidos em termos de quantidade total (padrão N=10).
*   Calcular a quantidade média de itens por nota fiscal.
*   Listar os N principais estados de origem (UF Emitente) por número de notas ou por valor total (padrão N=5).
*   Listar os N principais estados de destino (UF Destinatário) por número de notas ou por valor total (padrão N=5).
*   Mostrar a distribuição das notas por Natureza da Operação.
*   *Mantém as consultas originais:* Identificar o fornecedor com maior valor e o item com maior quantidade.

O agente foi projetado para ser extensível, permitindo a adição de novas consultas conforme necessário.

## Integração com N8N, RAG e WhatsApp

Desenvolvemos uma solução completa e integrada para processamento inteligente de notas fiscais utilizando Python como tecnologia principal. O sistema realiza a leitura automatizada dos arquivos de notas fiscais, extraindo as informações mais relevantes através de técnicas avançadas de processamento de documentos.

Com base nos dados extraídos, construímos uma robusta base de conhecimento estruturada em formato de perguntas e respostas, implementando o conceito de RAG (Retrieval-Augmented Generation). Esta abordagem combina a recuperação de informações específicas com capacidades de geração de linguagem natural, permitindo que o sistema não apenas encontre dados relevantes nas notas fiscais, mas também formule respostas contextualizadas e precisas para as consultas dos usuários.

### Arquitetura RAG

A implementação do RAG proporciona:
* Recuperação semântica inteligente de informações relevantes
* Geração de respostas contextualizadas com base nos dados reais das notas fiscais
* Maior precisão nas consultas, evitando respostas genéricas ou imprecisas
* Capacidade de compreender perguntas complexas e relacionar informações de múltiplas fontes

### Integração com WhatsApp via N8N

Para tornar a solução ainda mais acessível e prática, implementamos um agente conversacional no N8N totalmente integrado ao WhatsApp. Esta integração permite que os usuários interajam com o sistema através de uma interface familiar e amplamente utilizada, facilitando a adoção da solução.

O sistema conta com um fluxo auxiliar inteligente que monitora continuamente as atualizações na base de perguntas e respostas. Sempre que novos dados são processados ou informações são modificadas, o fluxo automaticamente sincroniza essas alterações com o banco de dados, atualizando também os embeddings e índices do sistema RAG, garantindo que o agente conversacional tenha sempre acesso às informações mais atualizadas e mantenha a qualidade das respostas geradas.

Esta arquitetura RAG proporciona uma experiência fluida e em tempo real, onde os usuários podem consultar informações específicas sobre suas notas fiscais através de conversas naturais no WhatsApp, recebendo respostas precisas, contextualizadas e fundamentadas nos dados reais dos documentos.

### Benefícios da Solução Integrada

* Redução significativa do tempo de consulta a documentos fiscais
* Minimização de erros humanos no processamento de informações
* Disponibilidade 24/7 através do WhatsApp
* Escalabilidade para grandes volumes de notas fiscais
* Interface intuitiva que não requer treinamento específico dos usuários
* Respostas inteligentes baseadas em recuperação semântica de dados reais
* Capacidade de relacionar informações de múltiplas notas fiscais simultaneamente

## Arquivos Incluídos

*   `202401_NFs_Cabecalho.csv`: Arquivo CSV com os dados do cabeçalho das notas fiscais.
*   `202401_NFs_Itens.csv`: Arquivo CSV com os dados dos itens das notas fiscais.
*   `load_data.py`: Script Python contendo a função para carregar e pré-processar os dados.
*   `query_agent_v2.py`: Script Python principal que implementa o agente de consulta interativo (versão aprimorada).
*   `test_queries.py`: Script Python para executar testes automatizados das funções de consulta.
*   `perguntas_respostas_notas_fiscais.xlsx`: Planilha Excel com todas as perguntas e respostas.
*   `README_v3.md`: Este arquivo com as instruções atualizadas.
*   `todo.md`: Arquivo de acompanhamento do desenvolvimento (para referência).

## Pré-requisitos

*   Python 3.x
*   Biblioteca Pandas (`pip install pandas`)
*   Para a integração com WhatsApp: N8N instalado e configurado

## Como Usar

### Modo Console

1.  **Certifique-se** de que os arquivos `202401_NFs_Cabecalho.csv` e `202401_NFs_Itens.csv` estejam no mesmo diretório que os scripts Python, ou ajuste os caminhos dentro dos scripts (`load_data.py`, `query_agent_v2.py`, `test_queries.py`) para apontar para a localização correta dos arquivos.
    *   Atualmente, os scripts esperam encontrar os arquivos em `/home/ubuntu/upload/`. Se você executar em um local diferente, **precisará editar** as linhas `cabecalho_file = "."` e `itens_file = "."` nos scripts.
2.  **Execute** o agente de consulta aprimorado a partir do seu terminal:
    ```bash
    python query_agent_v2.py
    ```
3.  O agente iniciará e exibirá uma mensagem de boas-vindas.
4.  **Digite** `ajuda` para ver uma lista completa de exemplos de perguntas que o agente pode responder.
5.  **Digite** sua pergunta no prompt `Faça sua pergunta: `.
    *   **Exemplos:**
        *   `Qual o valor total das notas?`
        *   `Qual a nota de maior valor?`
        *   `Qual o valor médio das notas?`
        *   `Top 5 fornecedores por valor` (ou `Top 10 fornecedores por valor`)
        *   `Top 3 destinatários por valor`
        *   `Qual item gerou maior receita?`
        *   `Top 10 itens por quantidade` (ou `Top 5 itens por quantidade`)
        *   `Qual a média de itens por nota?`
        *   `Top 5 estados de origem por contagem`
        *   `Top 3 estados de origem por valor`
        *   `Top 5 estados de destino por contagem`
        *   `Top 10 estados de destino por valor`
        *   `Qual a distribuição por natureza da operação?`
6.  O agente processará a pergunta e exibirá o resultado.
7.  Para **encerrar** o agente, digite `sair`.

### Modo WhatsApp (via N8N)

1. Certifique-se de que o N8N esteja configurado e em execução.
2. Configure o webhook do WhatsApp para se conectar ao fluxo N8N.
3. Envie suas perguntas diretamente pelo WhatsApp para o número configurado.
4. O sistema RAG processará sua pergunta e enviará a resposta contextualizada de volta.

## Testando as Consultas (Opcional)

Você pode executar o script `test_queries.py` para verificar se todas as funções de consulta estão retornando resultados (útil após modificações):
```bash
python test_queries.py
```
