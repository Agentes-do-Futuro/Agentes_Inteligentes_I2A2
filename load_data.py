import pandas as pd

def load_and_preprocess_data(cabecalho_path, itens_path):
    """Carrega e pré-processa os dados dos arquivos CSV de cabeçalho e itens de notas fiscais."""
    try:
        # Carregar os arquivos CSV
        df_cabecalho = pd.read_csv(cabecalho_path, sep=',', decimal='.')
        df_itens = pd.read_csv(itens_path, sep=',', decimal='.')

        # Converter colunas de data para datetime
        date_cols_cabecalho = ['DATA EMISSÃO', 'DATA/HORA EVENTO MAIS RECENTE']
        for col in date_cols_cabecalho:
            if col in df_cabecalho.columns:
                df_cabecalho[col] = pd.to_datetime(df_cabecalho[col], errors='coerce')

        date_cols_itens = ['DATA EMISSÃO'] # Apenas DATA EMISSÃO está presente nos itens, conforme visto
        for col in date_cols_itens:
             if col in df_itens.columns:
                df_itens[col] = pd.to_datetime(df_itens[col], errors='coerce')

        # Lidar com possíveis valores ausentes ou tipos incorretos, se necessário
        # Exemplo: Converter colunas numéricas que podem ter sido lidas como objeto
        numeric_cols_cabecalho = ['VALOR NOTA FISCAL']
        for col in numeric_cols_cabecalho:
            if col in df_cabecalho.columns:
                 df_cabecalho[col] = pd.to_numeric(df_cabecalho[col], errors='coerce')

        numeric_cols_itens = ['QUANTIDADE', 'VALOR UNITÁRIO', 'VALOR TOTAL']
        for col in numeric_cols_itens:
            if col in df_itens.columns:
                df_itens[col] = pd.to_numeric(df_itens[col], errors='coerce')

        print("Dados carregados e pré-processados com sucesso.")
        print("\nCabeçalho - Primeiras linhas:")
        print(df_cabecalho.head())
        print("\nCabeçalho - Tipos de dados:")
        print(df_cabecalho.info())

        print("\nItens - Primeiras linhas:")
        print(df_itens.head())
        print("\nItens - Tipos de dados:")
        print(df_itens.info())

        return df_cabecalho, df_itens

    except FileNotFoundError:
        print(f"Erro: Um ou ambos os arquivos não foram encontrados: {cabecalho_path}, {itens_path}")
        return None, None
    except Exception as e:
        print(f"Erro ao carregar ou pré-processar os dados: {e}")
        return None, None

if __name__ == "__main__":
    cabecalho_file = '/home/ubuntu/upload/202401_NFs_Cabecalho.csv'
    itens_file = '/home/ubuntu/upload/202401_NFs_Itens.csv'
    df_cabecalho, df_itens = load_and_preprocess_data(cabecalho_file, itens_file)

