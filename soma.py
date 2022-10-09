vlr_venda = float(input('Insira o valor total da venda : '))
vlr_desconto_percent = vlr_venda * 0.10
vlr_desconto = vlr_venda - vlr_desconto_percent 
vlr_parcela = vlr_venda / 3
comissao_vendedor = vlr_desconto * 0.05
comissao_vendedorb = vlr_venda * 0.05

print(f'O valor de venda é {vlr_venda} .')
print(f'O valor de desconto é de {vlr_desconto} .')
print(f' O valor da parcela a 3X sem juros sai a {vlr_parcela}')
print(f' A comissão do vendedor acaso a venda sai a vista e de {comissao_vendedor}')
print(f' A comissão do vendedor acaso a venda sai a prazo com 3x e de {comissao_vendedorb}')