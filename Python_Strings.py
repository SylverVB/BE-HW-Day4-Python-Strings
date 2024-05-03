# Lesson 6: Assignments | Python Strings

# 1. Product Review Analysis

# Objective: The aim of this assignment is to extract insights from product reviews by using 
# string manipulation to categorize and summarize customer feedback for a SaaS product.

# Task 1: Keyword Highlighter

# Write a program that searches through a series of product reviews for keywords such as 
# "good", "excellent", "bad", "poor", and "average". Print out each review with the keywords 
# in uppercase so they stand out.

reviews = [ "This product is really good. I'm impressed with its quality.", 
                  "The performance of this product is excellent. Highly recommended!", 
                  "I had a bad experience with this product. It didn't meet my expectations.", 
                  "Poor quality product. Wouldn't recommend it to anyone.", 
                  "The product was average. Nothing extraordinary about it." ]
keywords = ["good", "excellent", "bad", "poor", "average"]


for review in reviews:
    for keyword in keywords:
        review = review.replace(keyword, keyword.upper())
        review = review.replace(keyword.title(), keyword.upper())
    print(review)

# Task 2: Sentiment Tally

# Develop a function that tallies the number of positive and negative words in each review. 
# Use a predefined list of positive and negative words to check against. 
# The function should return the count of positive and negative words for each review.

positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"] 
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

positive = 0
negative = 0

for review in reviews:
    lower_review = review.lower()
    for pos_word in positive_words:
        if pos_word in lower_review:
            positive += 1
print(positive)

for review in reviews:
    lower_review = review.lower()
    for neg_word in negative_words:
        if neg_word in lower_review:
            negative += 1
print(negative)

# Task 3: Review Summary

# Implement a script that takes the first 30 characters of a review and appends "…" to create a summary. 
# Ensure that the summary does not cut off in the middle of a word.

summaries = []

for review in reviews:
    if len(review) <= 30:
        summaries.append(review)
    else:
        short_review = review[:30]
        last_space_index = short_review.rfind(' ')
        print(last_space_index)
        if last_space_index != -1:                           # If the space was found:
            short_review = short_review[:last_space_index]
            summaries.append(short_review + "...")

# Option 1.
print(summaries)

# Option 2.
for summary in summaries:
    print(summary)

         
# 2. User Input Data Processor

# Task 1: Input Length Validator. Write a script that checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")

if len(first_name) >= 2:
    if len(last_name) >= 2:
        print(f'The length of your first name is: {len(first_name)}')
        print(f'The length of your last name is: {len(last_name)}')
else:
    print(f"You entered {first_name} {last_name}. Both your first and last name should be at least 2 characters long. " 
          "Try again.")