LOAD DATA 
INFILE "..\mock data\Inventory"
INTO TABLE StfxUser
FIELDS TERMINATED BY ','
(UserID, First, Last, Address)
