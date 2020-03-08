LOAD DATA 
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\Technology.dat"
INTO TABLE Technology
FIELDS TERMINATED BY ','
(ItemID,Brand,DeviceType,SerialNo)