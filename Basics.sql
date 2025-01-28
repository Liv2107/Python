
CREATE TABLE employee (
    empID int NOT NULL UNIQUE,
    FirstName varchar(255) NOT NULL,
    LastName varchar(255) NOT NULL,
    Address varchar(255) NOT NULL,
    Department varchar(255) NOT NULL,
    PRIMARY KEY (empID),
    FOREIGN KEY (depID) REFERENCES department(depID)
);

ALTER TABLE employee ADD Age int;

CREATE TABLE department (
    depID int NOT NULL UNIQUE,
    Name varchar(255) NOT NULL,
    PRIMARY KEY (depID, Name)
);

SELECT * FROM employee;