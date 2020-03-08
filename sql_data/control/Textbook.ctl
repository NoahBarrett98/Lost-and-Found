LOAD DATA 
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql_data\data\Textbook.dat"
INTO TABLE Textbook
FIELDS TERMINATED BY ','
(ItemID,Isbn)