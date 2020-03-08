LOAD DATA 
INTO TABLE Class
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\Class.dat"
FIELDS TERMINATED BY ','
(CRN,deptCode,courseNum,courseName)