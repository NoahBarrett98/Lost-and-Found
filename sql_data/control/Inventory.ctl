LOAD DATA 
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql_data\data\Inventory.dat"
INTO TABLE Inventory
FIELDS TERMINATED BY ','
(itemID,userID,listPrice,PostDate,category,postType,Description,keywords,condition)