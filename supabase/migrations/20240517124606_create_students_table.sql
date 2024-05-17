-- Membuat tabel students
CREATE TABLE students (
    id BIGINT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    major VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Membuat tipe data ENUM untuk status
CREATE TYPE status_enum AS ENUM ('attend', 'absent');

-- Membuat tabel absensi
CREATE TABLE absensi (
    id SERIAL PRIMARY KEY,
    student_id BIGINT NOT NULL,
    status status_enum NOT NULL DEFAULT 'absent',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_student
        FOREIGN KEY(student_id) 
        REFERENCES students(id)
);
