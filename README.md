Reddit Rambler – JSON data extractor
Time to complete 30 minutes.
Introduction
The Reddit Rambler script is designed to process JSON files obtained from Reddit, typically containing data related to posts, comments, and other associated metadata. The script extracts detailed information about each post, including the title, content, and any associated comments and replies. The extracted data is then saved into organized text files for easy review.
The script performs several tasks:
1.	The script scans its directory for .JSON files and processes each one to extract key data, such as post titles, content, comments, and replies.
2.	It removes weblinks from the text to prevent interference with word frequency analysis.
3.	Usernames are pseudonymized but consistent across all processed files, allowing user tracking within the same batch.
4.	Polarity, Subjectivity, and Sentiment analysis can be performed using the TextBlob library.
5.	A list of common words is used to filter out unnecessary words.
6.	Word frequencies are counted and saved in two CSV files: "common_words" for words on a predefined list, and "other_frequencies" for all other words.
7.	A CSV file is generated for analyzing post timing (day and time) for further processing or heatmap creation.
8.	All posts, comments, and replies are also saved as CSV files.
9.	You can visualize your data as a word cloud or heat map.
To use the app, you will need to extract each post of interest from reddit in JSON file format. Instructions on how to do this here. You can process more than one JSON file at once. Then you just run the application and select the folder containing the JSONs, and the common words list for filtering (default provided in zip file). 
Figure 1. Screenshot of the Reddit Rambler
 
 
Disclaimer
The Reddit Rambler software is provided "as is" for educational and research purposes, primarily aimed at supporting students and academics in their research efforts. The developer makes no guarantees regarding the accuracy, reliability, or suitability of the software for any specific research projects.
By using this software, you acknowledge and agree that:
1.	Responsibility for Research: The developer is not responsible for the outcomes, validity, or integrity of any research conducted using this software. Users are solely responsible for ensuring that their work complies with academic standards, ethical guidelines, and applicable laws.
2.	Software Availability: The availability of the Reddit Rambler software is not guaranteed. The software may be removed or discontinued at any time without prior notice. Users should not rely on its continuous availability for their research needs.
3.	Development and Support: Ongoing development or technical support for the software is not guaranteed. The developer may choose to update, modify, or cease development of the software at any time. Users should not expect regular updates or dedicated support.
The developer disclaims all liability for any damages, losses, or issues arising from the use of the software, including but not limited to data loss, inaccuracies in research, or any other negative outcomes. Users are advised to use the software with caution and to independently verify any results produced using the tool. 
Contents
Introduction	1
Disclaimer	2
AI Statement	5
Getting JSON Files	5
Running Reddit Rambler	7
Common_Word_Frequencies CSV	8
Other_Word_Frequencies CSV	8
Heatmap_Data CSV	8
Reddit_Posts CSV	8
TextBlob	9
Polarity	9
Subjectivity	9
Sentiment	10
Visualisations	10
Word Cloud	10
Heat Map	11
Visualisation Options	11
Troubleshooting	11
Error When Loading JSON Files	11
Common Words File Not Found	11
GUI Freezes or Becomes Unresponsive	11
Sentiment Analysis Results Seem Inaccurate	12
Anonymized Usernames Are Inconsistent Across Files	12
Error Message: “Failed to Save Files”	12
The Application Crashes During Processing	12
Future development	12
Licence	12
Why the MIT License?	13
Libraries	13
References	15
Glossary of Terms	16
Appendix A	17
Appendix B	32

 
AI Statement
This app and supporting documents have been made with the help with artificial intelligence.
Getting JSON Files
•	Go to Reddit.com: Reddit - Dive into anything
•	Search for the subreddit/posts you are interested in and open the post.
•	Once the post has loaded click on the URL bar in the browser and add .json to the end of the text and hit return: 
 
•	This will convert the webpage into a JSON file (a standard text-based format for representing structured data based on JavaScript object syntax): 
 
•	You need to save the page by using the keyboard shortcut CTRL + S: 
 
•	Navigate to where you want to store the JSON file. I suggest creating a new folder and label it something useful like the date or topic etc. 
•	Then give the file a useful name, in the picture below I have used example, use something you know will be useful in identifying the data:
 
•	Double check that the Save as type is set to JSON, sometimes browsers will try and force different file types. In those instances, set the Save As type to All Files and add. json to the end of your filename: 
 
•	Click Save do this for each post you want to analyse.
Running Reddit Rambler
•	Double click the app.
 
