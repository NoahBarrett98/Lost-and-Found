LOAD DATA 
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql_data\data\UsedIn.dat"
INTO TABLE UsedIn
FIELDS TERMINATED BY ','
(CRN,ISBN,Year)