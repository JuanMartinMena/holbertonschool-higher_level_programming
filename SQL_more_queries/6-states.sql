-- Crear la base de datos solo si no existe
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Usar la base de datos
USE hbtn_0d_usa;

-- Crear la tabla 'states' solo si no existe
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT UNIQUE NOT NULL PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);
