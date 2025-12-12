CREATE DATABASE IF NOT EXISTS steam_db;
USE steam_db;


CREATE TABLE IF NOT EXISTS developers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country VARCHAR(100)
);


CREATE TABLE IF NOT EXISTS games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2),
    developer_id INT,
    FOREIGN KEY (developer_id) REFERENCES developers(id) ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS game_categories (
    game_id INT,
    category_id INT,
    PRIMARY KEY (game_id, category_id),
    FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

INSERT INTO developers (name, country) VALUES ('Valve', 'USA'), ('CD Projekt Red', 'Poland');
INSERT INTO categories (name) VALUES ('Shooter'), ('Strategy'), ('RPG');
INSERT INTO games (title, price, developer_id) VALUES ('Dota 2', 0.00, 1), ('Cyberpunk 2077', 59.99, 2);
INSERT INTO game_categories (game_id, category_id) VALUES (1, 2), (1, 1), (2, 3);