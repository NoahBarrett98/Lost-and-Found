LOAD DATA 
INTO TABLE Technology
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql\Technology.dat"
FIELDS TERMINATED BY ','
(ItemID,tBrand,Device,SerialNo)