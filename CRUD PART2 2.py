# Aluno: Enrique Vidal Silveira
# Disciplina: Raciocínio Computacional.
import json

#salvar a lista de estudantes em uma lista JSON
def salvar_lista_estudantes(lista_estudantes):
    with open("estudantes.json", "w") as arquivo:
        json.dump(lista_estudantes, arquivo)

#recuperar lista de estudantes em um arquivo JSON
def recuperar_lista_estudantes():
    try:
        with open("estudantes.json", "r") as arquivo:
            lista_estudantes = json.load(arquivo)
            return lista_estudantes
    except FileNotFoundError:
        return []

#incluir estudante
def incluir_estudante(lista_estudantes):
    codigo = int(input("Digite o código do estudante: "))
    nome = input("Digite o nome do estudante: ")
    cpf = input("Digite o CPF do estudante: ")
    novo_estudante = {"codigo": codigo, "nome": nome, "cpf": cpf}
    lista_estudantes.append(novo_estudante)
    salvar_lista_estudantes(lista_estudantes) #Opção de salvar
    print("Estudante cadastrado com sucesso!")

#listar estudante
def listar_estudantes(lista_estudantes):
    if lista_estudantes:
        for estudante in lista_estudantes:
            print("Código:", estudante["codigo"])
            print("Nome:", estudante["nome"])
            print("CPF:", estudante["cpf"])
            print()
    else:
        print("Não há alunos cadastrados.")

#excluir estudante
def excluir_estudante(lista_estudantes):
    codigo_para_excluir = int(input("Digite o código do estudante que deseja excluir: "))
    for estudante in lista_estudantes:
        if estudante["codigo"] == codigo_para_excluir:
            lista_estudantes.remove(estudante)
            salvar_lista_estudantes(lista_estudantes) #Opção de salvar
            print("Estudante excluído com sucesso!")
            return
    print("Estudante não encontrado.")

#editar estudante
def editar_estudante(lista_estudantes):
    codigo_para_editar = int(input("Digite o código do estudante que deseja editar: "))
    for estudante in lista_estudantes:
        if estudante["codigo"] == codigo_para_editar:
            novo_codigo = int(input("Digite o novo código do estudante: "))
            novo_nome = input("Digite o novo nome do estudante: ")
            novo_cpf = input("Digite o novo CPF do estudante: ")
            estudante["codigo"] = novo_codigo
            estudante["nome"] = novo_nome
            estudante["cpf"] = novo_cpf
            salvar_lista_estudantes(lista_estudantes) #Opção de salvar
            print("Estudante editado com sucesso!")
            return
    print("Estudante não encontrado.")

#salvar lista de professores em um arquivo JSON
def salvar_lista_professores(lista_professores):
    with open("professores.json", "w") as arquivo:
        json.dump(lista_professores, arquivo)

#recuperar a lista de professores de um arquivo JSON
def recuperar_lista_professores():
    try:
        with open("professores.json", "r") as arquivo:
            lista_professores = json.load(arquivo)
            return lista_professores
    except FileNotFoundError:
        return []

#incluir professor
def incluir_professor(lista_professores):
    codigo = int(input("Digite o código do professor: "))
    nome = input("Digite o nome do professor: ")
    cpf = input("Digite o CPF do professor: ")
    novo_professor = {"codigo": codigo, "nome": nome, "cpf": cpf}
    lista_professores.append(novo_professor)
    salvar_lista_professores(lista_professores)  #Opção de salvar
    print("Professor cadastrado com sucesso!")

#listar professor
def listar_professores(lista_professores):
    if lista_professores:
        for professor in lista_professores:
            print("Código:", professor["codigo"])
            print("Nome:", professor["nome"])
            print("CPF:", professor["cpf"])
            print()
    else:
        print("Não há professores cadastrados.")

#excluir professor
def excluir_professor(lista_professores):
    codigo_para_excluir = int(input("Digite o código do professor que deseja excluir: "))
    for professor in lista_professores:
        if professor["codigo"] == codigo_para_excluir:
            lista_professores.remove(professor)
            salvar_lista_professores(lista_professores)  #Opção de salvar
            print("Professor excluído com sucesso!")
            return
    print("Professor não encontrado.")

