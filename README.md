# A1-chatbot
Gen AI 

To create a Python chatbot that verifies updates and categorizes them into different lists, we can use the difflib library to compare text and identify changes. Here's a basic implementation of such a chatbot:

Python

Explanation:
Categorize Changes Function:
Uses difflib.Differ to compare texts and generate a diff.
Categorizes lines into unchanged, simple changes, large changes, and completely new based on diff markers (-, +, ?,  ).
Main Function:
Placeholder old_text and new_text are used for comparison.
Calls categorize_changes to get lists of categorized lines.
Prints categorized changes.
Usage:
Replace old_text and new_text with actual content you want to compare.
Run the script to get categorized differences.
This script provides a simple way to verify and categorize updates. Adjust the categorization logic as needed to fit more specific requirements.
