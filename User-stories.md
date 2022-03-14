# Case 1

> A user tastes the coffee Vinterkaffe 2022 from Trondheim brewery Jacobsen & Svart (roasted 20.01.2022), gives it 10 points and writes “Wow – an odyssey for the taste buds: citrus peel, milk chocolate, apricot!”. The coffee is a light roast, natural Bourbon (c. arabica) from the farm Nombre de Dios (1500 masl) in Santa Ana, El Salvador, has a price per kilo of 600 kr and is, according to the roastery, “A tasty and complex coffee for polar nights”. The coffee was harvested in 2021 and the farm was paid 8 USD per kilo. Input on the user side is roastery, coffee name, points and notes.

This can be done by inserting a new row into the tasting table with the given user input, and email corresponding to the users email.

# Case 2

>A user should be able to print a list of the users who have tasted most unique coffees so far this year, sorted in descending order. The list should contain the users’ full names and the number of coffees each user has drunk.

This can be done by joining the Tasting table with the User table and count the amount of tastings. Because tastings are relations, each tasting must be an unique coffee. Then you can sort based on this count. 

# Case 3

> One should be able to see which coffees offer the consumer most value for money (highest average number of points versus price), sorted in descending order. The list should contain the name of the roasteries, coffee names, prices and the average score.

This information can be gathered from the database by joining the roast table with the tasting table, calculating average points for all tastings and dividing by roast price. Finally returning names, prices, avg. score etc sorted by this value in descending order.

# Case 4

>  user searches for coffees which have been described as “floral”, either by users or roasteries. In return, the user should get a list containing roastery names and coffee names.

This can be done by joining the Tasing table with the Roast table naturally. Then you can filter this joined table for note-fields containing "floral" or description-fields containing "floral". Both the coffee name and roastery name is in this joined table.

# Case 5

>  user is tired of being disappointed by washed coffees and their occassionally quite boring taste profile, and therefore wishes to search for coffees from Rwanda and Colombia which are not washed. The application returns a list of roastery names and coffee names.

This information can be gathered from the database by joining the batc, farm and processing method tables. Then filtering out any row where the used method is washed and the farms are not located in Rwanda or Colombia. Finally returning the roastery-, and coffe-names of the remaining rows.