from App import App
app = App()
while(app.app):
    app.limpar()
    app.menu()
    escolha = input()
    if escolha == "1" or escolha == "ver notas" or escolha == "ver":
        app.verNotas()
    elif escolha == "2" or escolha == "adicionar nota" or escolha == "adicionar":
        app.adicionarNota()
    elif escolha == "3" or escolha == "editar nota" or escolha == "editar":
        app.editarNota()
    elif escolha == "4" or escolha == "deletar aluno" or escolha == "deletar":
        app.deletarAluno()
    elif escolha == "5" or escolha == "sair":
        app.app = False