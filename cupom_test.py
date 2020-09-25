import cupom
import pytest

# Refatoramento da verificação de campo obrigatório
def verifica_campo_obrigatorio(mensagem_esperada):
  with pytest.raises(Exception) as excinfo:
    cupom.dados_loja()
  the_exception = excinfo.value
  assert mensagem_esperada == str(the_exception)

# Todas as variáveis preenchidas
cupom.nome_loja = "Loja 1"
cupom.logradouro = "Log 1"
cupom.numero = 10
cupom.complemento = "C1"
cupom.bairro = "Bai 1"
cupom.municipio = "Mun 1"
cupom.estado = "E1"
cupom.cep = "11111-111"
cupom.telefone = "(11) 1111-1111"
cupom.observacao = "Obs 1"
cupom.cnpj = "11.111.111/1111-11"
cupom.inscricao_estadual = "123456789"

TEXTO_ESPERADO_LOJA_COMPLETA = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_loja_completa():
    assert cupom.dados_loja() == TEXTO_ESPERADO_LOJA_COMPLETA

def test_nome_vazio():
    global nome_loja
    cupom.nome_loja = ""
    verifica_campo_obrigatorio("O campo nome da loja é obrigatório") 
    cupom.nome_loja = "Loja 1"

def test_logradouro_vazio():
    global logradouro
    cupom.logradouro = ""
    verifica_campo_obrigatorio("O campo logradouro do endereço é obrigatório")
    cupom.logradouro = "Log 1"

TEXTO_ESPERADO_SEM_NUMERO = '''Loja 1
Log 1, s/n C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_numero_zero():
    global numero
    cupom.numero = 0
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_NUMERO
    cupom.numero = 10

TEXTO_ESPERADO_SEM_COMPLEMENTO = '''Loja 1
Log 1, 10
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_complemento():
    global complemento
    cupom.complemento = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_COMPLEMENTO
    cupom.complemento = "C1"

TEXTO_ESPERADO_SEM_BAIRRO = '''Loja 1
Log 1, 10 C1
Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_bairro():
    global bairro
    cupom.bairro = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_BAIRRO
    cupom.bairro = "Bai 1"

def test_municipio_vazio():
    global municipio
    cupom.municipio = ""
    verifica_campo_obrigatorio("O campo município do endereço é obrigatório")
    cupom.municipio = "Mun 1"

def test_estado_vazio():
    global estado
    cupom.estado = ""
    verifica_campo_obrigatorio("O campo estado do endereço é obrigatório")
    cupom.estado = "E1"

TEXTO_ESPERADO_SEM_CEP = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
Tel (11) 1111-1111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_cep():
    global cep
    cupom.cep = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_CEP
    cupom.cep = "11111-111"

TEXTO_ESPERADO_SEM_TELEFONE = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111
Obs 1
CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_telefone():
    global telefone
    cupom.telefone = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_TELEFONE
    cupom.telefone = "(11) 1111-1111"

TEXTO_ESPERADO_SEM_OBSERVACAO = '''Loja 1
Log 1, 10 C1
Bai 1 - Mun 1 - E1
CEP:11111-111 Tel (11) 1111-1111

CNPJ: 11.111.111/1111-11
IE: 123456789'''

def test_sem_observacao():
    global observacao
    cupom.observacao = None
    assert cupom.dados_loja() == TEXTO_ESPERADO_SEM_OBSERVACAO
    cupom.observacao = "Obs 1"

def test_cnpj_vazio():
    global cnpj
    cupom.cnpj = ""
    verifica_campo_obrigatorio("O campo CNPJ da loja é obrigatório")
    cupom.cnpj = "11.111.111/1111-11"

def test_inscricao_estadual_vazia():
    global inscricao_estadual
    cupom.inscricao_estadual = ""
    verifica_campo_obrigatorio("O campo inscrição estadual da loja é obrigatório")
    cupom.inscricao_estadual = "123456789"

def test_exercicio2_customizado():
    global nome_loja
    global logradouro
    global numero
    global complemento
    global bairro
    global municipio
    global estado
    global cep
    global telefone
    global observacao
    global cnpj
    global inscricao_estadual
    
    # Defina seus próprios valores para as variáveis a seguir
    cupom.nome_loja = "Smelly Cat"
    cupom.logradouro = "Rua Etheria"
    cupom.numero = 205
    cupom.complemento = "Perto da velhinha que mora em uma caverna"
    cupom.bairro = "Br. Templo do Cristal"
    cupom.municipio = "Beach City"
    cupom.estado = "BC"
    cupom.cep = "8051-604"
    cupom.telefone = "(66)4002-8922"
    cupom.observacao = "Por Favor ignorar os exército Intergalácticos em guerra tentando dominar o planeta"
    cupom.cnpj = "53.409.609/0001-85"
    cupom.inscricao_estadual = "512.670.302.653"

    expected = "Smelly Cat\n"
    expected += "Rua Etheria, 205 Perto da velhinha que mora em uma caverna\n"
    expected += "Br. Templo do Cristal - Beach City - BC\n"
    expected += "CEP:8051-604 Tel (66)4002-8922\n"
    expected += "Por Favor ignorar os exército Intergalácticos em guerra tentando dominar o planeta\n"
    expected +="CNPJ: 53.409.609/0001-85\n"
    expected += "IE: 512.670.302.653"
    #E atualize o texto esperado abaixo
    assert cupom.dados_loja() == expected
