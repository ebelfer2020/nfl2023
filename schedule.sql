CREATE TABLE bears_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/bears/bears_2023_schedule.csv'
INTO TABLE bears_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE bengals_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/bengals/bengals_2023_schedule.csv'
INTO TABLE bengals_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE bills_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/bills/bills_2023_schedule.csv'
INTO TABLE bills_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE broncos_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/broncos/broncos_2023_schedule.csv'
INTO TABLE broncos_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE browns_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/browns/browns_2023_schedule.csv'
INTO TABLE browns_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE buccaneers_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/buccaneers/buccaneers_2023_schedule.csv'
INTO TABLE buccaneers_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE cardinals_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/cardinals/cardinals_2023_schedule.csv'
INTO TABLE cardinals_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE chargers_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/chargers/chargers_2023_schedule.csv'
INTO TABLE chargers_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE chiefs_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/chiefs/chiefs_2023_schedule.csv'
INTO TABLE chiefs_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE colts_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/colts/colts_2023_schedule.csv'
INTO TABLE colts_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE commanders_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/commanders/commanders_2023_schedule.csv'
INTO TABLE commanders_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE cowboys_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/cowboys/cowboys_2023_schedule.csv'
INTO TABLE cowboys_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE dolphins_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/dolphins/dolphins_2023_schedule.csv'
INTO TABLE dolphins_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE eagles_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/eagles/eagles_2023_schedule.csv'
INTO TABLE eagles_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE falcons_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/falcons/falcons_2023_schedule.csv'
INTO TABLE falcons_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE giants_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/giants/giants_2023_schedule.csv'
INTO TABLE giants_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE jaguars_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/jaguars/jaguars_2023_schedule.csv'
INTO TABLE jaguars_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE jets_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/jets/jets_2023_schedule.csv'
INTO TABLE jets_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE lions_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/lions/lions_2023_schedule.csv'
INTO TABLE lions_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE niners_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/niners/niners_2023_schedule.csv'
INTO TABLE niners_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE packers_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/packers/packers_2023_schedule.csv'
INTO TABLE packers_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE panthers_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/panthers/panthers_2023_schedule.csv'
INTO TABLE panthers_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE patriots_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/patriots/patriots_2023_schedule.csv'
INTO TABLE patriots_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE raiders_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/raiders/raiders_2023_schedule.csv'
INTO TABLE raiders_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE rams_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/rams/rams_2023_schedule.csv'
INTO TABLE rams_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE ravens_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/ravens/ravens_2023_schedule.csv'
INTO TABLE ravens_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE saints_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/saints/saints_2023_schedule.csv'
INTO TABLE saints_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE seahawks_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/seahawks/seahawks_2023_schedule.csv'
INTO TABLE seahawks_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE steelers_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/steelers/steelers_2023_schedule.csv'
INTO TABLE steelers_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE texans_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/texans/texans_2023_schedule.csv'
INTO TABLE texans_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE titans_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/titans/titans_2023_schedule.csv'
INTO TABLE titans_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
CREATE TABLE vikings_2023_schedule (
id INTEGER,
week INTEGER,
date VARCHAR(15),
time VARCHAR(10),
opponent VARCHAR(30),
result VARCHAR (15),
recond VARCHAR (7),
venue  VARCHAR (30),
network VARCHAR(15), 
recap VARCHAR(5), 
PRIMARY KEY (id) 
);
LOAD DATA LOCAL INFILE '~/nfl2023/vikings/vikings_2023_schedule.csv'
INTO TABLE vikings_2023_schedule
FIELDS TERMINATED BY ','
IGNORE 1 ROWS;
