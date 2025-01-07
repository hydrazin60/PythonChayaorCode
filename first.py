USE XYZuniversity
SELECT * FROM Teacher
SELECT * FROM Student
SELECT * FROM Department
SELECT * FROM  Student
WHERE Gender = 'Male' OR Qualification = 'MBA'
SELECT Name , RegistrationNumber FROM Student
WHERE Faculty = 'Science' AND  Program = 'BSC IT'


SELECT * FROM Student
WHERE  RegistrationNumber BETWEEN 'REG002' AND 'REG004'
---------------------UPDATE--------
UPDATE Teacher
SET ContactNumber = 9861967354
WHERE  TeacherID  = 'T001';
 
-----------DELETE----------
DELETE FROM Teacher
WHERE TeacherID = 'T004'
 
----------------------DROP----------
DROP FROM table_name WHERE condition
DROP TABLE table_name;
DROP DATABASE database_name;