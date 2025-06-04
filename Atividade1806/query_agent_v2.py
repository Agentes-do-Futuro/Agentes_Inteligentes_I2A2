import pandas as pd
from load_data import load_and_preprocess_data

# --- Funções de Consulta --- 

def get_total_invoice_value(df_cabecalho):
    """Calcula o valor total de todas as notas fiscais."""
    if df_cabecalho is None or 'VALOR NOTA FISCAL' not in df_cabecalho.columns:
        return "Erro: DataFrame de cabeçalho inválido ou coluna 'VALOR NOTA FISCAL' ausente."
    total_value = df_cabecalho['VALOR NOTA FISCAL'].sum()
    return f"O valor total de todas as notas fiscais é R$ {total_value:.2f}."

def get_highest_value_invoice(df_cabecalho):
    """Encontra a nota fiscal com o maior valor individual."""
    if df_cabecalho is None or 'VALOR NOTA FISCAL' not in df_cabecalho.columns or 'CHAVE DE ACESSO' not in df_cabecalho.columns:
        return "Erro: DataFrame de cabeçalho inválido ou colunas necessárias ausentes."
    highest_invoice = df_cabecalho.loc[df_cabecalho['VALOR NOTA FISCAL'].idxmax()]
    return f"A nota fiscal com maior valor é a de chave '{highest_invoice['CHAVE DE ACESSO']}' com R$ {highest_invoice['VALOR NOTA FISCAL']:.2f}."

def get_average_invoice_value(df_cabecalho):
    """Calcula o valor médio das notas fiscais."""
    if df_cabecalho is None or 'VALOR NOTA FISCAL' not in df_cabecalho.columns:
        return "Erro: DataFrame de cabeçalho inválido ou coluna 'VALOR NOTA FISCAL' ausente."
    avg_value = df_cabecalho['VALOR NOTA FISCAL'].mean()
    return f"O valor médio das notas fiscais é R$ {avg_value:.2f}."

def get_top_suppliers_by_value(df_cabecalho, n=5):
    """Lista os N principais fornecedores por valor total faturado."""
    if df_cabecalho is None or 'RAZÃO SOCIAL EMITENTE' not in df_cabecalho.columns or 'VALOR NOTA FISCAL' not in df_cabecalho.columns:
        return "Erro: DataFrame de cabeçalho inválido ou colunas necessárias ausentes."
    supplier_totals = df_cabecalho.groupby('RAZÃO SOCIAL EMITENTE')['VALOR NOTA FISCAL'].sum().nlargest(n)
    result = f"Os {n} principais fornecedores por valor total são:\n"
    for supplier, value in supplier_totals.items():
        result += f"- {supplier}: R$ {value:.2f}\n"
    return result.strip()

def get_top_recipients_by_value(df_cabecalho, n=5):
    """Lista os N principais destinatários por valor total comprado."""
    if df_cabecalho is None or 'NOME DESTINATÁRIO' not in df_cabecalho.columns or 'VALOR NOTA FISCAL' not in df_cabecalho.columns:
        return "Erro: DataFrame de cabeçalho inválido ou colunas necessárias ausentes."
    recipient_totals = df_cabecalho.groupby('NOME DESTINATÁRIO')['VALOR NOTA FISCAL'].sum().nlargest(n)
    result = f"Os {n} principais destinatários por valor total são:\n"
    for recipient, value in recipient_totals.items():
        result += f"- {recipient}: R$ {value:.2f}\n"
    return result.strip()

def get_top_item_by_revenue(df_itens):
    """Encontra o item que gerou a maior receita total."""
    if df_itens is None or 'DESCRIÇÃO DO PRODUTO/SERVIÇO' not in df_itens.columns or 'VALOR TOTAL' not in df_itens.columns:
        return "Erro: DataFrame de itens inválido ou colunas necessárias ausentes."
    item_revenues = df_itens.groupby('DESCRIÇÃO DO PRODUTO/SERVIÇO')['VALOR TOTAL'].sum()
    top_item = item_revenues.idxmax()
    max_revenue = item_revenues.max()
    return f"O item que gerou maior receita total é '{top_item}' com R$ {max_revenue:.2f}."

