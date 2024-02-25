import os
#cria um diretório recursivamente
#exist_ok= true não retorna erro se o diretório existir 
#path.join é o caminho relativo para nosso diretório atual

def CriarDiretorio(NomeDiretorio,Caminho, Archive):
    Directory = NomeDiretorio

    Parent_Dir = Caminho


    os.makedirs(os.path.join(Parent_Dir, Directory), exist_ok=True)

    data_file = os.path.join(Parent_Dir, Directory, 'house_tiny.csv')

    with open(data_file, 'w') as f:
        f.write(Archive)
        


        
    