#editar professor
def editar_professor(lista_professores):
    codigo_para_editar = int(input("Digite o código do professor que deseja editar: "))
    for professor in lista_professores:
        if professor["codigo"] == codigo_para_editar:
            novo_codigo = int(input("Digite o novo código do professor: "))
            novo_nome = input("Digite o novo nome do professor: ")
            novo_cpf = input("Digite o novo CPF do professor: ")
            professor["codigo"] = novo_codigo
            professor["nome"] = novo_nome
            professor["cpf"] = novo_cpf
            salvar_lista_professores(lista_professores)  #Opção de salvar
            print("Professor editado com sucesso!")
            return
    print("Professor não encontrado.")

#salvar lista de disciplinas em um arquivo JSON
def salvar_lista_disciplinas(lista_disciplinas):
    with open("disciplinas.json", "w") as arquivo:
        json.dump(lista_disciplinas, arquivo)

#recuperar a lista de disciplinas de um arquivo JSON
def recuperar_lista_disciplinas():
    try:
        with open("disciplinas.json", "r") as arquivo:
            lista_disciplinas = json.load(arquivo)
            return lista_disciplinas
    except FileNotFoundError:
        return []

#incluir disciplina
def incluir_disciplina(lista_disciplinas):
    codigo = int(input("Digite o código da disciplina: "))
    nome = input("Digite o nome da disciplina: ")
    nova_disciplina = {"codigo": codigo, "nome": nome}
    lista_disciplinas.append(nova_disciplina)
    salvar_lista_disciplinas(lista_disciplinas)  #Opção de salvar
    print("Disciplina cadastrada com sucesso!")

#listar disciplina
def listar_disciplinas(lista_disciplinas):
    if lista_disciplinas:
        for disciplina in lista_disciplinas:
            print("Código:", disciplina["codigo"])
            print("Nome:", disciplina["nome"])
            print()
    else:
        print("Não há disciplinas cadastradas.")

#excluir disciplina
def excluir_disciplina(lista_disciplinas):
    codigo_para_excluir = int(input("Digite o código da disciplina que deseja excluir: "))
    for disciplina in lista_disciplinas:
        if disciplina["codigo"] == codigo_para_excluir:
            lista_disciplinas.remove(disciplina)
            salvar_lista_disciplinas(lista_disciplinas)  #Opção de salvar
            print("Disciplina excluída com sucesso!")
            return
    print("Disciplina não encontrada.")

#editar disciplina
def editar_disciplina(lista_disciplinas):
    codigo_para_editar = int(input("Digite o código da disciplina que deseja editar: "))
    for disciplina in lista_disciplinas:
        if disciplina["codigo"] == codigo_para_editar:
            novo_codigo = int(input("Digite o novo código da disciplina: "))
            novo_nome = input("Digite o novo nome da disciplina: ")
            disciplina["codigo"] = novo_codigo
            disciplina["nome"] = novo_nome
            salvar_lista_disciplinas(lista_disciplinas)  #Opção de salvar
            print("Disciplina editada com sucesso!")
            return
    print("Disciplina não encontrada.")

#salvar a lista de turmas em um arquivo JSON
def salvar_lista_turmas(lista_turmas):
    with open("turmas.json", "w") as arquivo:
        json.dump(lista_turmas, arquivo)

#recuperar a lista de turmas de um arquivo JSON
def recuperar_lista_turmas():
    try:
        with open("turmas.json", "r") as arquivo:
            lista_turmas = json.load(arquivo)
            return lista_turmas
    except FileNotFoundError:
        return []

#incluir turma
def incluir_turma(lista_turmas):
    codigo = int(input("Digite o código da turma: "))
    codigo_professor = int(input("Digite o código do professor: "))
    codigo_disciplina = int(input("Digite o código da disciplina: "))
    #Verificar se o código da turma já existe
    for turma in lista_turmas:
        if turma["codigo"] == codigo:
            print("Erro: Código da turma já existe.")
            return
    nova_turma = {"codigo": codigo, "codigo_professor": codigo_professor, "codigo_disciplina": codigo_disciplina}
    lista_turmas.append(nova_turma)
    salvar_lista_turmas(lista_turmas)  #Opção de salvar
    print("Turma cadastrada com sucesso!")

#listar turmas
def listar_turmas(lista_turmas):
    if lista_turmas:
        for turma in lista_turmas:
            print("Código:", turma["codigo"])
            print("Código do Professor:", turma["codigo_professor"])
            print("Código da Disciplina:", turma["codigo_disciplina"])
            print()
    else:
        print("Não há turmas cadastradas.")

