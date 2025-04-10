create database DataAnalytics;

use DataAnalytics;

CREATE TABLE Persons (
    PersonID int,
    LastName varchar(255),
    FirstName varchar(255),
    Address varchar(255),
    City varchar(255)
);

INSERT INTO Persons values(14,"Ekaashi","Nandi Vardhan Reddy","Tadipatri","Ananatapur");

INSERT INTO Persons values(15,"Malli","Durga Prasad","Balaji Nagar","Nellore"),
(16,"Mallu","Charan Reddy","Upparpalle","Tirupati");

SELECT * from Persons;

select City from Persons;

DELETE FROM Persons WHERE PersonID=15;

UPDATE Persons SET FirstName="Nandu Reddy" WHERE PersonID=14;


CREATE TABLE Users(
    UserID int auto_increment primary key,
    Username varchar(50),
    email varchar(255),
    passwordhash varchar(255),
    Firstname varchar(50),
    Lastname varchar(50),
    Dateofbirth Date,
    Createdat Datetime DEFAULT current_timestamp,
    Lastlogin datetime,
    Status ENUM('Active','Inactive','Suspended') DEFAULT ('Active'),
    INDEX (email)
);

INSERT into Users (UserId,Username,email,passwordhash,Firstname,Lastname,Dateofbirth,Createdat,Lastlogin,Status)
Values(1,'Nandu Reddy','nandu@gmail.com','password_123','Nandu','Ekaashi','2002-08-28',now(),now(),'Active');

select * from Users;

CREATE TABLE Students(
    student_id int primary key,
    name varchar(255),
    age int,
    check (age>18)
);

insert into Students values (1,'Nandu',21),(2,'Mahesh',22);

select * from Students;


CREATE TABLE Enrollments (
    enrollment_id int primary key,
    student_id int,
    course_id int,
    foreign key (student_id) references Students(student_id)
);

insert into Enrollments values(401,1,501),(402,2,502);

select * from Enrollments;

CREATE TABLE orderdetails (
     order_id int,
     product_id int,
     quantity int,
     Primary key (order_id,product_id)  -- composite key
);

truncate table Enrollments;

drop table Enrollments;


CREATE TABLE products(productid int,productname varchar(20), price int);

INSERT into products values(1,'Bike',200000),(2,'Bike',300000);

SELECT * FROM products;

INSERT INTO products values (1,'Bike',200000),(2,'Bike21',400000);

--  QUERY TO FIND OF THE MAXIMUM VALUE OF THE SPECIFIED COLUMN

SELECT MAX(price) FROM products;

SELECT MIN(price) FROM products;

SELECT MIN(price) AS Smallestprice,productid
FROM products
GROUP BY productid;

SELECT AVG(price) AS Smallestprice,productid
FROM products
GROUP BY productid;

select * from products;

-- QUERY TO FIND OUT NUMBER OF COLUMNS

SELECT count(*) AS numberofcolumns
FROM products;

-- QUERY TO FIND OUT THE COUNT OF PRODUCT WHOSE PRICE IS MORE THAN 200000

SELECT COUNT(productid)
FROM products
WHERE price > 200000;

-- QUERY TO REMOVE THE DUPLICATE PRICE VALUE AND RETURN THE COUNT WITHOUT DUPLICATE

SELECT COUNT(DISTINCT price)
FROM products;

-- SUM FUNCTION TO GET THE TOTAL OF ALL THE PRICES

SELECT SUM(price)
FROM products;

SELECT AVG(price)
FROM products;


CREATE TABLE customers (
    customer_id int primary key,
    name varchar(100)
);

CREATE TABLE orders (
     order_id int primary key,
     customer_id int,
     product varchar(100),
     foreign key (customer_id) REFERENCES customers(customer_id)
     ON DELETE CASCADE
);

-- INSERT INTO CUSTOMERS

insert into customers values(1,'Nandu'),(2,'Mahesh'),(3,'Charan');

-- INSERT INTO ORDERS

