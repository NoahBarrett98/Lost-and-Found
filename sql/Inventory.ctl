LOAD DATA 
INFILE "..\mock data\Inventory"
INTO TABLE Inventory
FIELDS TERMINATED BY ','
(ItemID, UserID, ListPrice, PostDate, Category, PostType, Description, Condition)