# Reddit Rambler – JSON data extractor
## Introduction
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
## Disclaimer
The Reddit Rambler software is provided "as is" for educational and research purposes, primarily aimed at supporting students and academics in their research efforts. The developer makes no guarantees regarding the accuracy, reliability, or suitability of the software for any specific research projects.
By using this software, you acknowledge and agree that:
1.	Responsibility for Research: The developer is not responsible for the outcomes, validity, or integrity of any research conducted using this software. Users are solely responsible for ensuring that their work complies with academic standards, ethical guidelines, and applicable laws.
2.	Software Availability: The availability of the Reddit Rambler software is not guaranteed. The software may be removed or discontinued at any time without prior notice. Users should not rely on its continuous availability for their research needs.
3.	Development and Support: Ongoing development or technical support for the software is not guaranteed. The developer may choose to update, modify, or cease development of the software at any time. Users should not expect regular updates or dedicated support.
The developer disclaims all liability for any damages, losses, or issues arising from the use of the software, including but not limited to data loss, inaccuracies in research, or any other negative outcomes. Users are advised to use the software with caution and to independently verify any results produced using the tool.
## AI Statement
This app and supporting documents have been made with the help with artificial intelligence.
## Getting JSON Files
•	Go to Reddit.com
•	Search for the subreddit/posts you are interested in and open the post.
•	Once the post has loaded click on the URL bar in the browser and add .json to the end of the text and hit return.
•	This will convert the webpage into a JSON file (a standard text-based format for representing structured data based on JavaScript object syntax).
•	You need to save the page by using the keyboard shortcut CTRL + S.
•	Navigate to where you want to store the JSON file. I suggest creating a new folder and label it something useful like the date or topic etc. 
•	Then give the file a useful name, in the picture below I have used example, use something you know will be useful in identifying the data.
•	Double check that the Save as type is set to JSON, sometimes browsers will try and force different file types. In those instances, set the Save As type to All Files and add. json to the end of your filename.
•	Click Save do this for each post you want to analyse.
## Running Reddit Rambler
•	Double click the app.
•	Click Browse to the right of the Select JSON Directory and select the folder that is containing all the JSON Files you want to process.
•	Click the Browse button to the right of the Select Common Words file.
•	You should have received a copy of the default common words list with when you downloaded the app. If not, you can create one easily by creating a blank text document (must be .txt, not .docx or any other text document), name it whatever you like. Click browse and select the common words file. You can click the Edit button to add or remove words you want to filter out of the analysis. 
•	Next select if you want to include TextBlob analysis.
•	Then click Start Processing.
•	Once processing has completed you will receive a message box indicating what has been undertook.
•	The app will also open the folder with all the processed data within.
## Common_Word_Frequencies CSV
This file contains three columns:
1.	Word: This is a list of individual words that were found in the posts that are contained in the Common_Words list (Appendix B).
2.	Frequency: This the number of times that word is present in the processed data.
3.	Type: The type of word, be it common (words filtered out of the data), or other, words retained in the data.  
## Other_Word_Frequencies CSV
This file contains three columns:
1.	Word: This is a list of words present in the posts, comments and replies after the common_words have been filtered out.
2.	Frequency: This the number of times that word is present in the processed data.
3.	Type: The type of word, be it common (words filtered out of the data), or other, words retained in the data.  
## Heatmap_Data CSV
This file contains three columns:
1.	Day: indicates the day of the week with 0 representing Monday, 6 representing Sunday.
2.	Hour: 24-hour time, e.g. 1 = 1am, 23 = 11pm
3.	Frequency: the number of posts made during that time and hour.  
## Reddit_Posts CSV
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
## TextBlob
TextBlob is a simple and easy-to-use Python library for processing textual data. It provides a convenient interface for performing common natural language processing (NLP) tasks and is especially useful for quick sentiment analysis using a lexicon-based approach, which calculates polarity and subjectivity scores for text. 
### Polarity
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
### Subjectivity
Subjectivity is a measure of how subjective or objective the text is. It ranges from 0 (completely objective) to 1 (completely subjective). Subjectivity reflects the presence of personal opinions, feelings, or beliefs in the text.
Here’s how it works:
Lexicon-Based Approach: Similar to polarity, TextBlob uses a dictionary where words are annotated with subjectivity scores. Words that convey strong opinions or emotions (e.g., "amazing," "horrible") are assigned higher subjectivity scores, while neutral words (e.g., "fact," "number") are assigned lower scores.
Sentence Subjectivity Calculation: The subjectivity score of a sentence is computed by averaging the subjectivity scores of the words within it.
Overall Subjectivity: For multiple sentences, the overall subjectivity score is the average of the individual sentence scores.
Example:
Sentence: "This cake is delicious."
"Delicious" might have a subjectivity score of 0.9, making the sentence highly subjective.
### Sentiment
When people refer to sentimentality in the context of TextBlob, they are usually referring to the combination of polarity and subjectivity that describes the sentiment of the text. The sentiment attribute in TextBlob gives you both the polarity and subjectivity of a text.
Here’s how TextBlob processes sentimentality:
TextBlob.sentiment: When you call TextBlob.sentiment on a text, it returns a Sentiment namedtuple with two values: polarity and subjectivity.
## Visualisations
This app currently offers two forms of visualisations that can be run after JSON data has been processed.  
### Word Cloud
A word cloud is a visual representation of text data where the size of each word indicates its frequency or importance in the dataset. Commonly used in text analysis, word clouds help to quickly identify the most prominent words in a body of text, with larger, bolder words appearing more frequently or being more significant. This visualization is often used to summarize large amounts of text data, making key themes or topics easy to identify briefly.
To create a word cloud, process the JSON files you are working with, then click on the WordCloud button and select which of the frequency (either other or common) files from the analysis by clicking and click OK. 
#### Word Cloud hints and tips
1.	Using “Common Words” to isolate or filter specific words. You could use a common words file to track the frequency of specific words you are interested in, instead of how it was originally intended, to filter out common high frequency words such as conjunctive like “and”. 
2.	If you find in your frequency file some words that you are not appropriate e.g. “for” in the example above, you could either:
a.	add for to the common words file.
b.	open the data file (for example in Excel) and delete the line containing the For frequency.
In the interest of data preservation, the first option is preferable. 

### Heat Map
The Heat Map illustrates when posts, comments, and replies are made by day and hour in a grid-like visual representation where each cell corresponds to a specific hour of the day and a specific day of the week. The colour intensity of each cell indicates the frequency or volume of activity (posts, comments, replies) during that time slot.
To create a heat map, process the JSON files you are working with, then click on the Heat Map button and select the heat map data file.  
## Licence
MIT License
Copyright © 2024 Caspar Wynne
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

