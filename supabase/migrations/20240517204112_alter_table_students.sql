-- Create the enum type for majors if it doesn't already exist
DO $$
BEGIN
    IF NOT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'majors') THEN
        CREATE TYPE majors AS ENUM ('SIJA', 'DKV', 'MM', 'TKJ', 'TITL', 'TAV', 'TKR', 'TP', 'KGSP', 'GEOMATIKA');
    END IF;
END $$;

-- Add the nis column to the students table
ALTER TABLE students
ADD COLUMN nis INT NOT NULL;

-- Alter the major column to use the new enum type majors
ALTER TABLE students
ALTER COLUMN major TYPE majors
USING major::text::majors;
