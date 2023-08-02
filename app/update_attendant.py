import pandas as pd


def atualiza_associado(planilha_excel):
    df = pd.read_excel(planilha_excel)

    df_selected = df[['B', 'S']]

    df_unique = df_selected.drop_duplicates(subset=['S'])

    return df_unique

