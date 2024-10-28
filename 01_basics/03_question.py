studentMarks = int(input("Enter your marks: "))

if(studentMarks > 100):
   print("Invalid marks")

elif(studentMarks < 0):
   
  if(studentMarks >= 90):
   grade = "A"
  elif(90 > studentMarks >= 80):
    grade = "B"
  elif(80 > studentMarks >= 70):
    grade = "C"
  elif(70 > studentMarks >= 60):
    grade = "D"
  elif(60 > studentMarks >= 50):
    grade = "E"
  else:
    grade = "F"   
  print("Your grade is ", grade)   


   
 


 