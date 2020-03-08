LOAD DATA 
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\Clothing.dat"
INTO TABLE Clothing
FIELDS TERMINATED BY ','
(ItemID,Brand,CSize,Article)