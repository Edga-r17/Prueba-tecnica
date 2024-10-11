CREATE TABLE Usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    fecha_de_registro DATE NOT NULL
);



INSERT INTO Usuarios (nombre, email, fecha_de_registro)
VALUES
('Juan Pérez', 'juan@example.com', '2024-01-15'),
('Ana Gómez', 'ana@example.com', '2024-02-10'),
('Luis Martínez', 'luis@example.com', '2024-03-05');