•	Click Browse to the right of the Select JSON Directory and select the folder that is containing all the JSON Files you want to process.
•	Click the Browse button to the right of the Select Common Words file.
•	You should have received a copy of the default common words list with when you downloaded the app. If not, you can create one easily by creating a blank text document (must be .txt, not .docx or any other text document), name it whatever you like. Click browse and select the common words file. You can click the Edit button to add or remove words you want to filter out of the analysis. 
•	Next select if you want to include TextBlob analysis, for more information on TextBlob go to: TextBlob: Simplified Text Processing — TextBlob 0.18.0.post0 documentation.
•	Then click Start Processing.
•	Once processing has completed you will receive a message box indicating what has been undertook:
 
•	The app will also open the folder with all the processed data within: 
 
Common_Word_Frequencies CSV
This file contains three columns:
1.	Word: This is a list of individual words that were found in the posts that are contained in the Common_Words list (Appendix B).
2.	Frequency: This the number of times that word is present in the processed data.
3.	Type: The type of word, be it common (words filtered out of the data), or other, words retained in the data.  
Other_Word_Frequencies CSV
This file contains three columns:
1.	Word: This is a list of words present in the posts, comments and replies after the common_words have been filtered out.
2.	Frequency: This the number of times that word is present in the processed data.
3.	Type: The type of word, be it common (words filtered out of the data), or other, words retained in the data.  
Heatmap_Data CSV
This file contains three columns:
1.	Day: indicates the day of the week with 0 representing Monday, 6 representing Sunday.
2.	Hour: 24-hour time, e.g. 1 = 1am, 23 = 11pm
3.	Frequency: the number of posts made during that time and hour.  
Reddit_Posts CSV
This file contains 5 compulsory columns and 3 optional:
Compulsory
1.	Comment/Reply: whether the extracted text was either a comment or reply.
2.	Username: Automatically anonymised usernames that remain consistent across posts if you want to track a single user across several different posts. Anonymisation cannot be undone. Nor will the option to not anonymise users be added so don’t ask.
3.	Text: the extracted text. Due to some issues with encoding text some anomalies will occur, especially if the comment or reply contains an emoji.
4.	Timestamp: date and time the comment/reply was made (dd/mm/yyyy, hh:mm).
5.	Source File: from which JSON file the text was extracted.
Optional:
6.	Polarity: measures the sentiment expressed in the comment/reply. It is a numerical value ranging from -1 (very negative) to 1 (very positive).
7.	Subjectivity: a numerical value ranging from 0 (completely objective) to 1 (completely subjective), higher subjectivity reflects the presence of personal opinions, or beliefs in the text.
8.	Sentiment: A combination of a statement’s subjectivity and polarity values that describes the sentiment of the text (positive, neutral, or negative). 
TextBlob
TextBlob is a simple and easy-to-use Python library for processing textual data. It provides a convenient interface for performing common natural language processing (NLP) tasks and is especially useful for quick sentiment analysis using a lexicon-based approach, which calculates polarity and subjectivity scores for text. For more information: TextBlob: Simplified Text Processing
Polarity 
A measure of the sentiment expressed in a text, ranging from -1 (very negative) to 1 (very positive). TextBlob calculates polarity by leveraging a pre-built lexicon of words, where each word has an associated polarity score.
Here’s how it works:
Lexicon-Based Approach: TextBlob uses a dictionary of words, each annotated with polarity scores. For instance, the word "good" might have a polarity of 0.7, while "bad" might have a polarity of -0.7.
Calculating Sentence Polarity: TextBlob parses the text into sentences and assigns a polarity score to each sentence by averaging the polarity of the words within it.
Averaging for Final Polarity: If analyzing multiple sentences, TextBlob will take the average of the individual sentence polarity scores to produce an overall polarity score for the entire text.
Example:
Sentence: "I love this product, but the packaging is terrible."
Polarity for "love": +0.5 (positive)
Polarity for "terrible": -0.8 (negative)
Overall sentence polarity might average out to around -0.15 (slightly negative).
Subjectivity
Subjectivity is a measure of how subjective or objective the text is. It ranges from 0 (completely objective) to 1 (completely subjective). Subjectivity reflects the presence of personal opinions, feelings, or beliefs in the text.
Here’s how it works:
Lexicon-Based Approach: Similar to polarity, TextBlob uses a dictionary where words are annotated with subjectivity scores. Words that convey strong opinions or emotions (e.g., "amazing," "horrible") are assigned higher subjectivity scores, while neutral words (e.g., "fact," "number") are assigned lower scores.
Sentence Subjectivity Calculation: The subjectivity score of a sentence is computed by averaging the subjectivity scores of the words within it.
Overall Subjectivity: For multiple sentences, the overall subjectivity score is the average of the individual sentence scores.
Example:
Sentence: "This cake is delicious."
"Delicious" might have a subjectivity score of 0.9, making the sentence highly subjective.
Sentiment
When people refer to sentimentality in the context of TextBlob, they are usually referring to the combination of polarity and subjectivity that describes the sentiment of the text. The sentiment attribute in TextBlob gives you both the polarity and subjectivity of a text.
Here’s how TextBlob processes sentimentality:
TextBlob.sentiment: When you call TextBlob.sentiment on a text, it returns a Sentiment namedtuple with two values: polarity and subjectivity.
Visualisations
This app currently offers two forms of visualisations that can be run after JSON data has been processed.  
Word Cloud
 
