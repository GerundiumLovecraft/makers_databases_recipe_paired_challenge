DROP TABLE IF EXISTS recipe_to_ingredients;
DROP TABLE IF EXISTS ingredients;
DROP TABLE IF EXISTS recipes;

CREATE TABLE recipes(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    recipe TEXT NOT NULL,
    cooking_time SMALLINT CHECK (cooking_time > 0),
    rating SMALLINT CHECK (rating BETWEEN 1 AND 5)
);

CREATE TABLE ingredients(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    spiciness SMALLINT CHECK (spiciness BETWEEN 1 AND 5)
);

CREATE TABLE recipe_to_ingredients(
    recipe_id INT,
    ingredient_id INT,
    amount INT NOT NULL CHECK (amount > 0),
    unit VARCHAR(10),
    constraint fk_recipe foreign key(recipe_id)
    references recipes(id)
    on delete cascade,
    constraint fk_ingredient foreign key(recipe_id)
    references ingredients(id)
    on delete cascade,
    PRIMARY KEY(recipe_id, ingredient_id)
);

INSERT INTO ingredients (name, spiciness) VALUES
('Chicken Breast', 1),
('Red Chili', 5),
('Garlic', 2),
('Coconut Milk', 1),
('Pasta', 1),
('Parmesan Cheese', 1),
('Black Pepper', 2),
('Cumin', 3);

INSERT INTO recipes (name, recipe, cooking_time, rating) VALUES
('Spicy Chili Chicken', 'Sauté chicken with minced red chilis and garlic.', 30, 5),
('Creamy Garlic Pasta', 'Boil pasta and toss with garlic and parmesan.', 20, 4),
('Coconut Curry', 'Simmer chicken in coconut milk with cumin and spices.', 45, 5),
('Simple Pepper Pasta', 'Toss pasta with olive oil and heavy black pepper.', 15, 3),
('Garlic Roasted Chicken', 'Slow roast chicken with cloves of garlic.', 60, 4);

INSERT INTO recipe_to_ingredients (recipe_id, ingredient_id, amount, unit) VALUES
-- Spicy Chili Chicken (Recipe 1)
(1, 1, 500, 'g'),   -- Chicken
(1, 2, 3, 'pcs'),   -- Red Chili
(1, 3, 4, 'cloves'),-- Garlic

-- Creamy Garlic Pasta (Recipe 2)
(2, 5, 200, 'g'),   -- Pasta
(2, 3, 2, 'cloves'),-- Garlic
(2, 6, 50, 'g'),    -- Parmesan

-- Coconut Curry (Recipe 3)
(3, 4, 400, 'ml'),  -- Coconut Milk
(3, 1, 400, 'g'),   -- Chicken
(3, 8, 2, 'tsp'),   -- Cumin

-- Simple Pepper Pasta (Recipe 4)
(4, 5, 200, 'g'),   -- Pasta
(4, 7, 1, 'tbsp'),  -- Black Pepper

-- Garlic Roasted Chicken (Recipe 5)
(5, 1, 1, 'kg'),    -- Chicken
(5, 3, 10, 'cloves');-- Garlic