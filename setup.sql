
CREATE TABLE IF NOT EXISTS task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(45),
    description TEXT,
    is_done BOOLEAN DEFAULT 0
);

--Optional (create dummy data)

INSERT INTO task (
    summary,
    description
) VALUES
(
    "walk the dog",
    "take fido out for walk"
),
(
    "wash the car",
    "The car needs washing"
),
(
    "buy groceries",
    "we need milk, tomatoes and bread"
);