#!/usr/bin/env python3

# Standard library imports
from random import randint, choice as rc

# Local imports
from app import app
from models import db, Recipe, User, Category, Category_recipe

with app.app_context():
    db.drop_all()
    db.create_all()

    #List of categories
    category_data = [
        {"category": "Appetizers"}
    ]

    def seed_categories():
        for data in category_data:
            category = Category(**data)
            db.session.add(category)

        db.session.commit()

    category_recipe_data = [
        {"category_id": 1, "recipe_id": 1}
    ]

    def seed_category_recipes():
        for data in category_recipe_data:
            category_recipe = Category_recipe(**data)
            db.session.add(category_recipe)
        
        db.session.commit()
    
    recipe_data = [
        {"user_id": "1", 
         
         "title": "Agedashi Tofu", 

         "picture": "", 

         "ingredients": """1 block medium-firm or firm tofu (1 pound) \n
         1 heaped tablespoon cornstarch\n
         1 heaped tablespoon tapioca starch\n
         1 heaped tablespoon flour\n
         ¼ teaspoon salt\n
         3-4 cups neutral-flavored oil for frying (vegetable, canola, etc)\n

         Sauce:\n
         1 cup dashi stock (use kombu dashi for vegetarian/vegan)\n
         2 Tbsp soy sauce\n
         2 Tbsp mirin\n
         Optional: 1 garlic clove halved\n
         Optional: ½ inch of ginger\n
         Optional: 2 inches kombu\n

         Toppings:\n
         1 daikon radish (1 daikon = 2.5 cm) (optional)\n
         2 green onion/scallion - green and light green parts only.\n
         ½ cup Katsuobushi (dried bonito flakes) (optional, and skip if vegetarian)\n
         Shichimi Togarashi (Japanese seven spice) (optional)\n""",

         "preparation": """Wrap the tofu with 3 layers of paper towels and place another plate on top. Drain the water out of tofu for 30-60 minutes.\n
         Mix the flour and the starches.\n
         Peel and grate the daikon and gently squeeze water out. Cut the green onion into thin slices. Dice the bonito flakes.\n
         Put all sauce ingredients - dashi, soy sauce, and mirin in a small saucepan and bring to a boil. Turn off the heat and set aside.\n
         Remove the tofu from paper towels and cut it into 6 blocks and then cut each block to 4. Total 24 pieces.\n
         Heat the oil to 350F (175C) in a deep fryer or medium saucepan. Work in two batches. Coat the tofu with flour mix, leaving excess flour, and immediately deep fry until they turn light brown and crispy. Turn if oil doesn’t cover, should take about 3-4 minutes.\n
         Remove the tofu and drain excess oil on the wire rack.\n
         5 minutes before serving, heat the oil to 375 f, move all the tofu to the pan in one layer, turning once and move to the wire rack. Should take 2-3 minutes.\n
         To serve, place the tofu in a serving bowl and gently pour the sauce without wetting the tofu. Garnish with grated daikon, green onion, katsuobushi, and shichimi togarashi.\n""", 
         "tips": "", 
         "reviews": ""
         }
    ]

    def seed_recipes():
        for data in recipe_data:
            recipe = Recipe(**data)
            db.session.add(recipe)

        db.session.commit()

    user_data = [
        {"username": "Chuchu", "password": "mayolover"}
    ]

    def seed_users():
        for data in user_data:
            user = User(**data)
            db.session.add(user)
        
        db.session.commit()
    
    def seed():
        seed_categories()
        seed_category_recipes()
        seed_recipes()
        seed_users()
    
    seed()
    print('Categories, category_recipes, recipes, and users Seeded!')

    