Python 3.6.5 (v3.6.5:f59c0932b4, Mar 28 2018, 16:07:46) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 2==3
False
>>> hate==hate
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    hate==hate
NameError: name 'hate' is not defined
>>> 'hate'=='hate'
True
>>> 9==6
False
>>> 9==nine
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    9==nine
NameError: name 'nine' is not defined
>>> nine=nine
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    nine=nine
NameError: name 'nine' is not defined
>>> n=7
>>> if  7>3:
	print('Collo has a fat head')

	
Collo has a fat head
>>> n=8
>>> print ('n + 8')
n + 8
>>> print('9+9')
9+9
>>> eligibility=input('What is your age?') >=int('18')
What is your age?18
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    eligibility=input('What is your age?') >=int('18')
TypeError: '>=' not supported between instances of 'str' and 'int'
>>> eligibility=int(input('What is your age?')) >=int('18')
What is your age?18
>>> eligibility=input(int('What is your age?')) >=int('18')
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    eligibility=input(int('What is your age?')) >=int('18')
ValueError: invalid literal for int() with base 10: 'What is your age?'
>>> eligibility=input('What is your age?') >='18'
What is your age?18
>>> print eligibility
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(eligibility)?
>>> print (eligibility)
True
>>> if eligibilty >=18
SyntaxError: invalid syntax
>>> 
>>> if eligibilty>=18
SyntaxError: invalid syntax
>>> if 7>5
SyntaxError: invalid syntax
>>> if 7>5
SyntaxError: invalid syntax
>>> 7.5
7.5
>>> if eligibility>='18':
	print (eligibility)

	
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    if eligibility>='18':
TypeError: '>=' not supported between instances of 'bool' and 'str'
>>> if  input('What is your age?') >='18' :
	print(eligibility)

	
What is your age?18
True
>>> i = 7
while i <=7:
  print (i)
  i = i +2

  print ('finished)







