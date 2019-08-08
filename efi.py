#!/usr/bin/python3

import os
import sys
from time import sleep


de = {'s':'spotify','n':'netflix','a':'amazon','v':'vpn','o':'other'}

#Errores
#
#Informacion
u_e = '[?] Error inesperado.'
c_o = '[?] Es obligatorio rellenar este campo'
p_l = '[?] Payload: '
#Advertencia
t_1,t_2 = '[!] Tamaño del ',' incorrecto. Corrija.'
f_i     = '[!] Formato incorrecto.'
#Proceso
e_s = '[+] Guardando datos en'
c_p = '[+] Cerrando programa...'
#Complido
g_e = '[*] Guardado con exito.'

def guardar(tipo,bin,fecha,cvv,comentario,combo,cc):
    r = open(tipo+'.txt','a')
    if comentario == None:
        ask_comm = input('Quieres agregar un comentario? (y/n): ')
        if ask_comm in ('n','N'):
            comm = False
        elif ask_comm in ('y','Y'):
            comm = True
        else:
            print(u_e)
    if comm == True:
        comm = input('Escriba su comentario a continuacion:\n')
        r.write(bin+' '+fecha+' '+cvv+' \''+comm+'\'')
    if comm == False:
        r.write(bin+' '+fecha+' '+cvv+' None')
    #combo
    if combo == None:
        comb = input('Quieres agregar combo(s)? (y/n): ')
        if comb in ('y','Y'):
            combo = True
        elif comb in ('n','N'):
            combo = False
        else:
            print(u_e)
    if combo == str():
        combo = False
    if combo:
        comb = input('Ingresa el/los combo(s) a continuacion:\n')
        r.write(' '+comb)
    if cc == None:
        cce = input('Quieres agregar cc utilizada? (y/n): ')
        if cce in ('y','Y'):
           cc = True
        elif cc in ('n','N'):
           cc = True
        else:
           print(u_e)
    if cc == str():
        cc = False
    if cc:
        cce = input('Ingresa la CC a continuacion:\n')
        r.write(' '+cce)
    print('\n'+e_s+' \''+tipo+'.txt\'...'),print(c_p),print(g_e)
    r.write('\n')
    r.close()

def bin(cuenta):
    def cvv_c(cvv):
        if len(cvv) == 4 or (len(cvv) == 3):
            return guardar(cuenta,bin,date,cvv,None,None,None)
        elif len(cvv) != (4 or 3):
            if cvv == 'rnd':
                return guardar(cuenta,bin,date,cvv,None,None,None)
            elif cvv != 'rnd':
                print(t_1+'cvv'+t_2)
        elif len(cvv) == 0:
            print(c_o)
            sleep(1)
            os.system('clear')
    bin = input('BIN : ')
    date = input('Date: ')
    cvv = input('Cvv : ')
    bin = bin.replace(' ',str())
    if len(bin) == 16:
        if 'x' not in bin:
            print('[?] Lo que usted escribio no es un bin. Corrija.')
            sleep(1)
            os.system('clear')
        elif date == 'rnd':
            cvv_c(cvv)
        elif len(date) != 0 and (len(date.split('/')) == 2):
            cvv_c(cvv)
        elif len(date) != 0 and (len(date.split('/')) != 2):
            print(f_i+'mes/año.')
        elif len(date) > 7:
            print(t_1+'fecha'+t_2)
        elif len(date) == 0:
            print(c_o)
            sleep(1)
            os.system('clear')
        else:
            print(u_e)
    elif len(bin) != 16:
        print(t_1+'bin'+t_2)
    elif len(bin) == 0:
        print(c_o)
        sleep(1)
        os.system('clear')
    else:
        print(u_e)

#sys
if len(sys.argv) != 2:
    print(t_1+'argumento'+t_2)
    print('Escribe: \''+sys.argv[0]+' -h\' for help.')
elif len(sys.argv) == 2 and (sys.argv[1] in ('-h','s','n','a','v','o')):
    if sys.argv[1] == '-h':
        print('''Eficiente. Programa para bineo y cardeo.

Commandos permitidos:
   -h : Encontrar ayuda

Cuentas permitidas:
   s  : Spotify
   n  : Netflix
   a  : Amazon
   v  : Vpn
   o  : Other\n''')
    elif sys.argv[1] != '-h':
        try:
            bin(de[sys.argv[1]])
        except KeyboardInterrupt:
            print('\n\n[!] Detuviste el programa.\n'+c_p)
            sleep(1.5)
            os.system('clear')
else:
    print(u_e)

