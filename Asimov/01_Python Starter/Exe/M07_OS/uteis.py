import os

def get_ext(path, ignore):
    # Coletar nomes dos arquivos/pastas
    content = os.listdir(path)
 
    # Itens que sejam pastas e não estejam em Ignore
    ext_list = set()
    for file in content:
        # Se for um arquivo e não estiver contido no conjunto ignore, adiciona na lista de extensões
        valid_file = os.path.isfile(os.path.join(path, file))
        if valid_file: 
            ext = file.split('.')[-1]
            ext_list.add(ext)
    return list(ext_list)

def create_dirs(path,  ext_list):
    # Criar pastas com os nomes da lista
    for ext in ext_list:
        if not (ext in os.listdir(path)): os.mkdir(os.path.join(path, ext))
    print('Pastas criadas')


def into(path, ignore):
    # Nomes de cada item na pasta atual
    content = os.listdir(path)
    for file in content:
        # Se for um arquivo e não estiver nos arquivos a ignorar, move para a nova pasta
        valid_file = os.path.isfile(os.path.join(path, file)) and not (file in ignore)
        if valid_file:
            new_path = os.path.join(path, file.split('.')[-1], file)
            os.rename(path, new_path)
    print('Arquivos empacotados')
        

def outof(path):
    # Nomes de cada pasta no path atual
    content = os.listdir(path)

    for dir in content:
        # Caminho da pasta de extensão atual
        curr_dir_path = os.path.join(path, dir)
        # Se for um diretório, move os arquivos para a pasta fora dele
        valid_dir = os.path.isdir(curr_dir_path)
        if valid_dir:
            curr_content = os.listdir(curr_dir_path)
            for file in curr_content:
                os.rename(
                    os.path.join(curr_dir_path, file), 
                    os.path.join(path, file)
                )
    print('Arquivos desempacotados')


def clear_dirs(path, ignore):
    # Nomes de cada item nesse path
    content = os.listdir(path)

    ext_list = get_ext(path, ignore)

    for dir in content:
    # Se for uma pasta e seu nome estiver na lista de extensões, apaga a pasta
        valid_dir = (os.path.isdir(os.path.join(path, dir))) and (dir in ext_list)
        if valid_dir: os.rmdir(dir)
    print('Pastas apagadas')
