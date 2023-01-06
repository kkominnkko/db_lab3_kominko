CREATE TABLE heroes (
	hero_name VARCHAR(250) NOT NULL,
	category_id INT NOT NULL,
	role_id INT NOT NULL,
	hero_strength INT NOT NULL,
	hero_agility INT NOT NULL,
	hero_intelligence INT NOT NULL
);

CREATE TABLE category (
	category_id INT NOT NULL,
	hero_category VARCHAR(100) NOT NULL
);

CREATE TABLE roles (
	role_id INT NOT NULL,
	hero_role VARCHAR(100) NOT NULL
);

ALTER TABLE heroes ADD PRIMARY KEY (hero_name); 
ALTER TABLE category ADD PRIMARY KEY (category_id); 
ALTER TABLE roles ADD PRIMARY KEY (role_id); 

ALTER TABLE heroes ADD CONSTRAINT FK_heroes_category FOREIGN KEY (category_id) 
REFERENCES category (category_id);
ALTER TABLE heroes ADD CONSTRAINT FK_heroes_roles FOREIGN KEY (role_id) 
REFERENCES roles (role_id);







