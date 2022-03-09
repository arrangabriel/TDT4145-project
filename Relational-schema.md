**User**(<u>email</u>, password, firstname, lastname)

**Tasting**(<u>userEmail</u>, <u>roastID</u>, note, points, date)

- userEmail is a foreign key of User
- roastID is a foreign key of Roast

**Roast**(<u>roastID</u>, roastery, degree, date, name, description, price, batchID)

- batchID is a foreign key of Batch
- price in NOK

**Batch**(<u>batchID</u>, price, year, processingMethod, farmID)

- processingMethod is a foreign key of ProcessingMethod
- price in USD

**ProcessingMethod**(<u>name</u>, description)

**Farm**(<u>farmID</u>, name, country, region, masl)

**BatchSpecies**(<u>batchID</u>, <u>beanSpecies</u>)

- batchID is a foreign key of Batch