-- Drop table if it exists to start fresh
DROP TABLE IF EXISTS notices;

-- Create the notices table
CREATE TABLE notices (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Insert some test data
INSERT INTO notices (title, content) VALUES
('First Notice', 'This is the content of the first notice.'),
('Second Notice', 'This is the content of the second notice. It has a bit more text to see how it wraps.'),
('Third Notice', 'A third notice has appeared!');