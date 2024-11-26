### STANDARD XII
<br>

`PYTHON`
<br><br>
[1] simple calculator performing only 4 operations (+ - * /) <br>
[2] check number is prime or not <br>
[3] input the string and count uppercase and lowercase letters <br>
[4] fibonacci series in tuple <br>
[5] bubble sort using list <br>
[6] user defined function to accept string as an input, input character for count, and display the total number of times the character is present <br>
[7] input element in tuple, count and display odd and even numbers, using function <br>
[8] addition of two numbers using file <br>
[9] copy the content of a file to another file <br>
[10] store and display multiple integers in file, and form a binary file <br>
[11] read a record from binary file student.txt <br>
[12] read the content of file student.csv <br>
[13] write data in file using writerows method student.csv <br>
[14] implement all basic operations of stack using list <br>
[15] display unique vowels present in the given word using stack <br>
[16] add delete display records of an employee using list implementation through stack <br><br>

`MYSQL`

[17] consider the following table named "Product", showing details of products being 
sold in a grocery shop
```bash
1. create the table product with appropriate data types and constraints 
2. identify the primary key from product
3. product code, name and price to descending order of their name, name is the same display the data to ascending order of price
4. add a new column discount to the table product
5. calculate value of the discount to table product as 10% of the price to all those products where the price is more than 100, otherwise the discount will be 0
6. display name, average of price from table product and group by name
7. display unique manufacturer from product 
8. display and count unique name from product
9. display name max(price) min(price) from table product and group by name
```
<br>

[18] using the car showroom database, write the sql queries for the following table <br>
![car-showroom](https://github.com/user-attachments/assets/c1b568aa-37d5-4add-af56-5f29719f2b8c)
```bash
1. add a new column discount to inventory table 
2. give appropriate discount values to all cars keeping mind the following - no discount on the lxi model - vxi model gives a 10% discount - 12% discount is given on cars other than lxi and vxi model
3. display name of costliest car with fuel is petrol
4. calculate average discount and total discount available on baleno cars
5. display total number of cars having no discount
```
<br>

[19] write the sql queries for the following table <br>
![customer-order](https://github.com/user-attachments/assets/bf68f148-afeb-42b0-b277-f640888da587)
```bash
1. find the total quantity sold per each product
2. find the customers who have placed more than 2 orders
3. find the average price of products sold per month
4. find the products that have been sold all months of a year
5. find the products that have a total sales value greater than 1000
```
<br>

[20] write the sql queries for the customer and order table <br>
![customer](https://github.com/user-attachments/assets/6d4c02d8-0533-47fa-a7a8-c6eab3594b44)
![orders](https://github.com/user-attachments/assets/b5a51ae9-8122-4624-bbd4-5bc9ce221759) <br>
```bash
1. perform an equi-join to find the customer name and order details
2. perform a natural join to find the customer name and order details
3. perform a cartesian product to find all combinations of customers and orders
4. insert a new record into the customers table
5. drop the orders table
6. use NULL and NOT NULL constraints
7. find customers whose names start with A
8. use a foreign key to enforce referential integrity
9. use a unique key to ensure that values to column are unique
10. delete a record from the orders table
```
<br>

[21] SET 1:  connect to a database <br>
```bash
1. establish a connection
2. check connection status
3. create a cursor
4. execute a selct query
5. execute an insert query
6. execute an update query
7. execute a delete query
8. fetch one row
9. fetch all rows
10. count rows
11. using %s format specifier
12. using format method
13. create a database
```
<br>

SET 2:  insert the following record in the table named student in database school <br>
`student_id` (integer)
`student_name` (string)
`student_dob` (date)
`student_fees` (float)

SET 2: note the following to establish connectivity between python and mysql <br>
`username` (root)
`password` (1234)
`host` (localhost)
`database` (school)

```bash
1. connect to the mysql database 
2. create a cursor object
3. prompt the user to enter the id, name, dob, and fees
4. prepare the sql query using placeholders
5. execute the sql query with the user provided values
6. commit the changes to the database
7. print a success message
8. close the database connection
```
