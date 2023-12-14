# prime_numbers
Python Flask project to calculate Prime Numbers 
#### Video Demo: https://youtu.be/TNXI1zphr9s
#### Description:
A website project about Prime Number 
Feature :
1. Generate Prime Number in specific range,
2. Check a number is prime number or not,
3. Summarize Prime Number in specific range,
4. Visualize thedistribution of Prime Number in specific range.

TODO :

project.py file contains:
  1. prime_selector Function to generate prime number in specific range,
  2. is_prime Function to define a number is a prime number or not
  3. sum_primes Function to summerize all prime number in range up to the given limit
  4. menu Function if user want to use in CLI mode, It's display different options based on user choice based on three function above
     
test_project.py file contains:
  1. test_prime_selector to test prime_selector Function
  2. test_is_prime to test is_prime Function
  3. test_sum_primes to sum_primes Function

app.py file contains : command to route for Flask website base on project.py  and helper.py file

helper.py file contains :
  1. primes_to_dataframe Function to generate a DataFrame with prime numbers in the given range.
  2. generate_html Function to Generate an HTML representation of a DataFrame with styling.
  3. distribution Function to  Display a bar chart showing the distribution of prime numbers.
  4. distr_his Function to Display a histogram showing the distribution of prime numbers.
  5. patern Function to Display a scatter plot showing the pattern of prime numbers.
  6. apology Function to Render message as an apology to user.


