#Notificação com resumo de vendas (usando plyer)#
import pandas as pd
from plyer import notification

def analisar_vendas(arquivo_csv):
    # Carregar o arquivo CSV
    df = pd.read_csv(arquivo_csv)
    
    # Verificar se o arquivo possui as colunas esperadas
    if not {'Produto', 'Quantidade', 'Total'}.issubset(df.columns):
        raise ValueError("O arquivo CSV deve conter as colunas: Produto, Quantidade e Total")
    
    # Produto mais vendido
    produto_mais_vendido = df.groupby('Produto')['Quantidade'].sum().idxmax()
    
    # Total geral de vendas
    total_vendas = df['Total'].sum()
    
    return produto_mais_vendido, total_vendas

def enviar_notificacao(produto, total):
    mensagem = f"Produto mais vendido: {produto}\nTotal de vendas: R$ {total:,.2f}"
    notification.notify(
        title="Resumo de Vendas",
        message=mensagem,
        timeout=10
    )

if __name__ == "__main__":
    try:
        arquivo_csv = "vendas.csv"  # Substitua pelo nome correto do arquivo
        produto, total = analisar_vendas(arquivo_csv)
        enviar_notificacao(produto, total)
    except Exception as e:
        print(f"Erro: {e}")
