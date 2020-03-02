LOAD DATA 
INTO TABLE Inventory
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\Inventory.dat"
FIELDS TERMINATED BY ','
(ItemID, UserID, ListPrice, PostDate, Category, PostType, Description, Condition)