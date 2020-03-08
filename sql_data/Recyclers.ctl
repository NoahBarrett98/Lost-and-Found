LOAD DATA 
INTO TABLE Recyclers
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\Recyclers.dat"
FIELDS TERMINATED BY ','
(recyclerID,companyName,companyNumber,companyEmail,companyAddress,recyclerCategory)