-- Tambahkan kolom baru 'number_absence' dengan tipe data int
ALTER TABLE students
ADD COLUMN number_absence INT;

-- Hapus foreign key dari tabel absensi
ALTER TABLE absensi DROP CONSTRAINT fk_student;

-- Drop kolom student_id dari tabel absensi
ALTER TABLE absensi DROP COLUMN student_id;

-- Ubah tipe data kolom 'id' menjadi UUID
ALTER TABLE students
ALTER COLUMN id SET DATA TYPE NUMERIC;

-- Tambahkan kolom student_id dengan tipe NUMERIC di tabel absensi
ALTER TABLE absensi ADD COLUMN student_id NUMERIC;

-- Tambahkan foreign key ke tabel students
ALTER TABLE absensi
ADD CONSTRAINT fk_student
FOREIGN KEY (student_id)
REFERENCES students(id);
