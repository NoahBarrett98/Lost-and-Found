# Lost-and-Found
CSCI 275 Database 

## Todo
1. **Datasets**
    - Brand
    - Article (clothing)
    - Sport
    - ~~FirstNames~~
    - LastNames
    - UserIDs
    - CourseDept 
    - CourseNo 
    - CourseName
    - CRN
    - ISBN
    - Addresses

2. **Features**
    - Functions for generating individual attributes (_genFirstName, _genLastName, etc)
        - **Not unique**
            - ~~First name~~
            - ~~Last name~~
            - ~~Article~~
            - Sport
            - ~~Brand~~
            - ~~CourseDept~~
            - ~~CourseNo~~
            - ~~CourseName~~
            - Address
            - ~~Date~~
            - ~~category~~
            - ~~condition~~
            - ~~device~~
            - edition
            - ~~instr type~~
            - item  desc
            - ~~item id~~
            - key words
            - ~~price~~
            - post type
            - size
            - ~~year~~
        - **Unique** (will have to be treated differently)
            - ~~ID~~
            - CRN
            - ~~ISBN~~
            - ~~phone number~~
            - email address
    - Function- for generating individual entries (_genUser, _genUsedIn, _genClass)
        - User
        - Used in
        - Class
        - Inventory
        - Textbook
        - ISBN
        - Technology
        - Clothing
        - Musical Instr
        - Sporting good
        - Shipment
        - Recyclers
        - Transaction
    - Write generated csv data (users, items, classes, etc.) to text file
        - same as above, but allow number of entries to be specified
    - Script that actually loads and writes data