insert into orders values(101,1,'mobile'),(102,1,'Tablet'),(103,2,'laptop'),(104,3,'Buds');

select * from customers;
select * from orders;

DELETE FROM customers WHERE customer_id=1;

UPDATE customers set name = 'krishna' where customer_id=3;

-- CLAUSES

SELECT * FROM products
ORDER BY price; 

SELECT * FROM products
ORDER BY price DESC;

CREATE TABLE Customerstable (
    CustomerID INT PRIMARY KEY,
    CustomerName VARCHAR(100),
    ContactName VARCHAR(100),
    Country VARCHAR(50)
);
 
CREATE TABLE Orderstable (
    OrderID INT PRIMARY KEY,
    OrderDate DATE,
    CustomerID INT,
    Amount DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customerstable(CustomerID)
);
 
INSERT INTO Customerstable (CustomerID, CustomerName, ContactName, Country) VALUES
(1, 'John Doe', 'John D.', 'USA'),
(2, 'Jane Smith', 'Jane S.', 'UK'),
(3, 'Alice Brown', 'Alice B.', 'Canada'),
(4, 'Bob Johnson', 'Bob J.', 'Australia');
 
INSERT INTO Orderstable (OrderID, OrderDate, CustomerID, Amount) VALUES
(101, '2024-09-01', 1, 250.00),
(102, '2024-09-05', 2, 300.00),
(103, '2024-09-07', 1, 150.00),
(104, '2024-09-10', 3, 450.00);

SELECT
     Customerstable.CustomerID,
     Customerstable.CustomerName,
     Orderstable.OrderID,
     Orderstable.OrderDate,
     Orderstable.Amount
FROM 
     Customerstable
INNER JOIN
     Orderstable ON Customerstable.CustomerID = Orderstable.CustomerID;
     
     
SELECT
     Customerstable.CustomerID,
     Customerstable.CustomerName,
     Orderstable.OrderID,
     Orderstable.OrderDate,
     Orderstable.Amount
FROM 
     Customerstable
LEFT JOIN
     Orderstable ON Customerstable.CustomerID = Orderstable.CustomerID;
     

SELECT
     Customerstable.CustomerID,
     Customerstable.CustomerName,
     Orderstable.OrderID,
     Orderstable.OrderDate,
     Orderstable.Amount
FROM 
     Customerstable
RIGHT JOIN
     Orderstable ON Customerstable.CustomerID = Orderstable.CustomerID;
     

SELECT
     Customerstable.CustomerID,
     Customerstable.CustomerName,
     Orderstable.OrderID,
     Orderstable.OrderDate,
     Orderstable.Amount
FROM 
     Customerstable
JOIN
     Orderstable ON Customerstable.CustomerID = Orderstable.CustomerID;
     
SELECT
     Customerstable.CustomerID,
     Customerstable.CustomerName,
     Orderstable.OrderID,
     Orderstable.OrderDate,
     Orderstable.Amount
FROM 
     Customerstable
CROSS JOIN
     Orderstable ON Customerstable.CustomerID = Orderstable.CustomerID;
     
     
CREATE TABLE drinks(id int,name varchar(10));

CREATE TABLE snacks(id int,name varchar(15));

INSERT INTO drinks values (1,'sprite'),(2,'Fanta');

Insert Into snacks values (1,'Egg Puff'),(2,'samosa');

SELECT drinks.id,drinks.name,snacks.id,snacks.name
FROM drinks
CROSS JOIN snacks;

CREATE TABLE Employee(Emp_ID int,Ename varchar(255),Job_Desc varchar(255),salary int,hire_date date);

insert into employee values(1,'Nandu','admin',100000,date '2020-08-28');
insert into employee values(2,'vishnu','manager',200000,date'2022-04-24');
insert into employee values(3,'manikanta','sales',300000,date'2008-07-14');
insert into employee values(4,'rohith','sales',450000,date '2005-07-23');
insert into employee values(5,'rahul','HR',600000,date '2014-04-18');

