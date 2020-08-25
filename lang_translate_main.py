# import important packeges.
import matplotlib.pyplot as plt
import pandas as pd
import os
from collections import Counter

def read_book(titile_path):
    """
    Read a book and return it as a  string.
    """
    with open(titile_path, "r", encoding="utf8") as current_file:
        text = current_file.read()
        text = text.replace("\n", "").replace("\r", "")
    return text 

def word_stats(word_counts):
    """"Return number of unique words and word frequencies."""
    num_unique = len(word_counts)
    counts = word_counts.values()
    return (num_unique,counts)

def count_words(text):
    """
    Count the number of times of each word occures in text(str). Return dictionary where keys are unique word
    and values are word counts.Skip puntuations.   
    """
    text = text.lower()
    skips = [".",",",";",":","'",'"']
    for ch in skips:
        text =text.replace(ch,"")
    
    word_counts = Counter(text.split(" "))
    return word_counts


# Source File locations:
book_dir ="./Books"

stats = pd.DataFrame(columns = ("language","author","title","length","unique"))
title_num = 1

for language in os.listdir(book_dir):
    for author in os.listdir(book_dir + "/" + language):
        for title in os.listdir(book_dir + "/" + language + "/" + author):
            inputfile = book_dir + "/" + language + "/" + author + "/" + title # Full path of the book
            print(inputfile) # get the list of all books
            text = read_book(inputfile)
            (num_unique, counts) = word_stats(count_words(text))
            stats.loc[title_num] = language, author.capitalize(), title.replace(".txt",""), sum(counts), num_unique
            title_num += 1  

# Visualize the final ouput
plt.figure(figsize= (10, 10))
subset = stats[stats.language == "English"]
plt.loglog(subset.length, subset.unique, "o", label="English", color="crimson")
subset = stats[stats.language == "French"]
plt.loglog(subset.length, subset.unique, "o", label="French", color="forestgreen")
subset = stats[stats.language == "German"]
plt.loglog(subset.length, subset.unique, "o", label="German", color="orange")
subset = stats[stats.language == "Portuguese"]
plt.loglog(subset.length, subset.unique, "o", label="Portuguese", color="blueviolet")
plt.legend()
plt.xlabel("Book Length")
plt.ylabel("No of unique words")
plt.savefig("lang_plot")

# Get the stats details
print(stats)