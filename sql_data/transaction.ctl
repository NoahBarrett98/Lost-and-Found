LOAD DATA 
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\Transaction.dat"
INTO TABLE Transaction
FIELDS TERMINATED BY ','
(transID,itemID,transPrice,buyerID,sellerID,transDate,transAddress)