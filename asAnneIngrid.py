def abreArquivo(nomeDoArquivo):
    arquivo=open(nomeDoArquivo,'+r')
    conteudo=arquivo.read().splitlines()
    arquivo.close()
    alunos=[]
    for linha in conteudo:
        if ';' in linha:
            alunos.append(linha.split(';'))
    return alunos
   
def maiorNota(nomeDoArquivo):
    lista=abreArquivo(nomeDoArquivo)
    maiorNota=0
    alunoMaiorNota=''
    notasBoas=[]
    maiorNotadoAluno=[]
    for item in lista:
        maiorNotadoAluno.append(item[0])
        if float(item[1])>float(item[2]):
            maiorNotadoAluno.append(item[1])
        else:
            maiorNotadoAluno.append(item[2])
        notasBoas.append(maiorNotadoAluno)
        maiorNotadoAluno=[]
    for item in notasBoas:
        if float(item[1])>maiorNota:
            maiorNota=float(item[1])
            alunoMaiorNota=item[0]
    return alunoMaiorNota

def maiorMedia(nomeDoArquivo):
    lista=abreArquivo(nomeDoArquivo)
    maiorMedia=0
    alunoMaiorMedia=''
    for aluno in lista:
        if float(aluno[3]) >maiorMedia:
            maiorMedia=float(aluno[3])
            alunoMaiorMedia=aluno[0]
    return alunoMaiorMedia

def procuraNota(nomeDoArquivo,aluno):
    lista=abreArquivo(nomeDoArquivo)
    for item in lista:
        if aluno in item:
            return item[1:]
        
    
def insereAlunoArquivo(nomeDoArquivo, nome, nota1, nota2):
    arquivo=open(nomeDoArquivo,'a')
    arquivo.write(str('\n'+nome +';'+ str(nota1) +';'+ str(nota2)))
    media=(nota1+nota2)/2
    arquivo.write(';'+str(media))
    arquivo.close()


opcao = 0
while opcao!=5:
    if opcao == 1:
       print("A maior nota é do aluno ", maiorNota('notas_alunos.csv'))
    elif opcao == 2:
        print("A maior média é do aluno ", maiorMedia('notas_alunos.csv'))
    elif opcao == 3:
        aluno=input("Que aluno você deseja ver as notas? ")
        print("As notas do aluno ", aluno, procuraNota('notas_alunos.csv',aluno))
    elif opcao == 4:
        nome=input("Nome do aluno: ")
        nota1=float(input("Nota G1: "))
        nota2=float(input("Nota G2: "))
        insereAlunoArquivo('notas_alunos.csv', nome, nota1, nota2)
        print("Aluno ",nome,"foi foi inserido com sucesso!")
    opcao = int(input("\n Escolha a opção desejada:"\
              "\n1. Encontrar a maior nota."\
              "\n2. Maior média"\
              "\n3. Pesquisar notas"\
              "\n4. Inserir Notas de aluno"\
              "\n5. Sair\n"))