A word cloud is a visual representation of text data where the size of each word indicates its frequency or importance in the dataset. Commonly used in text analysis, word clouds help to quickly identify the most prominent words in a body of text, with larger, bolder words appearing more frequently or being more significant. This visualization is often used to summarize large amounts of text data, making key themes or topics easy to identify briefly.
To create a word cloud, process the JSON files you are working with, then click on the WordCloud button and select which of the frequency (either other or common) files from the analysis by clicking and click OK. 
Word Cloud Hints and Tips
1.	Using “Common Words” to isolate or filter specific words. You could use a common words file to track the frequency of specific words you are interested in, instead of how it was originally intended, to filter out common high frequency words such as conjunctive like “and”. 
2.	If you find in your frequency file some words that you are not appropriate e.g. “for” in the example above, you could either:
a.	add for to the common words file.
b.	open the data file (for example in Excel) and delete the line containing the For frequency.
In the interest of data preservation, the first option is preferable. 
Heat Map
The Heat Map illustrates when posts, comments, and replies are made by day and hour in a grid-like visual representation where each cell corresponds to a specific hour of the day and a specific day of the week. The colour intensity of each cell indicates the frequency or volume of activity (posts, comments, replies) during that time slot.
To create a heat map, process the JSON files you are working with, then click on the Heat Map button and select the heat map data file.  
Visualisation Options
When a visualisation has been produced you can save the figure and edit certain visual features using some of the options available at the bottom of the visualisation window:
 
a)	Reset: this will return the visualization to its default appearance on generation. 
b)	Move: move the figure within the viewing window.
c)	Zoom: click and drag on the visualisation to focus not a specific area of the figure. 
d)	Configure subplots: use to adjust some of the parameters of the visualisation.
e)	Save: use this to save the figure.
Troubleshooting
Error When Loading JSON Files
•	Possible Cause: The JSON file might be improperly formatted or corrupted.
•	Solution: Double-check that the JSON file is correctly downloaded from Reddit. Follow the steps in the "Getting JSON Files" section to ensure the file is saved properly. If the problem persists, try opening the JSON file in a text editor to check for any obvious issues like incomplete data or syntax errors.
Common Words File Not Found
•	Possible Cause: Incorrect file path or missing file.
•	Solution: Ensure that the common words file is in the correct location and that the file path is correctly entered in the application. If you don’t have a common words file, you can create one as described in the support document.
GUI Freezes or Becomes Unresponsive
•	Possible Cause: Processing large JSON files or running intensive operations without sufficient system resources.
•	Solution: Ensure that your computer meets the system requirements to handle large files. Try processing smaller batches of JSON files. If the problem persists, consider optimizing the JSON files or running the process in a more powerful environment.
Sentiment Analysis Results Seem Inaccurate
•	Possible Cause: Limitations of the TextBlob library or text processing issues.
•	Solution:
o	Understand that TextBlob uses a lexicon-based approach, which may not always perfectly capture the sentiment of complex sentences or specialized language.
o	If you require more accurate sentiment analysis, consider using more advanced NLP tools or preprocessing the text data to better fit the sentiment model.
Anonymized Usernames Are Inconsistent Across Files
•	Possible Cause: Inconsistent salting or incorrect processing.
•	Solution: Ensure that the same salt value is used for pseudonymizing usernames across all processing sessions. The salt should remain consistent unless you intentionally want different pseudonyms across files.
Error Message: “Failed to Save Files”
•	Possible Cause: Insufficient write permissions, incorrect file path, or file is currently in use.
•	Solution:
o	Check that the output folder is accessible and that you have write permissions.
o	Ensure that the file paths are correct and that no other applications are using the file.
o	Try running the application as an administrator if permissions are an issue.
The Application Crashes During Processing
•	Possible Cause: Large data files, memory limitations, or unhandled exceptions.
•	Solution:
o	Try processing smaller batches of JSON files to reduce memory load.
o	Ensure that your system has sufficient resources to handle large datasets.
o	Update your system’s Python and library installations to the latest versions to benefit from bug fixes and performance improvements.
Future development
This app will continue to be developed whilst there is interest in its use, the methodology remains viable or that there is not a suitable freely available alternative. A copy of all materials have been uploaded to github: casparwynne/RedditRambler: A small flexible app that can extract data from JSON files taken from Reddit. (github.com)
Licence
MIT License
Copyright © 2024 Caspar Wynne
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
For more information: The MIT License – Open Source Initiative
Why the MIT License?
The MIT License was chosen for this project because it offers simplicity and clarity, ensuring that users and contributors can easily understand their rights. It allows others to freely contribute, copy, modify, and distribute the software without legal concerns, fostering a collaborative open-source community. Additionally, it provides protection for the author, reducing the risk of legal issues related to the software's use.
Libraries
The following python libraries were used in this project:
This project leverages several Python libraries to perform various tasks, ranging from data processing to GUI development and visualization. Below is a brief overview of each library and its role in the project:
1. os
Purpose: Provides a way to interact with the operating system. 
Usage: Used to handle file and directory operations such as listing files, creating directories, and working with file paths.

