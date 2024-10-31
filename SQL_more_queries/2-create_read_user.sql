-- Crear la base de datos solo si no existe
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Crear el usuario solo si no existe, y establecer su contraseña
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- Conceder privilegio de SELECT únicamente en la base de datos hbtn_0d_2
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