#excluir turma
def excluir_turma(lista_turmas):
    codigo_para_excluir = int(input("Digite o código da turma que deseja excluir: "))
    for turma in lista_turmas:
        if turma["codigo"] == codigo_para_excluir:
            lista_turmas.remove(turma)
            salvar_lista_turmas(lista_turmas)  #Opção de salvar
            print("Turma excluída com sucesso!")
            return
    print("Turma não encontrada.")

#editar turma
def editar_turma(lista_turmas):
    codigo_para_editar = int(input("Digite o código da turma que deseja editar: "))
    for turma in lista_turmas:
        if turma["codigo"] == codigo_para_editar:
            novo_codigo = int(input("Digite o novo código da turma: "))
            novo_codigo_professor = int(input("Digite o novo código do professor: "))
            novo_codigo_disciplina = int(input("Digite o novo código da disciplina: "))
            turma["codigo"] = novo_codigo
            turma["codigo_professor"] = novo_codigo_professor
            turma["codigo_disciplina"] = novo_codigo_disciplina
            salvar_lista_turmas(lista_turmas)  #Opção de salvar
            print("Turma editada com sucesso!")
            return
    print("Turma não encontrada.")

#salvar a lista de matrículas em um arquivo JSON
def salvar_lista_matriculas(lista_matriculas):
    with open("matriculas.json", "w") as arquivo:
        json.dump(lista_matriculas, arquivo)

#recuperar a lista de matrículas de um arquivo JSON
def recuperar_lista_matriculas():
    try:
        with open("matriculas.json", "r") as arquivo:
            lista_matriculas = json.load(arquivo)
            return lista_matriculas
    except FileNotFoundError:
        return []

#incluir matrícula
def incluir_matricula(lista_matriculas):
    codigo_turma = int(input("Digite o código da turma: "))
    codigo_estudante = int(input("Digite o código do estudante: "))
    #verifica se a matrícula já existe
    for matricula in lista_matriculas:
        if matricula["codigo_turma"] == codigo_turma and matricula["codigo_estudante"] == codigo_estudante:
            print("Erro: Matrícula já existe.")
            return
    nova_matricula = {"codigo_turma": codigo_turma, "codigo_estudante": codigo_estudante}
    lista_matriculas.append(nova_matricula)
    salvar_lista_matriculas(lista_matriculas)  #Opção de salvar
    print("Matrícula cadastrada com sucesso!")

#listar matrículas
def listar_matriculas(lista_matriculas):
    if lista_matriculas:
        for matricula in lista_matriculas:
            print("Código da Turma:", matricula["codigo_turma"])
            print("Código do Estudante:", matricula["codigo_estudante"])
            print()
    else:
        print("Não há matrículas cadastradas.")

#excluir uma matrícula
def excluir_matricula(lista_matriculas):
    codigo_turma = int(input("Digite o código da turma: "))
    codigo_estudante = int(input("Digite o código do estudante: "))
    for matricula in lista_matriculas:
        if matricula["codigo_turma"] == codigo_turma and matricula["codigo_estudante"] == codigo_estudante:
            lista_matriculas.remove(matricula)
            salvar_lista_matriculas(lista_matriculas)  #Opção de salvar
            print("Matrícula excluída com sucesso!")
            return
    print("Matrícula não encontrada.")

#carregar listas usando arquivos JSON
lista_estudantes = recuperar_lista_estudantes()
lista_professores = recuperar_lista_professores()
lista_disciplinas = recuperar_lista_disciplinas()
lista_turmas = recuperar_lista_turmas()
lista_matriculas = recuperar_lista_matriculas()

# Apresentar definição
# Menu Principal
def apresentar_Menu_Principal():
    print("Menu Principal")
    print("1. Estudantes")
    print("2. Disciplinas")
    print("3. Professores")
    print("4. Turmas")
    print("5. Matrículas")
    print("6. Sair")

# Apresentar definição
# Menu Operações
def apresentar_Menu_Operacoes():
    print("Menu Operações. O que deseja fazer?")
    print("1. Incluir")
    print("2. Listar")
    print("3. Atualizar")
    print("4. Excluir")
    print("5. Retornar ao Menu Principal")

