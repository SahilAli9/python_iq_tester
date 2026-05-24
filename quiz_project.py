   #---------------- IQ TESTER ----------------#
    #----------------THE_KIRA_X --------------#
    
    
import time
print("Quiz loading...")
time.sleep(1)
print("ready")
time.sleep(1)
print("start:")
print("\n")
print("There Are 10 Questions Complete 10/10 To Get Your Iq Score:")
print("\n")
name=input("Your Name:\n")

question_1=[{"Q.No1 Number Pattern":"2 ,6 ,7 ,21 ,23 ,69 what comes next ?","options":["A.70","B.71","C.72","D.73"],"Answer":"D.73","points":"5"}]
question_2=[{"Q.No2 Odd One Out":"?","options":["A.Cube","B.Sphere","C.Pyramid","D.Circle"],"Answer":"D.Circle","points":"15"}]
question_3=[{"Q.No3 Letter Pattern":"A , C , F , J , O what comes next ?","options":["A.S","B.T","C.U","D,V"],"Answer":"C.U","points":"20"}]
question_4=[{"Q.No4 Logical Sequence":" If Cat is 24 Dog is 26 Then Bat ?","options":["A.21","B.22","C.23","D.24"],"Answer":"C.23","points":"10"}]
question_5=[{"Q.No5 Coding Decoding":" If Flower is GMPXFS Then Garden is ?","options":["A.HBSFEO","B.HBSDFO","C.HCRFEO","D.HBSFEN"],"Answer":"A.HBSFEO","points":"5"}]
question_6=[{"Q.No6 Missing Number":" 3 , 9 , 27 , 81 what comes next ?","options":["A.162","B.243","C.324","D.729"],"Answer":"B.243","points":"10"}]
question_7=[{"Q.No7 Logical Puzzle":"all Roses Are flowers Some Flowers Fade Quickly ?","options":["A.All Roses Fade Quickly","B.Some Roses Fade Quickly","C.No Roses Fade Quickly","D.Cannot Be Determined"],"Answer":"D.Cannot Be Determined","points":"10"}]
question_8=[{"Q.No8 Mirror Logic":"If LEFT=RIGHT in a mirror then,TOP becomes ?","options":["A.Bottom","B.Pot","C.Still Top","D.Cannot Say"], "Answer":"C.Still Top","points":"20"}]
question_9=[{"Q.No9 Hard Pattern":"1 , 1 , 2 , 6 , 24 what comes next ?","options":["A.48","B.96","C.120","D.720"], "Answer":"C.120","points":"10"}]
question_10=[{"Q.No10 Hard Logic Question":"A Man Looks At A Photo And Says/nBrothers and sisters , i have none/nBut That Mans Father Is My Son/nWho Is in The Picture ?","options":["A.His Cousin", "B. His Son", "C.He Himself" , "D.His Father"],"Answer":"D.His Father","points":"30"}]



           
          #--------- Questions ---------#
         #----------- Startup ------------# 
         
total_score=0       

for items in question_1:
    print("Q.No1:",items["Q.No1 Number Pattern"])
for options in items["options"]:
    print(options)
user_answer1=input("\nChoose Option (A/B/C/D:").upper()
if user_answer1 == "D":
   time.sleep(1)
   points=10
   total_score+=10
   print("Correct Answer\nScore +10")
   print("\n")
   
else:
    time.sleep(2)
    points= 2
    total_score+=2
    print("Wrong Answer Correct Is:",items["Answer"])
    print("Score",points)
    print("\n")

    
for items in question_2:
     print ("Q.No2: Odd One Out",items["Q.No2 Odd One Out"]) 
for options in items["options"]:
    print(options)
user_answer2=input("\nChoose Option (A/B/C/D:").upper()
if user_answer2 =="D":
    time.sleep(1)
    points=20
    total_score+=20
    print("Correct Answer\nScore +20")
    print("\n")
    
else:
    time.sleep(2)
    points=4
    total_score+=4
    print ("Wrong Answer Correct Is:",items["Answer"])
    print ("score",points)
    print("\n")
for items in question_3:
    print("Q.No3:",items["Q.No3 Letter Pattern"])
for options in items["options"]:
    print(options)
user_answer3=input("\nChoose Option (A/B/C/D:").upper()
if user_answer3 == "C":
    time.sleep(1)
    points=15
    total_score+=15
    print("Correct Answer\nScore +15")
    print("\n")

else:
    time.sleep(2)
    points=3
    total_score+=3
    print("Wrong Answer Correct Is:",items["Answer"])
    print ("score", points)
    print("\n")

for items in question_4:
    print("Q.No4:",items["Q.No4 Logical Sequence"])
for options in items["options"]:
    print(options)
user_answer4=input("\nChoose Option (A/B/C/D:").upper()
if user_answer4 == "C":
    time.sleep(1)
    points=12
    total_score+=12
    print("Correct Answer\nScore +12")
    print("\n")

