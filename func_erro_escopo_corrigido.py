# coding:utf-8

salario = 500

def bonus_salario():
    global salario
    salario += 500
    print u'O bônus foi aplicado'

print u'valor antes da bonificação => R$ %s' % salario
bonus_salario()
print u'valor após da bonificação => R$ %s' % salario