# Primeiro loop
apresentar_Menu_Principal()
while True:
    opcao = input("Digite uma opção válida: ")
    try:
        opcao = int(opcao)
        if 1 <= opcao <= 6:
            if opcao == 1:
                print("Você selecionou uma opção Válida: Estudantes")
                while True:
                    apresentar_Menu_Operacoes()
                    operacoes = input("Digite uma opção válida: ")
                    try:
                        operacoes = int(operacoes)
                        if 1 <= operacoes <= 5:
                            if operacoes == 1:
                                incluir_estudante(lista_estudantes)
                            elif operacoes == 2:
                                listar_estudantes(lista_estudantes)
                            elif operacoes == 3:
                                editar_estudante(lista_estudantes)
                            elif operacoes == 4:
                                excluir_estudante(lista_estudantes)
                            elif operacoes == 5:
                                print("Retornando ao menu principal")
                                break #Retorna ao menu principal
                        else:
                            raise ValueError
                    except ValueError:
                        print("Opção INVÁLIDA! Digite uma opção válida")
            elif opcao == 2:
                print("Você selecionou uma opção Válida: Disciplinas")
                while True:
                    apresentar_Menu_Operacoes()
                    operacoes = input("Digite uma opção válida: ")
                    try:
                        operacoes = int(operacoes)
                        if 1 <= operacoes <= 5:
                            if operacoes == 1:
                                incluir_disciplina(lista_disciplinas)
                            elif operacoes == 2:
                                listar_disciplinas(lista_disciplinas)
                            elif operacoes == 3:
                                editar_disciplina(lista_disciplinas)
                            elif operacoes == 4:
                                excluir_disciplina(lista_disciplinas)
                            elif operacoes == 5:
                                print("Retornando ao menu principal")
                                break #Retorna ao menu principal
                        else:
                            raise ValueError
                    except ValueError:
                        print("Opção INVÁLIDA! Digite uma opção válida")
            elif opcao == 3:
                print("Você selecionou uma opção Válida: Professores")
                while True:
                    apresentar_Menu_Operacoes()
                    operacoes = input("Digite uma opção válida: ")
                    try:
                        operacoes = int(operacoes)
                        if 1 <= operacoes <= 5:
                            if operacoes == 1:
                                incluir_professor(lista_professores)
                            elif operacoes == 2:
                                listar_professores(lista_professores)
                            elif operacoes == 3:
                                editar_professor(lista_professores)
                            elif operacoes == 4:
                                excluir_professor(lista_professores)
                            elif operacoes == 5:
                                print("Retornando ao menu principal")
                                break #Retorna ao menu principal
                        else:
                            raise ValueError
                    except ValueError:
                        print("Opção INVÁLIDA! Digite uma opção válida")
            elif opcao == 4:
                print("Você selecionou uma opção Válida: Turmas")
                while True:
                    apresentar_Menu_Operacoes()
                    operacoes = input("Digite uma opção válida: ")
                    try:
                        operacoes = int(operacoes)
                        if 1 <= operacoes <= 5:
                            if operacoes == 1:
                                incluir_turma(lista_turmas)
                            elif operacoes == 2:
                                listar_turmas(lista_turmas)
                            elif operacoes == 3:
                                editar_turma(lista_turmas)
                            elif operacoes == 4:
                                excluir_turma(lista_turmas)
                            elif operacoes == 5:
                                print("Retornando ao menu principal")
                                break #Retorna ao menu principal
                        else:
                            raise ValueError
                    except ValueError:
                        print("Opção INVÁLIDA! Digite uma opção válida")
            elif opcao == 5:
                print("Você selecionou uma opção Válida: Matrículas")
                while True:
                    apresentar_Menu_Operacoes()
                    operacoes = input("Digite uma opção válida: ")
                    try:
                        operacoes = int(operacoes)
                        if 1 <= operacoes <= 5:
                            if operacoes == 1:
                                incluir_matricula(lista_matriculas)
                            elif operacoes == 2:
                                listar_matriculas(lista_matriculas)
                            elif operacoes == 3:
                                print("Operação inválida para matrículas.")
                            elif operacoes == 4:
                                excluir_matricula(lista_matriculas)
                            elif operacoes == 5:
                                print("Retornando ao menu principal")
                                break #Retorna ao menu principal
                        else:
                            raise ValueError
                    except ValueError:
                        print("Opção INVÁLIDA! Digite uma opção válida")
            elif opcao == 6:
                print("Encerrando o programa...")
                break #Encerra o programa
        else:
            raise ValueError
    except ValueError:
        print("Opção INVÁLIDA! Digite uma opção válida")
