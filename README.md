# Introduction
In this work piece, I share my solution to the current data challenge. The main script has few annotations to document and quickly remind me of what was going through my mind while writing the code where the annotations were provided. I enjoy writing this code because I encoutered interesting situations where my code almost crashed my 32GB laptop, big thanks to Big O notation for helping me figure out where in my code lies the problem.

# Abolade's Approach
The key take away for me while writing this code was efficient data structure and good understanding of the what the challenge requires from each candidate. I found python's dictionaries, lists and tuples very useful in crafting my solution to the challenge. The net effect was my script was able to complete the exercise and return required results within a reasonable.
* I used dictionaries to create a map of `product_ids` to frequencies of their occurence using `reordered` column of `order_products.csv` file. This greatly reduced the amount of computation (in this case looping) required and simplified indexing of my intermediate datasets  create required aggregations. With this approach, I was able to simplify the complexity of the challenge and demonstrate my understanding of the tasks at hand.
* Using dictionaries also made it easier for me to aggregate information contained in my two dictionaries and extract the requesting `department_id` from the product dict for the final `report.csv` file.
* I experimented with many of the available methods and base modules before I selected the experiemnt that gave me the optimal solution.

# Testing
While writing the code, I had two to three hypothesis about the data and the descriptions the chanllenge provided. I shared one of such as a comment in the code regarding `product_id` mapping to `department_id`. I found the supplied test scipt sufficient and adequate for covering test cases for the challenge. 
Here is what my final directory stucture looked like:

    ├── README.md 
    ├── run.sh
    ├── src
    │   └── purchase_analytics.py
    ├── input
    │   └── order_products.csv
    │   └── products.csv
    ├── output
    |   └── report.csv
    ├── insight_testsuite
        └── run_tests.sh
        └── tests
            └── test_1
            |   ├── input
            |   │   └── order_products.csv
            |   │   └── products.csv
            |   |__ output
            |   │   └── report.csv
            ├── abolade_test_1
                ├── input
                │   └── order_products.csv
                |   └── products.csv
                |── output
                    └── report.csv
   
