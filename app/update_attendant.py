import pandas as pd


# Function that recieve a excel workbook and filter the columns based in 
def atualiza_associado(planilha_excel):
    df = pd.read_excel(planilha_excel)
    df_selected = df[['Proprietário do caso', 'E-mail do Proprietário']].copy()
    df_unique = df_selected.drop_duplicates(subset=df_selected.columns[1])

    return df_unique

