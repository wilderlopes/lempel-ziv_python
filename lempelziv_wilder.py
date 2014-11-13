# -*- coding: cp1252 -*-
#The MIT License (MIT)
#
#Copyright (c) 2014 Wilder Lopes
#
#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the #Software is
#furnished to do so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

# Universidade de São Paulo - Escola Politécnica
# PTC 5600 - Tópicos sobre Teoria da Informação
# 3º trimestre - 2012 - Prof. Cristiano Panazio
# Lista 4 - Implementação do algoritmo Lempel-Ziv
# Estudante: Wilder Bezerra Lopes - 7282551

from __future__ import division
from scipy import log2
    
def compare(inp,d):
    flag = 0
    pointer = ''
    for j in range(len(d)):
        if inp == d[j]:
            flag = 1
            pointer = str(j)
    return str(flag)+pointer


def parsing(inpstr):

    dic = [''] #empty substring
    prefix = ''
    pointer_bit_dec = ['']
    pfx = 0
    
    for i in range(len(inpstr)):
        
        sin = prefix + inpstr[i]
        prefix = ''
        
        result = compare(sin,dic) #Comparing with the dictionary
                
        if result == '0':
            dic.append(sin)
            pointer_bit_dec.append(str(bin(pfx))+sin[-1]) #format: (pointer, extra bit)
        else:
            pfx = int(result[-1]) #Position in dictionary
            prefix = sin            
            
            if i == len(inpstr)-1:
                sufix = ''
                dic.append(sin+sufix)
                pointer_bit_dec.append(str(bin(pfx))+'') #format: (pointer, extra bit)
                
    #print 'substrings = %s' % (dic)
            
    return pointer_bit_dec


def encoding(pointerbit, indexbit):
    out_enc = []
    
    for i in range(len(pointerbit)):
        a = pointerbit[i]
        a = a[2:]
       
        if len(a) < indexbit + 1:
            b = a.zfill(indexbit + 1)
            #print 'a = %s, zfill = %d, b=%s' % (a,indexbit + 1 - len(a),b)
        else:
            b = a
        
        out_enc.append(b)

    return out_enc


def main():

    print '# Universidade de Sao Paulo - Escola Politecnica'
    print '# PTC 5600 - Topicos sobre Teoria da Informacao'
    print '# 3o. trimestre - 2012 - Prof. Cristiano Panazio'
    print '# Lista 4 - Implementacao do algoritmo Lempel-Ziv'
    print '# Estudante: Wilder Bezerra Lopes - 7282551 \n'    
    
    print 'Aponte o caminho ou nome do arquivo (.txt) a ser compactado:'
    user_input = raw_input('--> ')
    input_file = open(user_input,'r')
    s = input_file.read()     
       
    pointer_bit= parsing(s)   
    numseg = len(pointer_bit)
    index_bits = int(round(log2(numseg)))    
    outstr = ''
    sout = encoding(pointer_bit, index_bits)   
    outstr = outstr.join(sout)
    outstr = outstr[index_bits+1:]

    num_1 = 0
    num_0 = 0

    
    for i in range(len(outstr)):
        if outstr[i] == '1':
            num_1 = num_1 + 1
        if outstr[i] == '0':
            num_0 = num_0 + 1

    freq_1 = (num_1/len(outstr))
    freq_0 = (num_0/len(outstr))
    entropy = -((freq_1*log2(freq_1)) + (freq_0*log2(freq_0))) ## a partir das frequencias
    
##    print 'sout = %s' % (sout)
##    print 'encoded string = %s' % (outstr)
    print '\n'
    print '=== LOG do algoritmo ===\n'
    print 'Numero de palavras no dicionario   = %d' % (len(pointer_bit)) 
    print 'Comprimento da seq de entrada      = %d bits' % (len(s)) 
    print 'Comprimento da seq de saida        = %d bits' % (len(outstr))
    print 'Quantidade de bits "1"             = %d' % (num_1)
    print 'Quantidade de bits "0"             = %d' % (num_0)
    print 'Frequencia de bits "1"             = %1.4f' % freq_1
    print 'Frequencia de bits "0"             = %1.4f' % freq_0
    print 'Entropia a partir das frequencias  = %1.4f bits\n' % entropy


    output_file = open('lz_seq_encoded.txt','w')  
    output_file.write(outstr)
    print 'Arquivo comprimido --> lz_seq_encoded.txt'
    raw_input("Pressione qualquer tecla para sair")
   
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
