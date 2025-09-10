CREATE DATABASE datatp4_sql;
USE datatp4_sql;

CREATE TABLE etudiants (
    id INT AUTO_INCREMENT,
    prenom VARCHAR(45) NOT NULL,
    PRIMARY KEY (id)
);

INSERT INTO etudiants (id, prenom) VALUES (NULL, 'Brook');
INSERT INTO etudiants (id, prenom) VALUES (NULL, 'Antoine');
INSERT INTO etudiants (id, prenom) VALUES (NULL, 'Ventsoo');
