LOAD DATA 
INTO TABLE User
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\User.dat"
FIELDS TERMINATED BY ','
(userID,fName,lName,userAddress)