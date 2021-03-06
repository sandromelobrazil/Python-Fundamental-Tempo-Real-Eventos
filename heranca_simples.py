# coding: utf-8

"""
Criando herança simples em Python.
"""

class Book(object):
	
	def __init__(self, author, title, year):
		self.author = author
		self.title = title
		self.year = year
		

class BookPDF(Book):
	
	def __init__(self, author, title, year, len_MB):
#		Book.__init__(self, author, title, year)
		super(BookPDF, self).__init__(author, title, year)
		self.len_MB = len_MB
	
	def list_all(self):
		print 'Author: %s' % self.author
		print 'Title: %s' % self.title
		print 'Year: %s' % self.year
		print 'Length MB: %s' % self.len_MB
		
		
book = BookPDF('Guilherme Carvalho', 'Python Fundamental', 2014, 1.0)
book.list_all()
