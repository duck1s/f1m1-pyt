Last login: Mon Sep 13 12:31:37 on ttys000
joeribreedveld@Joeris-MacBook-Pro ~ % python3
Python 3.9.7 (v3.9.7:1016ef3790, Aug 30 2021, 16:39:15) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> 2 + 2
4
>>> 3 * 10
30
>>> 100 - 10
90
>>> 25 / 5
5.0
>>> 10 / 3
3.3333333333333335
>>> 10 // 3
3
>>> print('Mijn naam is Joeri')
Mijn naam is Joeri
>>> naam = 'Joeri'
>>> print(naam)
Joeri
>>> print(naam.upper())
JOERI
>>> print(naam[0:2])
Jo
>>> print(naam[::-1])
ireoJ
>>> leeftijd = 16
>>> print('Hallo ' + naam + ' ben je al ' + str(leeftijd) + ' jaar?')
Hallo Joeri ben je al 16 jaar?
>>> leeftijd = leeftijd + 1
>>> leeftijd
17
>>> leeftijd-=1
>>> leeftijd
16
>>> if leeftijd < 18:
...     hoelang_tot18jaar = 18 - leeftijd
...     print('Over ' + str(hoelang_tot18jaar) + ' jaar wordt je 18')
... elif leeftijd > 18:
...     hoelang_al18jaar = leeftijd - 18
...     print('Het is alweer ' + str(hoelang_al18jaar) + ' jaar geleden dat je 18 werd ;-)')
... else:
...     print('Je bent precies ' + str(leeftijd) + ' jaar')
... 
Over 2 jaar wordt je 18
>>> from random import randint
>>> randint(0,1000)
449
>>> willekeurig_getal = randint(0,1000)
>>> willekeurig_getal
360
>>> print('Willekeurig getal tussen 0 en 1000: ' +str(willekeurig_getal))
Willekeurig getal tussen 0 en 1000: 360
>>> from datetime import datetime
>>> datum = datetime.now()
>>> print(datum)
2021-09-13 12:38:04.967242
>>> datum.strftime('%A %d %B %Y')
'Monday 13 September 2021'
>>> import locale
>>> locale.setlocale(locale.LC_TIME, 'nl_NL')
'nl_NL'
>>> datum.strftime('%A %d %B %Y')
'maandag 13 september 2021'
>>> locale.setlocale(locale.LC_TIME, 'it_IT')
'it_IT'
>>> datum.strftime('%A %d %B %Y')
'Lunedì 13 Settembre 2021'
>>> 
