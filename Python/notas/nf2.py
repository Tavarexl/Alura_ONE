from xml.dom import minidom


with open("exemplo.xml", 'r', encoding='utf-8') as f:
    xml = minidom.parse(f)
    nome = [xml.getElementsByTagName("Nome")]
    cnpj = [xml.getElementsByTagName("CNPJ")]
    cpf = [xml.getElementsByTagName("CPF")]


    print(f'Nome da empresa: {nome[0].firstChild.data}')