def get_top_items_by_quantity(df_itens, n=10):
    """Lista os N itens mais vendidos em termos de quantidade total."""
    if df_itens is None or 'DESCRIÇÃO DO PRODUTO/SERVIÇO' not in df_itens.columns or 'QUANTIDADE' not in df_itens.columns or 'UNIDADE' not in df_itens.columns:
        return "Erro: DataFrame de itens inválido ou colunas necessárias ausentes."
    item_quantities = df_itens.groupby('DESCRIÇÃO DO PRODUTO/SERVIÇO')['QUANTIDADE'].sum().nlargest(n)
    result = f"Os {n} itens mais vendidos por quantidade são:\n"
    for item, quantity in item_quantities.items():
        # Tenta obter a unidade mais comum para o item (pode variar)
        try:
            unit = df_itens.loc[df_itens['DESCRIÇÃO DO PRODUTO/SERVIÇO'] == item, 'UNIDADE'].mode()[0]
        except IndexError:
            unit = "(unidade não especificada)"
        result += f"- {item}: {quantity} {unit}\n"
    return result.strip()

def get_avg_items_per_invoice(df_itens):
    """Calcula a quantidade média de itens por nota fiscal."""
    if df_itens is None or 'CHAVE DE ACESSO' not in df_itens.columns:
         return "Erro: DataFrame de itens inválido ou coluna 'CHAVE DE ACESSO' ausente."
    items_per_invoice = df_itens.groupby('CHAVE DE ACESSO').size()
    avg_items = items_per_invoice.mean()
    return f"A média de itens por nota fiscal é {avg_items:.2f}."

def get_top_origin_states(df_cabecalho, by='count', n=5):
    """Lista os N principais estados de origem (UF Emitente) por contagem ou valor."""
    if df_cabecalho is None or 'UF EMITENTE' not in df_cabecalho.columns:
        return "Erro: DataFrame de cabeçalho inválido ou coluna 'UF EMITENTE' ausente."
    if by == 'value' and 'VALOR NOTA FISCAL' not in df_cabecalho.columns:
        return "Erro: Coluna 'VALOR NOTA FISCAL' ausente para agrupar por valor."
        
    if by == 'value':
        top_states = df_cabecalho.groupby('UF EMITENTE')['VALOR NOTA FISCAL'].sum().nlargest(n)
        result = f"Os {n} principais estados de origem por valor total são:\n"
        for state, value in top_states.items():
            result += f"- {state}: R$ {value:.2f}\n"
    else: # by count
        top_states = df_cabecalho['UF EMITENTE'].value_counts().nlargest(n)
        result = f"Os {n} principais estados de origem por número de notas são:\n"
        for state, count in top_states.items():
            result += f"- {state}: {count} notas\n"
    return result.strip()

def get_top_destination_states(df_cabecalho, by='count', n=5):
    """Lista os N principais estados de destino (UF Destinatário) por contagem ou valor."""
    if df_cabecalho is None or 'UF DESTINATÁRIO' not in df_cabecalho.columns:
        return "Erro: DataFrame de cabeçalho inválido ou coluna 'UF DESTINATÁRIO' ausente."
    if by == 'value' and 'VALOR NOTA FISCAL' not in df_cabecalho.columns:
        return "Erro: Coluna 'VALOR NOTA FISCAL' ausente para agrupar por valor."
        
    if by == 'value':
        top_states = df_cabecalho.groupby('UF DESTINATÁRIO')['VALOR NOTA FISCAL'].sum().nlargest(n)
        result = f"Os {n} principais estados de destino por valor total são:\n"
        for state, value in top_states.items():
            result += f"- {state}: R$ {value:.2f}\n"
    else: # by count
        top_states = df_cabecalho['UF DESTINATÁRIO'].value_counts().nlargest(n)
        result = f"Os {n} principais estados de destino por número de notas são:\n"
        for state, count in top_states.items():
            result += f"- {state}: {count} notas\n"
    return result.strip()

def get_operation_nature_distribution(df_cabecalho):
    """Mostra a distribuição das notas por Natureza da Operação."""
    if df_cabecalho is None or 'NATUREZA DA OPERAÇÃO' not in df_cabecalho.columns:
        return "Erro: DataFrame de cabeçalho inválido ou coluna 'NATUREZA DA OPERAÇÃO' ausente."
    distribution = df_cabecalho['NATUREZA DA OPERAÇÃO'].value_counts()
    result = "Distribuição por Natureza da Operação:\n"
    for nature, count in distribution.items():
        result += f"- {nature}: {count} notas\n"
    return result.strip()

# --- Função Principal do Agente --- 

