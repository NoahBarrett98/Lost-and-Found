LOAD DATA 
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql_data\data\Shipment.dat"
INTO TABLE Shipment
FIELDS TERMINATED BY ','
(ShipID,itemID,userAddress,RcyclAddress,dateShipped)