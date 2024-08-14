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
