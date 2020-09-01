import json

# Recuperacao dos dados originais do banco de dados

# Baseado em https://github.com/python-engineer/python-engineer-notebooks/blob/master/advanced-python/11-JSON.ipynb
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf8') as arquivo:
        return json.load(arquivo)

def corrigir_nomes(dados):
    for i in range(len(dados)):
        for j in range(len(dados[i]['name'])):   
            if dados[i]['name'][j] == 'æ':
                dados[i]['name'] = dados[i]['name'][:j] + 'a' + dados[i]['name'][j+1:]

            elif dados[i]['name'][j]== '¢':
                dados[i]['name'] = dados[i]['name'][:j] + 'c' + dados[i]['name'][j+1:] 
            
            elif dados[i]['name'][j] == 'ø':
                dados[i]['name'] = dados[i]['name'][:j] + 'o' + dados[i]['name'][j+1:]

            elif dados[i]['name'][j] == 'ß':
                dados[i]['name'] = dados[i]['name'][:j] + 'b' + dados[i]['name'][j+1:]
    
    return dados

# Baseado em https://docs.python.org/2/library/functions.html#isinstance
#            https://stackoverflow.com/questions/1549801/what-are-the-differences-between-type-and-isinstance
def corrigir_precos(dados):
    for i in range(len(dados)):
        if isinstance(dados[i]['price'], str):
            dados[i]['price'] = float(dados[i]['price'])

    return dados

# Baseado em https://github.com/python-engineer/python-engineer-notebooks/blob/master/advanced-python/03-Dictionary.ipynb
#            https://stackoverflow.com/questions/45157521/insert-an-item-into-a-specific-location-in-a-dict-in-a-single-statement
def corrigir_quantidade(dados):
    for i in range(len(dados)):
        if 'quantity' not in dados[i]:
            dados[i] = {k: v for k, v in (list(dados[i].items())[:2] + [('quantity', 0)] + list(dados[i].items())[2:])}
 
    return dados

def exportar_arquivo(nome_arquivo):
    with open(nome_arquivo, 'w', encoding='utf8') as arquivo:
        return json.dump(dados, arquivo, indent=4, ensure_ascii=False)

# Validação do banco de dados corrigido

# Baseado em https://docs.python.org/3/howto/sorting.html
#            https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
def imprime_lista(nome_arquivo):
    
    impressao_dados = sorted(ler_arquivo(nome_arquivo), key=lambda k: (k['category'], k['id']))

    for i in range(len(impressao_dados)):
        print(impressao_dados[i]['name'])

    return

def valor_total(nome_arquivo):
    calcula_dados = ler_arquivo(nome_arquivo)

    valor_total = dict()

    for i in range(len(calcula_dados)):
        if calcula_dados[i]['category'] in valor_total:
            valor_total[calcula_dados[i]['category']] = round(valor_total[calcula_dados[i]['category']] +
                                                        calcula_dados[i]['quantity'] * calcula_dados[i]['price'], 2)
                
        else:
            valor_total[calcula_dados[i]['category']] = round(calcula_dados[i]['quantity'] *
                                                        calcula_dados[i]['price'], 2)

    return valor_total

# Recuperação
dados = ler_arquivo('broken-database.json')
dados = corrigir_quantidade(corrigir_precos(corrigir_nomes(dados)))
exportar_arquivo('saida.json')

# Validação
imprime_lista('saida.json')
valor_total('saida.json')