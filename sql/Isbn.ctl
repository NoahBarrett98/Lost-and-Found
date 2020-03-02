
LOAD DATA 
INFILE "..\mock data\Inventory"
INTO TABLE Isbn
FIELDS TERMINATED BY ','
(Isbn, Title, Author, Edition)