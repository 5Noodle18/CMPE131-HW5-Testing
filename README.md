# Homework 
- Name: Bryan D. Morales Sosa
## Question 1) Define the following: Unit, integration and regression tests. When you would use each?
- **Unit test**: A test that aims to evaluate a singular, arbitrarily-defined unit of code (like a method function).
  - *When to Use*: When you create a helper method for a data type, like checkout() for a ShoppingCart Object. You would want to check if the shopping cart empties and balance withdrawn from a user.
- **Integration test**: This is a combination of two (or more) units of code to test and see if they can function as intended together when both are implemented.
  - *When to Use*: Suppose I continue from the previous example, and I want to add a CreditCard Object that ShoppingCart.checkout() will reference to subtract the balance from.
I want to see if my CreditCard and my ShoppingCart won't break any logic when I use them both in my application.
- **Regression test**: This is a re-iteration of previous unit tests to evaluate if new work/code has unintentionally affected old functionalities, i.e. regress the code.
  - *When to Use*: Suppose I add a DEAL data type that modifies item values to reflect discounts. I should test to see if that has affected functionalities like .addAll(). For example,
  .addAll() found too many arguments or now is being passed an unexpected type, etc. 
## Question 2) Briefly explain pytest discovery (file/function naming) and what a fixture is.
- Pytest discovery is the process pytest uses to find files or functions in order to test them using its operations. By convention:
  - Files: searches for files with format test_*.py or *_test.py
  - Functions: begins with the prefix test_<> (like test_checkout())
- Fixtures are the processes that are called to manage pre and post conditions. This is to make testing environments modular and easy to implement.
Fixtures are the technical equivalent of setting up a lab with equipment, and after the test is concluded, dismantling projects and putting everything away.
