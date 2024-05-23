import os

curr_path = os.getcwd()
ignore = ['pack.py', 'unpack.py']

# Conteúdo inicial da pasta, apenas diretórios por extensão e os arquivos ignore
old_content = os.listdir(curr_path)



# Reorganizando arquivos, reunindo novamente em uma só pasta
for dir in old_content:
    # Caminho da pasta de extensão atual
    old_path = os.path.join(curr_path, dir)
    # Se for um diretório, move os arquivos para a pasta fora dele
    valid_dir = os.path.isdir(old_path)
    if valid_dir:
        curr_content = os.listdir(old_path)
        for file in curr_content:
            os.rename(
                os.path.join(old_path, file), 
                os.path.join(curr_path, file)
            )
print('Arquivos desempacotados')



# Conteúdo da pasta com pastas por extensão vazias e todos os arquivos
new_content = os.listdir(curr_path)
for file in ignore:
    if file in new_content: new_content.remove(file)

# Criando lista com nomes equivalentes às extensões
ext_list = set()
for file in new_content:
    valid_file = os.path.isfile(os.path.join(curr_path, file))
    if valid_file:
        ext = file.split('.')[-1]
        ext_list.add(ext)
ext_list = list(ext_list)



# Remove pastas com os nomes da lista de extensões
for dir in new_content:
    # Se for uma pasta e seu nome estiver na lista de extensões
    valid_dir = (os.path.isdir(os.path.join(curr_path, dir))) and (dir in ext_list)
    if valid_dir: 
        os.rmdir(dir)
print('Pastas excluídas')
