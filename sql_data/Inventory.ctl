LOAD DATA 
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\Inventory.dat"
INTO TABLE InstrType
FIELDS TERMINATED BY ','
(itemID,userID,listPrice,PostDate,category,postType,Description,keywords,condition
)