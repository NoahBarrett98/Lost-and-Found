LOAD DATA 
INFILE "..\mock data\Inventory"
INTO TABLE UsedIn
FIELDS TERMINATED BY ','
(Crn, Isbn, Year)
