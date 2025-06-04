import pandas as pd
from load_data import load_and_preprocess_data
# Import functions from the new agent script
from query_agent_v2 import (
    get_total_invoice_value,
    get_highest_value_invoice,
    get_average_invoice_value,
    get_top_suppliers_by_value,
    get_top_recipients_by_value,
    get_top_item_by_revenue,
    get_top_items_by_quantity,
    get_avg_items_per_invoice,
    get_top_origin_states,
    get_top_destination_states,
    get_operation_nature_distribution
)

def run_tests():
    cabecalho_file = '/home/ubuntu/upload/202401_NFs_Cabecalho.csv'
    itens_file = '/home/ubuntu/upload/202401_NFs_Itens.csv'

    print("Carregando e pré-processando dados...")
    # Reutiliza a função de carregamento já existente
    df_cabecalho, df_itens = load_and_preprocess_data(cabecalho_file, itens_file)

    if df_cabecalho is None or df_itens is None:
        print("Falha ao carregar dados. Abortando testes.")
        return

    print("\n--- Iniciando Testes das Consultas Avançadas ---")

    print("\n1. Valor total das notas:")
    print(get_total_invoice_value(df_cabecalho))

    print("\n2. Nota de maior valor:")
    print(get_highest_value_invoice(df_cabecalho))

    print("\n3. Valor médio das notas:")
    print(get_average_invoice_value(df_cabecalho))

    print("\n4. Top 3 Fornecedores por Valor:")
    print(get_top_suppliers_by_value(df_cabecalho, n=3))

    print("\n5. Top 3 Destinatários por Valor:")
    print(get_top_recipients_by_value(df_cabecalho, n=3))

    print("\n6. Item com maior receita:")
    print(get_top_item_by_revenue(df_itens))

    print("\n7. Top 5 Itens por Quantidade:")
    print(get_top_items_by_quantity(df_itens, n=5))

    print("\n8. Média de itens por nota:")
    print(get_avg_items_per_invoice(df_itens))

    print("\n9. Top 3 Estados de Origem (Contagem):")
    print(get_top_origin_states(df_cabecalho, by='count', n=3))

    print("\n10. Top 3 Estados de Origem (Valor):")
    print(get_top_origin_states(df_cabecalho, by='value', n=3))

    print("\n11. Top 3 Estados de Destino (Contagem):")
    print(get_top_destination_states(df_cabecalho, by='count', n=3))

    print("\n12. Top 3 Estados de Destino (Valor):")
    print(get_top_destination_states(df_cabecalho, by='value', n=3))

    print("\n13. Distribuição por Natureza da Operação:")
    print(get_operation_nature_distribution(df_cabecalho))

    print("\n--- Testes Concluídos --- ")

if __name__ == "__main__":
    run_tests()

