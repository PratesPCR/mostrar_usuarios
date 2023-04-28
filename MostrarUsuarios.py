#!/usr/bin/env pynthon3

import pwd

#lista todos os usuarios do Linux

for usuarios in pwd.getpwall():
    print(usuarios.pw_name)
    