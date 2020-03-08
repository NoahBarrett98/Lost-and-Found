LOAD DATA 
INTO TABLE ISBN
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\ISBN.dat"
FIELDS TERMINATED BY ','
(ISBN,Title,Author)