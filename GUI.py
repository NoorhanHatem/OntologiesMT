import tkinter as tk


def search():
    including_actors = including_actors_entry.get()
    excluding_actors = excluding_actors_entry.get()
    included_directors = included_directors_entry.get()
    excluded_directors = excluded_directors_entry.get()
    included_genres = included_genres_entry.get()
    excluded_genres = excluded_genres_entry.get()
    included_writers = included_writers_entry.get()
    excluded_writers = excluded_writers_entry.get()

    # perform the search operation based on the input values
    # For now, let's just print them
    result_text.delete(1.0, tk.END)
    result_text.insert(tk.END, "Including Actors: {}\n".format(including_actors))
    result_text.insert(tk.END, "Excluding Actors: {}\n".format(excluding_actors))
    result_text.insert(tk.END, "Included Directors: {}\n".format(included_directors))
    result_text.insert(tk.END, "Excluded Directors: {}\n".format(excluded_directors))
    result_text.insert(tk.END, "Included Genres: {}\n".format(included_genres))
    result_text.insert(tk.END, "Excluded Genres: {}\n".format(excluded_genres))
    result_text.insert(tk.END, "Included Writers: {}\n".format(included_writers))
    result_text.insert(tk.END, "Excluded Writers: {}\n".format(excluded_writers))


# Create main window
root = tk.Tk()
root.title("Movie Search")

# Create labels and text entry boxes for including and excluding actors, directors, genres, and writers
text_boxes = [
    "Including Actors", "Excluding Actors",
    "Included Directors", "Excluded Directors",
    "Included Genres", "Excluded Genres",
    "Included Writers", "Excluded Writers"
]

for i, text_box in enumerate(text_boxes):
    label = tk.Label(root, text=f"{text_box}:")
    label.grid(row=i, column=0, sticky="w")
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)

# Create search button
search_button = tk.Button(root, text="Search", command=search)
search_button.grid(row=len(text_boxes), columnspan=2)

# Create text widget to display results
result_text = tk.Text(root, width=40, height=10)
result_text.grid(row=len(text_boxes) + 1, columnspan=2)

root.mainloop()
