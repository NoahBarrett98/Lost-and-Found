LOAD DATA 
INTO TABLE Recycler
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql_data\data\Recycler.dat"
FIELDS TERMINATED BY ','
(RcyclID ,Name,PhoneNo,Email,Address,recyclerCategory)