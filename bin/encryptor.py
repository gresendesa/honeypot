"""
Este método de encriptação gera uma string inteligível s1 em outra string qualquer s2, de preferência inteligível (veja as regras) com base em uma outra string chave.
"""
"""
Defina-se como S o conjunto todas as sequências cujos caracteres fazem parte de uma sequência C.
Sejam s1 e s2 dois elementos do conjunto S que possuem comprimentos l1 e l2, respectivamente, tal que l1<=l2.
"""

"""
Definição I: Sejam a e b elementos de uma sequência C de comprimento l e N(a) e N(b) a posição dos caracteres na sequência C, respectivamente. 
A distância d entre a e b é dado por :
IA.   d =   N(b) - N(a)     se N(a) <= N(b)
IB.   d =   l - N(a) + N(b)   se N(a) > N(b)
"""

"""
Para reverter uma posição, como consequência da definição 1
IIA.  N(a) = N(b) - d     se d <= N(b)
IIB.  N(a) = l + N(b) - d   se d > N(b)

# Seja K uma sequência de números kn, tal que kn é a distância entre o caractere n de S1 e o caratere n de S2 na sequência C. 

#Nota: S1 deve preferencialmente possuir comprimento par para uma melhor qualidade encriptação (caractere central problemático) 

"""

import string

class Honey:

  def __init__(self, C=[c for c in string.printable]):

    self.C = lambda p: chr(p)
    self.l = 65536 #2^16
    self.N = lambda c: ord(c)

  def transform(self, s1, s2):
    try:
      S1 = [a for a in s1]
      S2 = [b for b in s2]
      l1 = len(S1)
      l2 = len(S2)
      d = lambda a, b: self.N(b) - self.N(a) if self.N(a) <= self.N(b) else self.l - self.N(a) + self.N(b)

      if l1 <= l2:
        K = [d(a, S2[n]) for n, a in enumerate(S1)]
      else:
        print('S2 needs to be longer than S1')
        exit()
      return ''.join([chr(k) for k in K])
    except Exception as e:
      raise Exception(f'Unable to transform: {e}')

  def reconstruct(self, s2, key): #reconstrói S1 com base na sequência K e em s1

    K = [ord(k) for k in key]

    try:
      S2 = [b for b in s2]
      Na =  lambda b, d: self.l + self.N(b) - d if d > self.N(b) else self.N(b) - d 
      for n, d in enumerate(K):
        S1 = [self.C(Na(S2[n], d)) for n, d in enumerate(K)]
      return ''.join(S1)
    except Exception as e:
      raise Exception(f'Unable to reconstruct: {e}')




