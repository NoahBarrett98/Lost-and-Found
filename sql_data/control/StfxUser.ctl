LOAD DATA 
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql_data\data\StfxUser.dat"
INTO TABLE StfxUser
FIELDS TERMINATED BY ','
(UserID,First,Last,Address)