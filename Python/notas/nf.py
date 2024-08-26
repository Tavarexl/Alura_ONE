from xml.dom import minidom


with open("exemplo.xml", 'r', encoding='utf-8') as f:
    xml = minidom.parse(f)
    nome = xml.getElementsByTagName("Nome")
    cnpj = xml.getElementsByTagName("CNPJ")
    cpf = xml.getElementsByTagName("CPF")


    print(f'Nome da empresa: {nome.firstChild.data} ')
    print(f'CNPJ da empresa: {cnpj[0].fisrtChild.data}')
    print('\n')
    print(f'Nome do cliente: {nome[1].fisrtChild.data} ')
    print(f'CPF do cliente: {cpf[0].fisrtChild.data}')