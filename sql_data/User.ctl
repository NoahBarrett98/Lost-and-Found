LOAD DATA 
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\User.dat"
INTO TABLE User
FIELDS TERMINATED BY ','
(UserID,fName,lName,userAddress)