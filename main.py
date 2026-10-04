total_vendas = 0

vendas_online = 0

quantidade_eletronico = 0
quantidade_papelaria = 0
quantidade_informatica = 0
quantidade_acessorio = 0

faturamento = 0

with open("vendas_pratica_python_120_registros.csv", "r", encoding="utf-8") as arquivo:
    next(arquivo)

    maior_valor = 0
    produto_maior_venda = ""

    for linha in arquivo:
        linha = linha.strip()
        dados = linha.split(",")
        
        id_venda = int(dados[0])
        produto = dados[1]
        categoria = dados[2]
        valor = float(dados[3])
        quantidade = int(dados[4])
        canal = dados[5]

        if not linha:
            continue

        total_vendas += 1

        if canal == "Online":
            vendas_online += 1

        if categoria == "Eletronico":
           quantidade_eletronico += 1

        if categoria == "Papelaria":
           quantidade_papelaria += 1

        if categoria == "Informatica":
           quantidade_informatica += 1

        if categoria == "Acessorio":
           quantidade_acessorio += 1

        total_item = valor * quantidade
        faturamento += total_item

        if total_item > maior_valor:
            maior_valor = total_item
            produto_maior_venda = produto

print("=========== Relatório de Vendas ===========")
print("-------------------------------------------")
print("Quantidade de vendas:", total_vendas)
print("-------------------------------------------")
print("Vendas por canal:")
print("Online:", vendas_online)
print("Loja:", total_vendas - vendas_online)
print("-------------------------------------------")
print("Quantidade por Categoria:")
print("Eletrônico:", quantidade_eletronico)
print("Papelaria:", quantidade_papelaria)
print("Informática:", quantidade_informatica)
print("Acessórios:", quantidade_acessorio)
print("-------------------------------------------")
print("Faturamento total: R$ {:.2f}".format(faturamento))
print("-------------------------------------------")
print("Produto da maior venda:", produto_maior_venda)
print(f"Valor da maior venda: R$ {maior_valor:.2f}")
print("===========================================")