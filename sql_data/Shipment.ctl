LOAD DATA 
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\Shipment.dat"
INTO TABLE Sports
FIELDS TERMINATED BY ','
(shipmentID,itemID,userAddress,recyclerID,recyclerAddress,dateShipped)