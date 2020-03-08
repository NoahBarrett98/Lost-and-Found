LOAD DATA 
INTO TABLE Clothing
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\Clothing.dat"
FIELDS TERMINATED BY ','
(userID,fName,lName,userAddress)