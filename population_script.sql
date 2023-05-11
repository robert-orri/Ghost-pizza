INSERT INTO manufacturer_Offer (name, description, price, image) VALUES('Ghost pizza challenge', 'Are you brave enough? Do you think you can handle the heat? Then take on this spooky flaming hot pizza, dont worry, you can cool off with the meat and cheese pizza', 14.99, 'https://media.istockphoto.com/id/1053158242/photo/classic-italian-pizza.jpg?s=612x612&w=0&k=20&c=6mkL3cg8rqxerDjHQCF4z74t2aJoCcaJ9i7n9pZ6E2M=');
INSERT INTO manufacturer_Offer (name, description, price, image) VALUES('Two for one', 'Two pizzas for one? How could you resist', 0.00, 'https://www.pizzahut.ca/_next/static/static/images/menu/pizzas.ca.fb90341bbc44b9fa9d6bd5436edc38a5.jpg');


INSERT INTO pizza_Pizza (name, description, price, category, image) VALUES('Margarita', 'The classic one', 4.99, 'classic', 'https://upload.wikimedia.org/wikipedia/commons/c/c8/Pizza_Margherita_stu_spivack.jpg');
INSERT INTO pizza_Pizza (name, description, price, category, image) VALUES('Pepperoni', 'The better classic one', 6.99, 'classic', 'https://www.dogtownpizza.com/wp-content/uploads/2020/01/picking-slice-of-pepperoni-pizza-picture-id1133727757.jpg');
INSERT INTO pizza_Pizza (name, description, price, category, image) VALUES('Ghost pizza', 'Careful not to get spooked', 9.99, 'special', 'https://hips.hearstapps.com/hmg-prod/images/wdy060120pizza-003-1590688915.jpg?crop=0.561xw:0.843xh;0.351xw,0&resize=1200:*');
INSERT INTO pizza_Pizza (name, description, price, category, image) VALUES('Hawaii', 'A delicious goodness that you have to hide from your president', 6.99, 'treason', 'https://www.allrecipes.com/thmb/v1Xi2wtebK1sZwSJitdV4MGKl1c=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/hawaiian-pizza-ddmfs-3x2-132-450eff04ad924d9a9eae98ca44e3f988.jpg');
INSERT INTO pizza_Pizza (name, description, price, category, image) VALUES('Calsone', 'Is that even a pizza?', 8.99, 'special', 'https://thecozyapron.com/wp-content/uploads/2021/01/calzone_thecozyapron_1.jpg');
INSERT INTO pizza_Pizza (name, description, price, category, image) VALUES('Cheese and meat', 'You love meat? This is for you then', 9.99, 'special', 'https://www.dominos.is/media/jdilajxj/dom_vef_3750x2500_meatandcheese_0619.jpg');

INSERT INTO ingredient_Ingredient (name) VALUES('cheese');
INSERT INTO ingredient_Ingredient (name) VALUES('pepperoni')
INSERT INTO ingredient_Ingredient (name) VALUES('beef');
INSERT INTO ingredient_Ingredient (name) VALUES('bacon');
INSERT INTO ingredient_Ingredient (name) VALUES('ghost pepper');
INSERT INTO ingredient_Ingredient (name) VALUES('chilli');
INSERT INTO ingredient_Ingredient (name) VALUES('pineapple');
INSERT INTO ingredient_Ingredient (name) VALUES('ham');
INSERT INTO ingredient_Ingredient (name) VALUES('cream cheese');

INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(1, 1);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(2, 1);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(2, 2);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(3, 1);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(3, 2);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(3, 5);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(3, 6);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(3, 9);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(4, 1);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(4, 8);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(4, 7);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(5, 1);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(5, 2);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(5, 3);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(5, 4);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(5, 8);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(5, 9);

INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(6, 1);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(6, 2);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(6, 3);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(6, 4);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(6, 8);
INSERT INTO pizzas_PizzaIngredient (pizzas_id, Ingredient_id) VALUES(6, 9);