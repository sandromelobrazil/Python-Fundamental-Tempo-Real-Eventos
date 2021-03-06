# coding: utf-8

"""
Importando o módulo datetime para trabalhar com datas em Python.
Esse módulo prove várias funcionalidades interessantes para
facilitar o trabalho do programador na manipulação de datas.
Ele já está incluso nas baterias do Python.
"""
from datetime import datetime

# retorna a data e hora
data_completa = datetime.now()
print '\ndata completa => %s' % data_completa

# obtendo apenas a data
data_sem_horas = datetime.now().date()
print 'data sem as horas => %s' % data_sem_horas

# imprimindo qual dia da semana é
days_of_week = {
	0: u'Domingo',
	1: u'Segunda-Feira',
	2: u'Terça-Feira',
	3: u'Quarta-Feira',
	4: u'Quinta-Feira',
	5: u'Sexta-Feira',
	6: u'Sábado',
}
number_of_day = datetime.now().isoweekday() # dom = 0 ... sáb = 6
print 'Today is %s' % days_of_week[number_of_day]

# formatando a saída da data
print u'Data sem formatação: %s' % datetime.now()
print u'Data formatada: %s' % datetime.now().strftime('%A %d de %b de %Y')



