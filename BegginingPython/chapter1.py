Python 3.4.3 (default, Oct 14 2015, 20:33:09) 
[GCC 4.8.4] on linux
Type "copyright", "credits" or "license()" for more information.
>>> names = ["Allex","Jack"]
>>> isinstance(names,list)
True
>>> isinstance(names,number)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    isinstance(names,number)
NameError: name 'number' is not defined
>>> movies = ["Action",2014,[["San Andreas","V. Kilmer"],["The Space","W.Smith"]],"Sci-fi",2014[["The Ten Theory","J. Stray"],["Losing Gravitus","B.Mimi"]]]
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    movies = ["Action",2014,[["San Andreas","V. Kilmer"],["The Space","W.Smith"]],"Sci-fi",2014[["The Ten Theory","J. Stray"],["Losing Gravitus","B.Mimi"]]]
TypeError: 'int' object is not subscriptable
>>> movies = ["The Call",[2014,"B. Dedes"],"Losing Touch",[2015,"T. Thedaes"]]
>>> for m in movies:
	print(m)

	
The Call
[2014, 'B. Dedes']
Losing Touch
[2015, 'T. Thedaes']
>>> for m in movies:
	if isinstance(m,list):
		for item in m:
			print(item)

			
2014
B. Dedes
2015
T. Thedaes
>>> for m in movies:
	print(m[0])

	
T
2014
L
2015
>>> for m in movies:
	print(m)

	
The Call
[2014, 'B. Dedes']
Losing Touch
[2015, 'T. Thedaes']
>>> 
