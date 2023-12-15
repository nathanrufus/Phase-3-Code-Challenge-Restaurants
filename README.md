Phase-3-Code-Challenge-Restaurants

The Restaurant Review System is a Python program that simulates a basic review system for restaurants and customers. It consists of three main classes: Restaurant, Review, and Customer, which work together to manage restaurant reviews and customer information.
Classes
Restaurant class

The Restaurant class represents a restaurant. It has attributes for the restaurant's name and a list of reviews. Additionally, it includes methods to add reviews, retrieve reviews, list customers who reviewed the restaurant, and calculate the average star rating.
Review class

The Review class represents a review. It includes attributes for the customer who wrote the review, the restaurant being reviewed, and the rating given. The review instance is associated with both the customer and the restaurant. This class also includes methods to retrieve rating, customer, and restaurant information.
Customer class

The Customer class represents a customer. It includes attributes for the customer's given name, family name, and a list of reviews they've given. This class provides methods to retrieve customer names, list restaurants they've reviewed, add new reviews, count the number of reviews, and search for customers by name.
Example usage of the Restaurant and Review classes
Creating instances of Restaurant

restaurant1 = Restaurant("Restaurant A") restaurant2 = Restaurant("Restaurant B")
Adding reviews for restaurants

customer1.add_review(restaurant1, 4) customer2.add_review(restaurant2, 5)
Printing restaurant details

print("Restaurant 1:", restaurant1.name) print("Restaurant 1 Reviews:", restaurant1.get_reviews()) print("Restaurant 1 Customers:", restaurant1.get_customers()) print("Restaurant 1 Average Rating:", restaurant1.get_average_star_rating())
