LOAD DATA 
INFILE "C:\Users\x2017sre\Downloads\PortableGit\Lost-and-Found\sql_data\data\Recycler.dat"
INTO TABLE Recycler
FIELDS TERMINATED BY ','
(RcyclID ,Name,PhoneNo,Email,Address,recyclerCategory)