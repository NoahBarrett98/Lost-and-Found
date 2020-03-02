LOAD DATA 
INFILE "..\mock data\Inventory"
INTO TABLE Inventory
FIELDS TERMINATED BY ','
(ItemID, UserID, ListPrice, PostDate, Category, PostType, Description, Condition)

LOAD DATA 
INFILE "..\mock data\Inventory"
INTO TABLE Isbn
FIELDS TERMINATED BY ','
(Isbn, Title, Author, Edition)

LOAD DATA 
INFILE "..\mock data\Inventory"
INTO TABLE StfxUser
FIELDS TERMINATED BY ','
(UserID, First, Last, Address)


LOAD DATA 
INFILE "..\mock data\Inventory"
INTO TABLE UsedIn
FIELDS TERMINATED BY ','
(Crn, Isbn, Year)

