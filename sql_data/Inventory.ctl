LOAD DATA 
INTO TABLE InstrType
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\Inventory.dat"
FIELDS TERMINATED BY ','
(itemID,userID,listPrice,datePosted,category,postType,itemDescription,keywords,condition
)