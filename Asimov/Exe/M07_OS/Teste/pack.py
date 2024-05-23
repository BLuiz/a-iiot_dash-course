import os

curr_path = os.getcwd()
ignore = ['pack.py', 'unpack.py']

# Conteúdo inicial da pasta, todos os arquivos
content = os.listdir(curr_path)
for file in ignore:
    if file in content: content.remove(file)



# Criando lista com nomes equivalentes às extensões
ext_list = set()
for file in content:
    valid_file = os.path.isfile(os.path.join(curr_path, file))
    if valid_file: 
        ext = file.split('.')[-1]
        ext_list.add(ext)
ext_list = list(ext_list)



# Criar pastas com os nomes da lista de extensões
for ext in ext_list:
    if not (ext in os.listdir(curr_path)): os.mkdir(os.path.join(curr_path, ext))
print('Pastas criadas')



# Organizando arquivos nas respectivas pastas, por extensão
for ext in ext_list:
    # Caminho destino para arquivos desse extensão
    new_path = os.path.join(curr_path, ext)
    # Nomes de cada item na pasta atual
    content = os.listdir(curr_path)
    for file in content:
        # Se for um arquivo e não estiver nos arquivos a ignorar, move para a nova pasta
        valid_file = os.path.isfile(os.path.join(curr_path, file)) and not (file in ignore)
        if valid_file and file.split('.')[-1] == ext:
            os.rename(
                file,
                os.path.join(new_path, file)
            )
print('Arquivos empacotados')