else:
    time.sleep(2)
    points=4
    total_score+=4
    print("Wrong Answer Correct is:",items["Answer"])
    print("score",points)
    print("\n")
    
for items in question_5:
    print ("Q.No5",items["Q.No5 Coding Decoding"])
for options in items["options"]:
    print(options)
user_answer5=input("\nChoose Option (A/B/C/D:").upper()
if user_answer5== "A":
    time.sleep(1)
    points=20
    total_score+=20
    print("Correct Answer\nScore +20")
    print("\n")
else:
    time.sleep(2)
    points=5
    total_score+=5
    print("Wrong Answer Correct Is:",items["Answer"])
    print("score",points)
    print("\n")
    
for items in question_6:
    print("Q.No6:",items["Q.No6 Missing Number"])
for options in items["options"]:
    print(options)
user_answer6=input("\nChoose Option (A/B/C/D:").upper()
if user_answer6 == "B":
    time.sleep(1)
    points=10
    total_score+=10
    print("Correct Answer\n Score +10")
    print("\n")
else:
    time.sleep(2)
    points=2
    total_score+=2
    print("Wrong Answer Correct Is:", items ["Answer"])
    print("score",points)
    print("\n")
    
for items in question_7:
    print("Q.No7:",items["Q.No7 Logical Puzzle"])
for options in items["options"]:
    print(options)
user_answer7=input("\nChoose Option (A/B/C/D:").upper()
if user_answer7 == "D":
    time.sleep(1)
    points = 10
    total_score+=10
    print("Correct Answer\nScore +10")
    print("\n")
else:
    time.sleep(2)
    points=1
    total_score+=1
    print("Wrong Answer Correct Is:",items ["Answer"])
    print("score",points)
    
for items in question_8:
     print("Q.No8:",items["Q.No8 Mirror Logic"])
for options in items["options"]:
    print(options)
user_answer8=input("\nChoose Options (A/B/C/D:").upper()
if user_answer8 == "C":
    time.sleep(1)
    points=12
    total_score+=12
    print("Correct Answer\nScore +12")
    print("\n")
else:
    time.sleep(2)
    points=3
    total_score+=3
    print("Wrong Answer Correct Is:",items["Answer"])
    print("Score",points)
    print("\n")

for items in question_9:
    print("Q.No9:", items["Q.No9 Hard Pattern"])
for options in items["options"]:
    print(options)
user_answer9=input("\nChoose Option (A/B/C/D:").upper()
if user_answer9 == "C":
    time.sleep(1)
    points=15
    total_score+=15
    print("Correct Answer\nScore +15")
    print("\n")
else:
    time.sleep(2)
    points=5
    total_score+=5
    print("Wrong Answer Correct Is:",items["Answer"])
    print("Score +5", points)
    print("\n")
    
for items in question_10:
    print ("Q.No10:",items["Q.No10 Hard Logic Question"])
for options in items["options"]:
    print(options)
user_answer10=input("Choose Option (A/B/C/D:").upper()
if user_answer10 == "D":
    time.sleep(1)
    points=20
    total_score+=20
    print("Correct Answer\nScore +20")
    print("\n")
else:
    time.sleep(2)
    points=5
    total_score+=5
    print("Wrong Answer Correct Is:",items["Answer"])
    print("Score +5",points)
    print("\n")
    
    
       #------------ Results -----------#
print(name,"Your Total Score Is", total_score,"/130")
print("\n")
if total_score >=100:
    print("Dear",name,"You Are A Genius\nYour IQ is on Pro Level")
elif total_score >=70:
    print("Dear",name, "Almost You Tried Your Best\nYour IQ Is On Intermediate Level")
elif total_score >= 50:
    print("Dear",name, "Your IQ Is Too Low\n Your IQ Is On Beginner Level")
else:
    ("Dear",name,"You Make Me Feel So Cold\nYour IQ Is Below Beginner Level")
    

#for items in question_2:
   # print(items["options"].replace(",","\n"))


#if len(name)  5 => 0

#names=["sahil","rahil","mahil","gahil","fahil"]
#print(*names[1:2])

#questions=[{"q": "5+5?" , "options": ["a.8" , "b.9" , "c.10"] , "answer":"c" }]
#print(*questions[0]["options"])
#print(questions[0]["answer"])
#for sahil in questions[0]["options"]:
  



""" 
iq test 
"""









































#students.add.              for sets because they are immutable 
#students.diff()
#student.add()
#students.clear()
    
#students=["sahil","rahil","mahil"]
#print(students[0])
#students.append("gahil")
#print(*students)            #list
#("\n")

#person={"name":"sahil","age":16}
#print(person["name"])
#quiz = [
  #  {"question": "2+2?", "answer": "4"},
  #  {"question": "3+3?", "answer": "6"}
#]
#for q in quiz: