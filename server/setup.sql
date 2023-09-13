--- TABLE CREATION

CREATE TABLE task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    summary VARCHAR(128),
    description TEXT,
    is_active BOOLEAN DEFAULT 1
);

--- INSERT DUMMY DATA

INSERT INTO task (
    summary, 
    description
) VALUES 
    (
        "Walk the dog",
        "Take the dg to the park for a walk"
    ),
    (
        "Do the dishes",
        "Wash the dishes after dinner"
    ),
    (
        "Wash the car",
        "Take th car to the car wach and wash it"
    );