def main():
    cabecalho_file = '/home/ubuntu/upload/202401_NFs_Cabecalho.csv'
    itens_file = '/home/ubuntu/upload/202401_NFs_Itens.csv'
    
    df_cabecalho, df_itens = load_and_preprocess_data(cabecalho_file, itens_file)
    
    if df_cabecalho is None or df_itens is None:
        print("Não foi possível carregar os dados. Encerrando o agente.")
        return

    print("\n--- Agente de Consulta de Notas Fiscais (v2.0) ---")
    print("Olá! Posso ajudar a consultar informações sobre as notas fiscais.")
    print("Digite sua pergunta ou 'ajuda' para ver exemplos, 'sair' para encerrar.")

    while True:
        try:
            query = input("\nFaça sua pergunta: ").strip().lower()

            if query == 'sair':
                print("Encerrando o agente. Até logo!")
                break
            elif query == 'ajuda':
                print("\nExemplos de perguntas que posso responder:")
                print("- Qual o valor total das notas?")
                print("- Qual a nota de maior valor?")
                print("- Qual o valor médio das notas?")
                print("- Top 5 fornecedores por valor")
                print("- Top 5 destinatários por valor")
                print("- Qual item gerou maior receita?")
                print("- Top 10 itens por quantidade")
                print("- Qual a média de itens por nota?")
                print("- Top 5 estados de origem (por valor ou por contagem)?")
                print("- Top 5 estados de destino (por valor ou por contagem)?")
                print("- Qual a distribuição por natureza da operação?")
                print("- (Original) Qual o fornecedor com maior valor?") # Mantendo a original
                print("- (Original) Qual o item com maior quantidade?") # Mantendo a original
            
            # Interpretação das perguntas (simplificada)
            elif 'valor total' in query and 'nota' in query:
                print(get_total_invoice_value(df_cabecalho))
            elif ('nota' in query and 'maior valor' in query) or ('maior nota' in query):
                 print(get_highest_value_invoice(df_cabecalho))
            elif 'valor médio' in query and 'nota' in query:
                print(get_average_invoice_value(df_cabecalho))
            elif 'top' in query and 'fornecedor' in query and 'valor' in query:
                n = 5 # Padrão
                try: n = int(query.split('top')[1].split()[0]) # Tenta pegar o número (ex: top 10)
                except: pass
                print(get_top_suppliers_by_value(df_cabecalho, n))
            elif 'top' in query and 'destinatário' in query and 'valor' in query:
                n = 5 # Padrão
                try: n = int(query.split('top')[1].split()[0])
                except: pass
                print(get_top_recipients_by_value(df_cabecalho, n))
            elif 'item' in query and 'maior receita' in query:
                print(get_top_item_by_revenue(df_itens))
            elif 'top' in query and 'item' in query and 'quantidade' in query:
                n = 10 # Padrão
                try: n = int(query.split('top')[1].split()[0])
                except: pass
                print(get_top_items_by_quantity(df_itens, n))
            elif 'média de itens' in query and 'nota' in query:
                print(get_avg_items_per_invoice(df_itens))
            elif 'top' in query and 'estado' in query and 'origem' in query:
                n = 5
                by = 'count'
                try: n = int(query.split('top')[1].split()[0])
                except: pass
                if 'valor' in query: by = 'value'
                print(get_top_origin_states(df_cabecalho, by, n))
            elif 'top' in query and 'estado' in query and 'destino' in query:
                n = 5
                by = 'count'
                try: n = int(query.split('top')[1].split()[0])
                except: pass
                if 'valor' in query: by = 'value'
                print(get_top_destination_states(df_cabecalho, by, n))
            elif 'distribuição' in query and 'natureza da operação' in query:
                print(get_operation_nature_distribution(df_cabecalho))
            # Mantendo as perguntas originais como fallback ou específicas
            elif 'fornecedor' in query and ('maior valor' in query or 'montante' in query):
                print(get_top_suppliers_by_value(df_cabecalho, n=1)) # Usa a função top com n=1
            elif 'item' in query and ('maior quantidade' in query or 'volume' in query):
                 print(get_top_items_by_quantity(df_itens, n=1)) # Usa a função top com n=1
            else:
                print("Desculpe, não entendi essa pergunta. Digite 'ajuda' para ver exemplos.")
        except Exception as e:
            print(f"Ocorreu um erro ao processar sua consulta: {e}")

if __name__ == "__main__":
    main()

