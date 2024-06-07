"""Projeto de organização de arquivos"""
import os
from M07_OS.uteis import *
from time import sleep

# curr_path = os.getcwd()
curr_path = 'C:\\Users\\Administrativo\\Desktop\\DashTraining\\Asimov\\Exe\\M07_OS\\Teste'
ignore = ['pack.py', 'unpack.py']
ext_names = get_ext(curr_path, ignore)

# Garantir estar na pasta correta
os.chdir(curr_path)


def pack():
    """
    Função para organizar os arquivos de uma pasta em outras pastas, separando-os pelas extensões
    """
    create_dirs(curr_path, ext_names)
    into(curr_path, ignore)
    sleep(2)


def unpack():
    """
    Função para reorganizar os arquivos de uma pasta, captando todos os arquivos em pastas menores e juntar em apenas uma pasta externa
    """
    outof(curr_path)
    clear_dirs(curr_path, ignore)
    sleep(2)
