CREATE DATABASE IF NOT EXISTS tp4_data;
USE tp4_data;

CREATE TABLE IF NOT EXISTS myTable (
    id INT AUTO_INCREMENT,
    prenom VARCHAR(45) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO myTable (id, prenom) VALUES (NULL, 'Brook');
INSERT INTO myTable (id, prenom) VALUES (NULL, 'Antoine');
INSERT INTO myTable (id, prenom) VALUES (NULL, 'Ventsoo');
