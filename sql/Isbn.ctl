LOAD DATA 
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\Isbn.dat"
INTO TABLE Isbn
FIELDS TERMINATED BY ','
(Isbn, Title, Author, Edition)