2. json
Purpose: Enables working with JSON (JavaScript Object Notation) data in Python.
Usage: Used to load and parse JSON files that contain Reddit data.

3. hashlib
Purpose: Provides a suite of secure hash functions.
Usage: Used to pseudonymize usernames by generating a unique hash for each username.

4. datetime
Purpose: Supplies classes for manipulating dates and times.
Usage: Used to convert and format timestamps from Reddit data, as well as for generating timestamps in filenames.

5. re
Purpose: Offers powerful tools for searching and manipulating strings.
Usage: Used to remove weblinks from text and to find words in the text for frequency analysis.

6. csv
Purpose: Facilitates reading from and writing to CSV (Comma-Separated Values) files.
Usage: Used to save word frequencies, posts data, and heat map data into CSV files.

7. collections
Purpose: Provides specialized data structures, such as counters and default dictionaries.
Usage: Used to count word frequencies and manage user data efficiently.

8. tkinter
Purpose: A standard GUI (Graphical User Interface) toolkit in Python.
Usage: Used to create the application's GUI, allowing users to interact with the software through a visual interface.

9. subprocess
Purpose: Allows spawning of new processes, connecting to their input/output/error pipes, and obtaining their return codes.
Usage: Used to open files for editing in external applications (e.g., Notepad).

10. TextBlob: Simplified Text Processing
Purpose: A library for processing textual data.
Usage: Used for sentiment analysis, providing polarity and subjectivity scores for Reddit comments and replies.

11. wordcloud · PyPI
Purpose: Generates word clouds from text data.
Usage: Used to create visual representations of word frequencies, where the size of each word reflects its frequency.

12. seaborn (Waskom, 2021)
Purpose: A data visualization library based on Matplotlib, providing a high-level interface for drawing attractive and informative statistical graphics.
Usage: Used to create the heat map visualization of activity by hour and day.

13. matplotlib (Hunter, 2007)
Purpose: A comprehensive library for creating static, animated, and interactive visualizations in Python.
Usage: Used in conjunction with Seaborn to plot the heat map and display the word cloud.

14. webbrowser
 Purpose: Provides a high-level interface to allow displaying Web-based documents to users.
 Usage: Used to open URLs in a web browser, such as linking to the project's README file.
