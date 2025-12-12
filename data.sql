-- Створення бази даних
CREATE DATABASE IF NOT EXISTS steam_db;
USE steam_db;

-- 1. Таблиця Розробників (Developer)
CREATE TABLE IF NOT EXISTS developers (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    country VARCHAR(100)
);

-- 2. Таблиця Ігор (Game) - зв'язок M:1
CREATE TABLE IF NOT EXISTS games (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    price DECIMAL(10, 2),
    developer_id INT,
    FOREIGN KEY (developer_id) REFERENCES developers(id) ON DELETE SET NULL
);

-- 3. Таблиця Категорій (Category)
CREATE TABLE IF NOT EXISTS categories (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

-- 4. Стиковочна таблиця (Game_Category) - зв'язок M:M
CREATE TABLE IF NOT EXISTS game_categories (
    game_id INT,
    category_id INT,
    PRIMARY KEY (game_id, category_id),
    FOREIGN KEY (game_id) REFERENCES games(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES categories(id) ON DELETE CASCADE
);

-- Тестові дані (щоб база не була пустою)
INSERT INTO developers (name, country) VALUES ('Valve', 'USA'), ('CD Projekt Red', 'Poland');
INSERT INTO categories (name) VALUES ('Shooter'), ('Strategy'), ('RPG');
INSERT INTO games (title, price, developer_id) VALUES ('Dota 2', 0.00, 1), ('Cyberpunk 2077', 59.99, 2);
INSERT INTO game_categories (game_id, category_id) VALUES (1, 2), (1, 1), (2, 3);