LOAD DATA 
INTO TABLE UsedIn
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\UsedIn.dat"
FIELDS TERMINATED BY ','
(CRN,ISBN,Year)