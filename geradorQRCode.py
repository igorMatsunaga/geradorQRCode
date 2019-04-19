#!/usr/bin/env python
# -*- coding: utf-8 -*-

#importar QRCode 
import pyqrcode
from pyqrcode import QRCode

#String que será representada pelo QRCode
s = raw_input("Digite a url a ser transformada: ")
#Nome parao arquivo de saida 
n = raw_input("Digite o nome de saida: ")

#Gerar o QRCode
url = pyqrcode.create(s)
#Criar e salvar o arquivo com o nome inserido
url.svg( n +".svg", scale = 8)
