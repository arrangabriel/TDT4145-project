**User**(<u>email</u>, password, firstname, lastname)

There are no functional dependencies amongst the attributes of User, it is therefore in BCNF.

**Tasting**(<u>userEmail</u>, <u>roastery</u>, <u>roastName</u>, note, points, date)

- userEmail is a foreign key of User
- roastery and roastName are foreign keys of Roast

There are no functional dependencies amongst the attributes of Tasting, it is therefore in BCNF.

**Roast**(<u>roastery</u>, degree, date, <u>name</u>, description, price, batchID)

- batchID is a foreign key of Batch
- price in NOK

There are no functional dependencies amongst the attributes of Roast, it is therefore in BCNF.

**Batch**(<u>batchID</u>, price, year, processingMethod, farmID)

- processingMethod is a foreign key of ProcessingMethod
- farmID is a foreign key of ProcessingMethod
- price in USD

There are no functional dependencies amongst the attributes of Batch, it is therefore in BCNF.

**ProcessingMethod**(<u>name</u>, description)

There are no functional dependencies amongst the attributes of ProcessingMethods, it is therefore in BCNF.

**Farm**(<u>farmID</u>, name, country, region, masl)

With the assumption that a region name can exist in multiple countries there are no funcitonal dependencies amongst the attributes of Farm, and it is therefore in BCNF. If country is functionally dependent on region there is a transitive dependency from farmID to country, and Farm is therefore only in 2NF.

**BatchBean**(<u>batchID</u>,<u>beanName</u>, beanSpecies)

- batchID is a foreign key of Batch

There are no functional dependencies amongst the attributes of BatchBean, it is therefore in BCNF.