LOAD DATA 
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql_data\data\ISBN.dat"
INTO TABLE ISBN
FIELDS TERMINATED BY ','
(ISBN,Title,Author)