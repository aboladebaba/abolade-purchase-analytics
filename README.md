# abolade-purchase-analytics
This work piece contains my submission for the current data challenge. The main script has few annotations to document and quickly remind me of what was going through my mind while writing the code where the annotations were provided. I enjoy writing this script as I encoutered interesting situations where my code almost crashed my 32GB laptop, big thanks to Big O for helping me out with the corrections I needed.
# Abolade's Approach
The key take away for me while writing this entry was efficient data structure and good understanding of the what the challenge requires from each candidate. I found python's dictionaries, lists and tuples as very useful in crafting my solution for the challenge. The net effect was my script was able to complete the exercise with the 3 million dataset in less than a minute on my 2009 Dell Optilex Desktop with 6GB total memory.
* I used dictionaries to create a map of product IDs to frequency of their occurence with the reordered column. I then ran mini aggregations to simplify the complexity and demonstrate my understanding of the task at hand.
* I experimented with many of the available methods and base modules before I selected the experiemnt that gave me the optimal solution.
# Tesing the Approach
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
   
