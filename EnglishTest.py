# -*- coding: utf-8 -*-
import random
import sys
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
print "~~~            Тест английского                 ~~~"
print "~~~           Copyleft iHal 2016                ~~~"
print "~~~         Для выхода введите \'!\'              ~~~"
print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
engWords = dict()
engWords = {"one":"один", "two":"два", "gloves":"перчатки" , "понедельник":"monday" \
,"walk":"гулять" ,"sky":"небо" ,"draw":"рисовать" ,"sharpener":"точилка"\
,"pen":"ручка" ,"mirror":"зеркало", "ball":"мяч" ,"word":"слово" , "dog":"собака"\
, "яблоко":"apple" ,"purple":"фиолетовый" ,"hat":"шляпа" ,"favourite":"любимый" ,\
"textbook":"учебник" ,"shop":"магазин" ,"umbrella":"зонт" ,"cow":"корова" ,\
"duck":"утка" ,"goldfish":"золотая рыбка" ,"be ill":"болеть" ,"know":"знать"\
 ,"call":"называть" ,"pet":"питомец" ,"rabbit":"кролик" ,"repair":"ремонтировать" }
leanWords = dict()
intQRight=0
intQWrong=0
intRight=0
wordPosition=1
intMaxWords=len(engWords)
intMinWords=1
myWord=""
exitWord="!"
print ("Переведите:")
#бесконечный цикл пока слово пользователя не равно exitWord:
userText = ""
while(userText != exitWord):
	wordPosition = random.randint(intMinWords-1, intMaxWords-1)
	myWord=engWords.keys()[wordPosition]
	userText = raw_input(myWord+'? ')
	if (userText==exitWord):
		print "Ну пока!"
		if (intQRight>0 or intQWrong>0):
			print "Правильных ответов: " + str(intQRight) + \
			". Неверных ответов: " + str(intQWrong)
			sys.exit()
	else:
		if (userText==engWords.values()[wordPosition]):
			print "Верно!!!"
			intQRight+=1
			intRight+=1
			if (intRight==3):
				print("Ты просто супер! :-)")
				intRight=0
		else:
			print ":-( неверно... Это слово " + engWords.values()[wordPosition]
			intRight=0
			intQWrong+=1
			#leanWords.update()
