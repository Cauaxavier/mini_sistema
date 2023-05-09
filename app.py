from time import sleep


def main():
    while True:
        arq = 'lista.txt'
        arquivoExiste(arq)
        if not arquivoExiste(arq):
            criarAquivo(arq)
        escolha = menu(['Ver pessoas cadastradas',
                       'Cadastrar nova pessoa', 'Sair do sistema'])
        if escolha == 1:
            cabecalho('NO CADASTRADO')
            pessoas(arq)
        elif escolha == 2:
            cabecalho('CADASTRAR PESSOAS')
            cont = leiaInt('Quantas pessoas deseja cadastrar? ')
            for i in range(0, cont):
                nome = str(input('Nome: ')).strip().capitalize()
                idade = leiaInt('Idade: ')
                cadastro(arq, nome, idade)
        elif escolha == 3:
            cabecalho('\033[32mSaindo do sistema...\033[m')
            break
        else:
            print('\033[31mOpção inválida, tente novamente\033[m')
        sleep(1)


def cabecalho(txt):
    print('-' * 60)
    print(txt.center(60))
    print('-' * 60)


def menu(opcoes):
    c = 1
    cabecalho('MENU PRINCIPAL')
    for opc in opcoes:
        print(f'{c} - \033[34m{opc}\033[m')
        c += 1
    print('-' * 60)
    num = leiaInt('\033[33mEscolha uma opção:\033[m ')
    return num


def leiaInt(msg):
    valor = 0
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31m[ERRO], dado inválido, tente novamente.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar o valor.\033[m')
            return 0
        else:
            return valor


def arquivoExiste(a):
    try:
        arquivo = open(a, 'rt')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarAquivo(a):
    try:
        arquivo = open(a, 'wt+')
        arquivo.close()
    except:
        print('Não foi possivel criar o arquivo')
    else:
        print('Arquivo criado com sucesso.')


def pessoas(a):
    try:
        arquivo = open(a, 'rt',  encoding="utf-8")
    except:
        print('Não foi possivel abrir tal arquivo.')
    else:
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', ' ')
            print(f'{dado[0]:<20}{dado[1]:>3} anos')
    finally:
        arquivo.close()


def cadastro(a, nome='<desconhecido>', idade=0):
    try:
        arquivo = open(a, 'at', encoding='utf-8')
    except:
        print('\033[31mHouve um erro na abertura do arquivo.\033[m')
    else:
        try:
            arquivo.write(f'{nome};{idade}\n')
        except:
            print('\033[31m[ERRO] Não foi possivel cadastrar a pessoa.\033[m')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso.')


main()
