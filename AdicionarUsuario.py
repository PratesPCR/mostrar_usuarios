#!/usr/bin/env python3
import subprocess

#definindo uma váriavel para usuário e senha
novo_usuario = "Prates"
nova_senha = "paswd123"

#cria o usuário e senha no sistema Linux
subprocess.run(["sudo", "useradd", novo_usuario])
subprocess.run(["sudo", "passwd", novo_usuario],input=f"{nova_senha}\n{nova_senha}\n".encode())

import pwd

#lista todos os usuarios do Linux

for usuarios in pwd.getpwall():
    print(usuarios.pw_name)
    