References
Hunter, J. D. (2007). Matplotlib: A 2D Graphics Environment. https://ieeexplore.ieee.org/document/4160265/
Waskom, M. L. (2021). seaborn: Statistical data visualization. Journal of Open Source Software, 6(60), 3021. https://doi.org/10.21105/joss.03021

 
Glossary of Terms
JSON (JavaScript Object Notation): A lightweight data-interchange format that is easy for humans to read and write and easy for machines to parse and generate. It is commonly used for transmitting data in web applications.
GUI (Graphical User Interface): A visual interface that allows users to interact with software using graphical elements like buttons, menus, and icons, rather than text-based commands.
Word Cloud: A visual representation of text data where the size of each word indicates its frequency or importance in the dataset. It helps to quickly identify the most prominent words in a body of text.
Heat Map: A data visualization that shows the frequency or volume of activity in different areas of a dataset. In this context, it represents the timing of Reddit posts, comments, and replies, with color intensity indicating activity levels.
Polarity: A measure of the sentiment expressed in a text, ranging from -1 (very negative) to 1 (very positive). Polarity is calculated using natural language processing tools like TextBlob.
Subjectivity: A measure of how subjective or objective a text is, ranging from 0 (completely objective) to 1 (completely subjective). Higher subjectivity indicates a greater presence of personal opinions or feelings in the text.
Sentiment: A combination of a text's polarity and subjectivity that describes its overall emotional tone, categorized as positive, neutral, or negative.
TextBlob: A Python library used for processing textual data. It provides tools for common natural language processing tasks, including sentiment analysis, which involves determining the polarity and subjectivity of a text.
Common Words: In this context, a predefined list of frequently occurring words that are filtered out during word frequency analysis to focus on more significant terms.
Pseudonymize: The process of replacing private identifiers with fictitious names or codes to protect the privacy of individuals. In this project, usernames are pseudonymized to ensure user anonymity.
CSV (Comma-Separated Values): A file format used to store tabular data, where each line represents a row in the table, and fields within the row are separated by commas.
Lexicon-Based Approach: A method used in natural language processing where words in a text are matched against a predefined dictionary (lexicon) of words with assigned sentiment or subjectivity scores.
Open-Source: A type of software where the source code is made freely available for anyone to view, modify, and distribute.
MIT License: A permissive open-source license that allows users to freely use, modify, and distribute the software with minimal restrictions, while also providing legal protection to the author.
 
Appendix A
Complete copy of code from version 1. 
import os
import json
import hashlib
from datetime import datetime, timezone
import re
import csv
from collections import Counter, defaultdict
import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
from textblob import TextBlob
from wordcloud import WordCloud
import seaborn as sns
import matplotlib.pyplot as plt
import webbrowser  # To open the hyperlink in a web browser

# Global variables
output_folder = ""
all_posts_data = []

