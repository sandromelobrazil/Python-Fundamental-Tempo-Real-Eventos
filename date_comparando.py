# coding: utf-8

"""
Importando o módulo datetime para trabalhar com datas em Python.
Esse módulo prove várias funcionalidades interessantes para
facilitar o trabalho do programador na manipulação de datas.
Ele já está incluso nas baterias do Python.
"""
from datetime import datetime

# calculando diferença de dias entre duas datas
hoje = datetime.now().date()
prox_aniv = datetime(hoje.year+1, 3, 21, 12, 0, 0, 0)

print 'Hoje: %s' % hoje.strftime('%d-%m-%Y')
print u'Próximo aniversário: %s' % prox_aniv.strftime('%d-%m-%Y')
print u'Faltam %s dias' % (prox_aniv.date() - hoje).days

# calculando diferença entre horas em python
hoje = datetime.now()
print u'Faltam %.0f segundos' % (prox_aniv - hoje).total_seconds()
print u'Faltam %.0f minutos' % ((prox_aniv - hoje).total_seconds() // 60)
print u'Faltam %.0f horas' % ((prox_aniv - hoje).total_seconds() // 60 // 60)
