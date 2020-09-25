nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"


def isEmpty(value:str) -> bool:
        return (value == None) or (len(value) == value.count(" "))
def dados_loja():
    # Implemente aqui
    global numero
    if (nome_loja == ""):
        raise Exception("O campo nome da loja é obrigatório")
    if (logradouro == ""):
        raise Exception("O campo logradouro do endereço é obrigatório")
    if (numero == 0):
        numero = ("s/n")
    if(cnpj == ""):
        raise Exception("O campo CNPJ da loja é obrigatório")
    if (municipio == ""):
        raise Exception("O campo município do endereço é obrigatório")
    if (estado == ""):
        raise Exception("O campo estado do endereço é obrigatório")
    if (inscricao_estadual == ""):
        raise Exception("O campo inscrição estadual da loja é obrigatório")

    part2 = f"{logradouro}, {numero}"
    if not isEmpty (complemento):
        part2 += f" {complemento}"
    part3 = str()
    if not isEmpty (bairro):
        part3 += f"{bairro} - "
    part3 += f"{municipio} - {estado}"
    part4 = str()
    if not isEmpty (cep):
        part4 = f"CEP:{cep}"
    if not isEmpty(telefone):
        if not isEmpty(part4):
            part4 += " "
        part4 += f"Tel {telefone}"     
    if not isEmpty(part4):
        part4 += "\n"
    part5 = str()
    if not isEmpty(observacao):
        part5 += f"{observacao}"
    
    output = f"{nome_loja}\n"
    output += f"{part2}\n"
    output += f"{part3}\n"
    output += f"{part4}"
    output += f"{part5}\n"
    output += f"CNPJ: {cnpj}\n"
    output += f"IE: {inscricao_estadual}"

    return output