# Function to load common words from an external .txt file
def load_common_words(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            common_words = set(word.strip().lower() for word in file.readlines())
        return common_words
    except Exception as e:
        messagebox.showerror("Error", f"Error loading common words from file: {str(e)}")
        return set()

# Function to pseudonymize the username
def pseudonymize_username(username, salt="reddit_pseudonym_salt"):
    hash_object = hashlib.sha256((salt + username).encode())
    return "user_" + hash_object.hexdigest()[:8]

# Function to remove weblinks from text
def remove_weblinks(text):
    return re.sub(r'http\S+|www\S+', '', text, flags=re.MULTILINE)

# Function to process a single JSON file
def process_json_file(file_path, common_words, include_polarity, include_subjectivity, include_sentiment, source_file):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            reddit_data = json.load(file)

        user_data = defaultdict(lambda: {"count": 0, "posts": 0, "comments": 0, "replies": 0})
        total_posts = 0
        combined_text = ""

        posts_data = []
        post = reddit_data[0]['data']['children'][0]['data']

        title = remove_weblinks(post.get('title', 'No Title'))
        content = remove_weblinks(post.get('selftext', 'No Content'))
        comments_data = reddit_data[1]['data']['children']

        combined_text += f"{title} {content} "
        total_posts += 1

        for comment in comments_data:
            comment_data = comment['data']
            user = pseudonymize_username(comment_data.get('author', '[deleted]'))
            body = remove_weblinks(comment_data.get('body', '[deleted]'))

            polarity, subjectivity, sentiment = None, None, None

            if include_polarity or include_subjectivity or include_sentiment:
                blob = TextBlob(body)
                if include_polarity:
                    polarity = round(blob.sentiment.polarity, 2)
                if include_subjectivity:
                    subjectivity = round(blob.sentiment.subjectivity, 2)
                if include_sentiment:
                    sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"

            user_data[user]["count"] += 1
            user_data[user]["comments"] += 1

            combined_text += f"{body} "
            posts_data.append({
                "Comment/Reply": "Comment",
                "Username": user,
                "Text": body,
                "Polarity": polarity,
                "Subjectivity": subjectivity,
                "Sentiment": sentiment,
                "Timestamp": datetime.fromtimestamp(comment_data.get('created_utc', 0), timezone.utc).strftime('%Y-%m-%d %H:%M:%S'),
                "Source File": source_file
            })

            if 'replies' in comment_data and comment_data['replies']:
                replies_data = comment_data['replies']['data']['children']
                for reply in replies_data:
                    reply_data = reply['data']
                    reply_user = pseudonymize_username(reply_data.get('author', '[deleted]'))
                    reply_body = remove_weblinks(reply_data.get('body', '[deleted]'))

                    polarity, subjectivity, sentiment = None, None, None

                    if include_polarity or include_subjectivity or include_sentiment:
                        blob = TextBlob(reply_body)
                        if include_polarity:
                            polarity = round(blob.sentiment.polarity, 2)
                        if include_subjectivity:
                            subjectivity = round(blob.sentiment.subjectivity, 2)
                        if include_sentiment:
                            sentiment = "Positive" if polarity > 0 else "Negative" if polarity < 0 else "Neutral"

                    user_data[reply_user]["count"] += 1
                    user_data[reply_user]["replies"] += 1

                    combined_text += f"{reply_body} "
                    posts_data.append({
                        "Comment/Reply": "Reply",
                        "Username": reply_user,
                        "Text": reply_body,
                        "Polarity": polarity,
                        "Subjectivity": subjectivity,
                        "Sentiment": sentiment,
                        "Timestamp": datetime.fromtimestamp(reply_data.get('created_utc', 0), timezone.utc).strftime('%Y-%m-%d %H:%M:%S'),
                        "Source File": source_file
                    })

        # All words frequency count
        words = re.findall(r'\b\w+\b', combined_text.lower())
        all_word_frequencies = Counter(words)

        # Split into common and other word frequencies
        common_word_frequencies = Counter()
        other_word_frequencies = Counter()

        for word, freq in all_word_frequencies.items():
            if word in common_words:
                common_word_frequencies[word] = freq
            else:
                other_word_frequencies[word] = freq

        total_users = len(user_data)

        return user_data, common_word_frequencies, other_word_frequencies, posts_data, total_users, total_posts, None
    except Exception as e:
        return None, None, None, 0, 0, str(e)

# Function to save word frequencies to separate CSV files
def save_word_frequencies(common_word_frequencies, other_word_frequencies, common_csv_file_path, other_csv_file_path):
    try:
        # Save common words to a separate CSV file
        with open(common_csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Word', 'Frequency', 'Type'])
            for word, freq in sorted(common_word_frequencies.items(), key=lambda x: x[1], reverse=True):
                writer.writerow([word, freq, 'Common'])

        # Save other words to a separate CSV file
        with open(other_csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Word', 'Frequency', 'Type'])
            for word, freq in sorted(other_word_frequencies.items(), key=lambda x: x[1], reverse=True):
                writer.writerow([word, freq, 'Other'])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save word frequencies: {str(e)}")

# Function to save heat map data to a CSV
def save_heat_map_data(hour_day_counts, heatmap_csv_file_path):
    try:
        with open(heatmap_csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Day', 'Hour', 'Frequency'])
            for (day, hour), frequency in sorted(hour_day_counts.items()):
                writer.writerow([day, hour, frequency])
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save heat map data: {str(e)}")

# Function to save posts data to CSV
def save_posts_data(posts_data, csv_file_path, include_polarity, include_subjectivity, include_sentiment):
    try:
        fieldnames = ["Comment/Reply", "Username", "Text", "Timestamp", "Source File"]

        if include_polarity:
            fieldnames.append("Polarity")
        if include_subjectivity:
            fieldnames.append("Subjectivity")
        if include_sentiment:
            fieldnames.append("Sentiment")

        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts_data:
                filtered_post = {key: post[key] for key in fieldnames}
                writer.writerow(filtered_post)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save posts data: {str(e)}")

# Function to process all JSON files in the selected folder
def process_files(directory, common_words_file, include_polarity, include_subjectivity, include_sentiment):
    global output_folder, all_posts_data  # Make these variables global so they can be accessed later
    common_words = load_common_words(common_words_file)
    json_files = [f for f in os.listdir(directory) if f.endswith('.json')]

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_folder = os.path.join(directory, f"Data_{timestamp}")

    try:
        os.makedirs(output_folder, exist_ok=True)
        print(f"Created directory: {output_folder}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to create output directory: {str(e)}")
        return

    summary_file_path = os.path.join(output_folder, f"log_{timestamp}.txt")
    common_word_freq_csv_path = os.path.join(output_folder, f"common_word_frequencies_{timestamp}.csv")
    other_word_freq_csv_path = os.path.join(output_folder, f"other_word_frequencies_{timestamp}.csv")
    posts_csv_path = os.path.join(output_folder, f"reddit_posts_{timestamp}.csv")
    heatmap_csv_file_path = os.path.join(output_folder, f"heatmap_data_{timestamp}.csv")  # Path for heatmap data

    combined_common_word_frequencies = Counter()
    combined_other_word_frequencies = Counter()
    all_posts_data = []
    total_users = 0
    total_posts = 0
    total_comments = 0
    total_replies = 0
    log_content = []
    hour_day_counts = Counter()

    for json_file in json_files:
        json_file_path = os.path.join(directory, json_file)
        log_content.append(f"Processing file: {json_file}\n")

        user_data, common_word_frequencies, other_word_frequencies, posts_data, users, posts, error = process_json_file(
            json_file_path, common_words, include_polarity, include_subjectivity, include_sentiment, json_file)
        
        if error:
            log_content.append(f"Error processing {json_file}: {error}\n")
            continue

        combined_common_word_frequencies.update(common_word_frequencies)
        combined_other_word_frequencies.update(other_word_frequencies)
        all_posts_data.extend(posts_data)
        total_users += users
        total_posts += posts
        total_comments += sum(user["comments"] for user in user_data.values())
        total_replies += sum(user["replies"] for user in user_data.values())

        # Update hour and day counts for heatmap data
        for post in posts_data:
            timestamp = datetime.strptime(post['Timestamp'], '%Y-%m-%d %H:%M:%S')
            hour = timestamp.hour
            day = timestamp.weekday()  # Monday is 0 and Sunday is 6
            hour_day_counts[(day, hour)] += 1

        log_content.append(f"Posts: {posts}, Comments: {sum(user['comments'] for user in user_data.values())}, Replies: {sum(user['replies'] for user in user_data.values())}\n")
        log_content.append(f"Total Users: {users}\n\n")

    try:
        save_word_frequencies(combined_common_word_frequencies, combined_other_word_frequencies, common_word_freq_csv_path, other_word_freq_csv_path)
        print(f"Saved common word frequencies to: {common_word_freq_csv_path}")
        print(f"Saved other word frequencies to: {other_word_freq_csv_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save word frequencies: {str(e)}")
        return
    
    try:
        save_posts_data(all_posts_data, posts_csv_path, include_polarity, include_subjectivity, include_sentiment)
        print(f"Saved posts data to: {posts_csv_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save posts data: {str(e)}")
        return

    try:
        save_heat_map_data(hour_day_counts, heatmap_csv_file_path)
        print(f"Saved heat map data to: {heatmap_csv_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save heat map data: {str(e)}")
        return

    try:
        with open(summary_file_path, 'w', encoding='utf-8') as log_file:
            log_file.write("\n".join(log_content))
            log_file.write(f"Total Posts: {total_posts}\nTotal Comments: {total_comments}\nTotal Replies: {total_replies}\nTotal Users: {total_users}\n")
        print(f"Saved log file to: {summary_file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to save log file: {str(e)}")
        return

    try:
        os.startfile(output_folder)
        print(f"Opened folder: {output_folder}")
    except Exception as e:
        messagebox.showerror("Error", f"Could not open the directory: {str(e)}")

    messagebox.showinfo("Processing Complete", f"Files processed successfully.\n\nLog: {summary_file_path}\nCommon Word Frequencies: {common_word_freq_csv_path}\nOther Word Frequencies: {other_word_freq_csv_path}\nPosts Data: {posts_csv_path}\nHeat Map Data: {heatmap_csv_file_path}")

# Function to allow user to select the Word Cloud file
def select_word_cloud_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        generate_word_cloud(file_path, output_folder)

# Function to allow user to select the Heat Map file
def select_heat_map_file():
    file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
    if file_path:
        generate_heat_map(file_path)

# Function to generate a word cloud
def generate_word_cloud(csv_file_path, output_folder):
    # Load the word frequencies from the CSV file
    word_frequencies = {}
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            word_frequencies[row['Word']] = int(row['Frequency'])

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_frequencies)

    # Save the word cloud to a file
    wordcloud_file = os.path.join(output_folder, 'word_cloud.png')
    wordcloud.to_file(wordcloud_file)

    # Display the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

# Updated function to generate a heat map
def generate_heat_map(csv_file_path):
    # Load the heat map data from the CSV file
    heatmap_data = {}
    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            day = int(row['Day'])
            hour = int(row['Hour'])
            frequency = int(row['Frequency'])
            if day not in heatmap_data:
                heatmap_data[day] = [0] * 24
            heatmap_data[day][hour] = frequency

    # Convert the data into a 7x24 matrix
    heatmap_matrix = [heatmap_data.get(day, [0] * 24) for day in range(7)]

    # Create the heatmap
    plt.figure(figsize=(12, 6))
    sns.heatmap(heatmap_matrix, cmap='YlGnBu', cbar=True, annot=True, xticklabels=range(24), yticklabels=['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
    plt.title('Heat Map of Activity by Hour and Day')
    plt.xlabel('Hour of the Day')
    plt.ylabel('Day of the Week')
    plt.show()

# Function to display the About dialog with a hyperlink
def show_about():
    about_window = tk.Toplevel(root)
    about_window.title("About")
    about_window.geometry("400x250")
    about_window.resizable(False, False)

    about_text = (
        "Reddit Rambler\n"
        "Version 1.0\n\n"
        "This application processes Reddit data from JSON files,\n" 
        "generates word frequencies, and creates visualizations such\n"
        "as Word Clouds and Heat Maps.\n\n"
        "Developed by Caspar Wynne \n"
        "2024"
    )

    label = tk.Label(about_window, text=about_text, justify="left", padx=10, pady=10, anchor="w")
    label.pack()

    hyperlink = tk.Label(about_window, text="Read Me Document", fg="blue", cursor="hand2", padx=10, pady=10)
    hyperlink.pack()

    def open_url(event):
        webbrowser.open_new("https://github.com/casparwynne/RedditRambler/blob/main/README.md")

    hyperlink.bind("<Button-1>", open_url)

# Function to select the directory containing JSON files
def select_directory():
    directory = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(0, directory)

# Function to select the common words file
def select_common_words_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    common_words_entry.delete(0, tk.END)
    common_words_entry.insert(0, file_path)

# Function to open the common words file for editing
def open_common_words_file():
    file_path = common_words_entry.get()
    if os.path.exists(file_path):
        subprocess.Popen(['notepad.exe', file_path])
    else:
        messagebox.showwarning("File Not Found", "Common words file not found. Please select a valid file.")

# Function to start processing
def start_processing():
    directory = directory_entry.get()
    common_words_file = common_words_entry.get()

    if not directory:
        messagebox.showwarning("Input Error", "Please select a directory.")
        return

    if not common_words_file:
        messagebox.showwarning("Input Error", "Please select a common words file.")
        return

    try:
        process_files(directory, common_words_file, polarity_var.get(), subjectivity_var.get(), sentiment_var.get())
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred during processing: {str(e)}")


# Create the main application window
root = tk.Tk()
root.title("Reddit Rambler")

# Create a menu bar with an About option
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)
help_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=show_about)

# Directory selection
tk.Label(root, text="Select JSON Directory:").grid(row=0, column=0, padx=10, pady=10)
directory_entry = tk.Entry(root, width=50)
directory_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_directory).grid(row=0, column=2, padx=10, pady=10)

# Common words file selection
tk.Label(root, text="Select Common Words File:").grid(row=1, column=0, padx=10, pady=10)
common_words_entry = tk.Entry(root, width=50)
common_words_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_common_words_file).grid(row=1, column=2, padx=10, pady=10)
tk.Button(root, text="Edit", command=open_common_words_file).grid(row=1, column=3, padx=10, pady=10)

# Options for polarity, subjectivity, and sentiment
polarity_var = tk.BooleanVar(value=True)
subjectivity_var = tk.BooleanVar(value=True)
sentiment_var = tk.BooleanVar(value=True)

tk.Checkbutton(root, text="Include Polarity", variable=polarity_var).grid(row=2, column=0, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Include Subjectivity", variable=subjectivity_var).grid(row=2, column=1, padx=10, pady=5, sticky="w")
tk.Checkbutton(root, text="Include Sentiment", variable=sentiment_var).grid(row=2, column=2, padx=10, pady=5, sticky="w")

tk.Label(root, text="Visualisations:").grid(row=3, column=0, padx=10, pady=10)

tk.Button(root, text="Word Cloud", command=select_word_cloud_file).grid(row=4, column=1, padx=10, pady=10)
tk.Button(root, text="Heat Map", command=select_heat_map_file).grid(row=4, column=2, padx=10, pady=10)

# Start processing button
tk.Button(root, text="Start Processing", command=start_processing, width=20).grid(row=5, column=0, columnspan=4, padx=10, pady=20)

# Run the application
root.mainloop()
Appendix B
A recommended list of common words 
i
you
a
b
c
d
e
f
g
h
i
j
k
l
m
n
o
p
q
r
s
t
u
v
w
x
y
z
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
the
is
in
it
and
or
but
if
so
because
that
when
which
where
who
whom
this
that
these
those
am
are
was
were
be
been
being
have
has
had
do
does
did
a
an
on
with
by
from
to
of
at
