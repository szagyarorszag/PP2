-- SELECT <some list from table > , <also some list from table>
-- We use it when we want to choose some list in the table


-- SELECT * 
-- We use this star to chhose all lists of the table


-- FROM <table> , <another one>
-- we use it to choose some table 
-- FROM <database>.<table>
-- we also can take data like this from exactly one database 


-- WHERE <some condition>
-- We use it to get exactly something 

--      <list> IN (some elements in list)
--          IT is the pretty or logic operator 
--      <list> BETWEEN (some range) 
--          If we werent use it we will be write like this below
--          <list> >= number AND <list> <= another number 
--      <list> LIKE '<any symbols>%' 
--          we use it to sort some list by first symbols of the elements
--          after using % after symbols it means thet we dont care about other symbols and their quantity
--          also '%B%' means thet we taking some strings which includes 'B' or 'b' symbol and we dont care about order or quantity
--          and '%B' means that we taking elements where at the end of the string we have 'B' symbol 
--      <list> LIKE '_y'
--          we use it to get a string or may not string if you want eith exactly two symbols and at the end of the string there should be 'y' symbol
--      <list> LIKE '_____y' 
--          here for example we have a string length by 6 symbols and at the end of this string there should be 'y' symbol 
--      <list> REGEXP 'B'
--          we use it to find the data about in list which contains 'B'
--      <list> REGEXP '^B' 
--          we use it to find a string in this list which contains 'B' at the beggining of the element
--      <list> REGEXP 'b$' 
--          we use it to find a data in this list which contains 'B' at the end of the element in this list
--      <list> REGEXP 'b|c|d'
--          in this case "|" is just OR statement
--      <list> REGEXP '[fad]e'
--          in this case we can see that the befor e should be exactly one of those symbils into the braces and it should be before element outside the braces
--          FE: we cab represent it as  <list> REGEXP 'fe' OR <list> REGEXP 'ae' OR <list> REGEXP 'de' 
--      <list> REGEXP 'e[fad]'
--          same thing as article below but here e is first
--      <list> REGEXP 'e[f-x]'
--          it means that we will use all symbols from f till x 
--      <list> IS NOT NULL 
--          we can use to find the data which is contains some elements from list
--      <list> IS NULL 
--          we can use to find the data which isn't contains some elements from list

-- ORDER BY <a list of the table>
-- We use it to show the table in some order of the the some list
--      ORDER BY <a list of the table> DESC 
--      We use DESC to reverse the column

-- LIMIT <n-number> 
-- We use it for showing n-numbers(lines) of data 
--          LIMIT <k-number> , <n-number>
--          we skiping k numbers and showing n numbers of data

-- FROM <table1>
-- INNER JOIN <table2> ON <table1>.<list2> = <table2>.<list2>
-- We use it to add data from another table to another

-- FROM <database1>.<table1> 
-- OR 
-- JOIN <database1>.<table1> 
-- We use it to get some data from another database

--IF you want use JOIN two pimary keys you should use AND 


-- Implicit Join Syntax 
--SELECT *
--FROM orders o, customers c  
--WHERE ON o.customer_id = c.customer_id
--LEFT JOIN <table1>
-- We use LEFT JOIN to get information wheter ON(condition) it is true or not ( we using LEFT for the most left list)
-- same story with RIGHT func 


-- USING (<list>)
-- We use it after JOIN to don't write ON <table1>.<list1> = <table2>.<list1> 