select * from employee;

select * from employee order by Job_Desc;

-- AVERAGE SALARY FOR EACH DEPARTMENT

select Job_Desc,avg(salary) from employee group by Job_Desc;

-- COUNT THE NUMBER OF EMPLOYESS IN EACH DEPARTMENT

select Job_Desc,count(emp_id) from employee group by Job_Desc;

select Job_Desc,count(emp_id)
from employee
group by Job_Desc
having count(emp_id)>0
order by Job_Desc;

select Job_Desc,count(emp_id)
from employee where salary>200000
group by Job_Desc
having count(emp_id)>1
order  by Job_Desc;

-- subquery is executed first .output of subquery as the input for the main query

select ename from Employee where salary <
(select avg(salary) from Employee);


CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);
 
CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO departments (department_id, department_name) VALUES
(1, 'Sales'),
(2, 'Marketing'),
(3, 'HR');

Insert into departments values(4,'development');
 
INSERT INTO employees (employee_id, employee_name, department_id) VALUES
(101, 'Alice', 1),
(102, 'Bob', 1),
(103, 'Charlie', 2),
(104, 'Diana', 3);

-- to find the name of employees who work in the sales department 

select * from employees
where department_id in (
select department_id from departments
where department_name = 'sales'
);

 
select employee_name 
from employees
where department_id = (select department_id 
					   from departments
                       where department_name='sales');
                       
/**suppose you want to include the department name along with ecah employee's name. You can use a subquery in the select clause
to retrieve the department name.**/

select employee_name,
         ( select department_name 
           from departments
           where departments.department_id = employees.department_id) as deopartment_name
from employees;

/** find employees who are in deparment with more than 1 employee **/

select employee_name 
from employees
where department_id in (select department_id from employees
					    group by department_id
                        having count(*) > 1);
		
/** Find department that have at least one employee **/

select department_name
from departments d
where exists (select 1 
              from employees e
              where e.department_id = d.department_id);
              
/** Find departments that do not have any employees **/

select department_name
from departments d
where not exists (select 1
				  from employees e
                  where e.department_id = d.department_id);
                  
/** find departments where the average employee ID is greater than 102 **/

select department_id
from employees
group by department_id
having avg(employee_id)>102;

-- scalar functions operate on a single value and return a single values

select ucase("Hello World") as Upper_case_string;

select lcase("Hello World") as Lpper_case_string;

select mid("Hello World",4,8) as sub_string;

select length("Hello World") as string_length;

select ucase("Hello World") as Upper_case_string;

select round(1560.44444,2) as round_value;

select now() as currentdatetime;

select format(1234.1234,2) as format_number;


create table product(
       product_id int primary key,
       product_name varchar(255),
       product_price int
);


create table user(
     user_id int Auto_increment,
     name varchar(100),
     primary key(user_id)
);

insert into user (user_id,name) values (101,'nandu'),(102,'charan');

select name from user;

create table coupon(id int,coupon_name varchar(255),coupon_code varchar(255));

insert into coupon(id,coupon_name,coupon_code) values (150,'Jane smith','SAVE10'),(108,'Bethell','BET33'),(105,'Alice Brown',NULL);

select * from coupon;

-- TCL commands 

use dataanalytics;

delete from products;
select * from products;

start transaction;

savepoint point;

insert into products values(9,'Maruthi',500000);
insert into products values(10,'suziki',500000);

select * from products;

rollback to point;

commit;

DELIMITER //
CREATE PROCEDURE getallusers()
begin
    select * from users;
end;
//

call getallusers()

Delimiter //
create procedure getproductid(in productno int)
begin
    select productid,productname,price
    from products
    where productid=productno;
end
//

DELIMITER ;

call getproductid(9);

Delimiter //

create procedure getproduct_name(in product_id int, out name varchar(255))
begin
    select productname into name
    from products
    where productid = product_id;
end //

delimiter ;

set @product_name = '';

call getproduct_name(10,@product_name);

select @product_name;
