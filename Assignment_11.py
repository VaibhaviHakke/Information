
# # # # # Search Citations:

# # # # # Enter the IDs for two papers (Paper A and Paper B).
# # # # # Check if Paper A cites Paper B directly or indirectly (up to 3 levels of citation).
# # # # # Search Classification:

# # # # # Enter the ID for a paper.
# # # # # Retrieve and display the full classification hierarchy of the paper.

# # # # import tkinter as tk
# # # # from neo4j import GraphDatabase

# # # # # Neo4j database connection details
# # # # uri = "bolt://localhost:7687"
# # # # username = "neo4j"
# # # # password = "9049531968"

# # # # # Initialize the Neo4j driver
# # # # try:
# # # #     driver = GraphDatabase.driver(uri, auth=(username, password))
# # # # except Exception as e:
# # # #     print(f"Failed to connect to Neo4j: {e}")
# # # #     exit()

# # # # # Function to check if paper A cites paper B
# # # # def does_paper_a_cite_paper_b(tx, paper_a_id, paper_b_id):
# # # #     query = (
# # # #         "MATCH (a:Paper {paper_id: $paper_a_id})-[:CITATION*..3]->(b:Paper {paper_id: $paper_b_id}) "
# # # #         "RETURN count(*) > 0"
# # # #     )
# # # #     result = tx.run(query, paper_a_id=paper_a_id, paper_b_id=paper_b_id)
# # # #     return result.single()[0]

# # # # # Function to get the full classification of a paper
# # # # def get_classification_of_paper(tx, paper_id):
# # # #     query = (
# # # #         "MATCH (p:Paper {paper_id: $paper_id})-[:CLASSIFICATION*]->(c:Classification) "
# # # #         "RETURN c.name"
# # # #     )
# # # #     result = tx.run(query, paper_id=paper_id)
# # # #     return [record['c.name'] for record in result]

# # # # # Function to handle search button click
# # # # def search():
# # # #     # Get the paper IDs from the entry widgets
# # # #     paper_a_id = entry_paper_a_id.get()
# # # #     paper_b_id = entry_paper_b_id.get()
# # # #     paper_id = entry_paper_id.get()

# # # #     # Validate input
# # # #     if not paper_a_id or not paper_b_id or not paper_id:
# # # #         label_a_b.config(text="Please enter all paper IDs")
# # # #         label_a_cite_b.config(text="")
# # # #         label_classification.config(text="")
# # # #         return

# # # #     # Open a new Neo4j session
# # # #     with driver.session() as session:
# # # #         try:
# # # #             # Check if paper A cites paper B
# # # #             result_a_b = does_paper_a_cite_paper_b(session, paper_a_id, paper_b_id)
# # # #             label_a_b.config(text="Yes" if result_a_b else "No")

# # # #             # Check if paper A cites a paper that cites paper B
# # # #             result_a_cite_b = False
# # # #             for i in range(3):
# # # #                 result_a_cite_b = does_paper_a_cite_paper_b(session, paper_a_id, paper_b_id)
# # # #                 if result_a_cite_b:
# # # #                     break
# # # #             label_a_cite_b.config(text="Yes" if result_a_cite_b else "No")

# # # #             # Get the full classification of the paper
# # # #             result_classification = get_classification_of_paper(session, paper_id)
# # # #             label_classification.config(text="/".join(result_classification))
# # # #         except Exception as e:
# # # #             print(f"Query execution failed: {e}")
# # # #             label_a_b.config(text="")
# # # #             label_a_cite_b.config(text="")
# # # #             label_classification.config(text="Error executing query")

# # # # # Create the main window
# # # # window = tk.Tk()
# # # # window.title("Research Papers Database")

# # # # # Create the widgets
# # # # label_paper_a_id = tk.Label(window, text="Paper A ID:")
# # # # entry_paper_a_id = tk.Entry(window)
# # # # label_paper_b_id = tk.Label(window, text="Paper B ID:")
# # # # entry_paper_b_id = tk.Entry(window)
# # # # button_search_citations = tk.Button(window, text="Search Citations", command=search)
# # # # label_a_b = tk.Label(window, text="")
# # # # label_a_cite_b = tk.Label(window, text="")
# # # # label_paper_id = tk.Label(window, text="Paper ID:")
# # # # entry_paper_id = tk.Entry(window)
# # # # button_search_classification = tk.Button(window, text="Search Classification", command=search)
# # # # label_classification = tk.Label(window, text="")

# # # # # Pack the widgets
# # # # label_paper_a_id.pack()
# # # # entry_paper_a_id.pack()
# # # # label_paper_b_id.pack()
# # # # entry_paper_b_id.pack()
# # # # button_search_citations.pack()
# # # # label_a_b.pack()
# # # # label_a_cite_b.pack()
# # # # label_paper_id.pack()
# # # # entry_paper_id.pack()
# # # # button_search_classification.pack()
# # # # label_classification.pack()

# # # # # Run the main loop
# # # # window.mainloop()

# # # import tkinter as tk
# # # from tkinter import messagebox
# # # from neo4j import GraphDatabase

# # # # Neo4j database connection details
# # # uri = "bolt://localhost:7687"
# # # username = "neo4j"
# # # password = "9049531968"

# # # # Initialize the Neo4j driver
# # # try:
# # #     driver = GraphDatabase.driver(uri, auth=(username, password))
# # # except Exception as e:
# # #     print(f"Failed to connect to Neo4j: {e}")
# # #     exit()

# # # # Function to check if paper A cites paper B
# # # def does_paper_a_cite_paper_b(tx, paper_a_id, paper_b_id):
# # #     query = (
# # #         "MATCH (a:Paper {paper_id: $paper_a_id})-[:CITATION*..3]->(b:Paper {paper_id: $paper_b_id}) "
# # #         "RETURN count(*) > 0"
# # #     )
# # #     result = tx.run(query, paper_a_id=paper_a_id, paper_b_id=paper_b_id)
# # #     return result.single()[0]

# # # # Function to get the full classification of a paper
# # # def get_classification_of_paper(tx, paper_id):
# # #     query = (
# # #         "MATCH (p:Paper {paper_id: $paper_id})-[:CLASSIFICATION*]->(c:Classification) "
# # #         "RETURN c.name"
# # #     )
# # #     result = tx.run(query, paper_id=paper_id)
# # #     return [record['c.name'] for record in result]

# # # # Function to handle search button click
# # # def search():
# # #     # Get the paper IDs from the entry widgets
# # #     paper_a_id = entry_paper_a_id.get()
# # #     paper_b_id = entry_paper_b_id.get()
# # #     paper_id = entry_paper_id.get()

# # #     # Validate input
# # #     if not paper_a_id or not paper_b_id or not paper_id:
# # #         messagebox.showwarning("Warning", "Please enter all paper IDs")
# # #         return

# # #     # Open a new Neo4j session
# # #     with driver.session() as session:
# # #         try:
# # #             # Check if paper A cites paper B
# # #             result_a_b = does_paper_a_cite_paper_b(session, paper_a_id, paper_b_id)
# # #             label_a_b.config(text="Directly Cites" if result_a_b else "Does Not Cite")

# # #             # Check if paper A cites a paper that cites paper B
# # #             result_a_cite_b = False
# # #             for i in range(3):
# # #                 result_a_cite_b = does_paper_a_cite_paper_b(session, paper_a_id, paper_b_id)
# # #                 if result_a_cite_b:
# # #                     break
# # #             label_a_cite_b.config(text="Indirectly Cites" if result_a_cite_b else "Does Not Indirectly Cite")

# # #             # Get the full classification of the paper
# # #             result_classification = get_classification_of_paper(session, paper_id)
# # #             label_classification.config(text="Classification: " + "/".join(result_classification))
# # #         except Exception as e:
# # #             messagebox.showerror("Error", f"Query execution failed: {e}")
# # #             label_a_b.config(text="")
# # #             label_a_cite_b.config(text="")
# # #             label_classification.config(text="Error executing query")

# # # # Create the main window
# # # window = tk.Tk()
# # # window.title("Research Papers Database")

# # # # Create the widgets
# # # label_paper_a_id = tk.Label(window, text="Paper A ID:")
# # # entry_paper_a_id = tk.Entry(window)
# # # label_paper_b_id = tk.Label(window, text="Paper B ID:")
# # # entry_paper_b_id = tk.Entry(window)
# # # button_search_citations = tk.Button(window, text="Search Citations", command=search)
# # # label_a_b = tk.Label(window, text="")
# # # label_a_cite_b = tk.Label(window, text="")
# # # label_paper_id = tk.Label(window, text="Paper ID:")
# # # entry_paper_id = tk.Entry(window)
# # # button_search_classification = tk.Button(window, text="Search Classification", command=search)
# # # label_classification = tk.Label(window, text="")

# # # # Pack the widgets
# # # label_paper_a_id.pack(pady=5)
# # # entry_paper_a_id.pack(pady=5)
# # # label_paper_b_id.pack(pady=5)
# # # entry_paper_b_id.pack(pady=5)
# # # button_search_citations.pack(pady=5)
# # # label_a_b.pack(pady=5)
# # # label_a_cite_b.pack(pady=5)
# # # label_paper_id.pack(pady=5)
# # # entry_paper_id.pack(pady=5)
# # # button_search_classification.pack(pady=5)
# # # label_classification.pack(pady=5)

# # # # Run the main loop
# # # window.mainloop()

# # import tkinter as tk
# # from tkinter import messagebox
# # from neo4j import GraphDatabase

# # # Neo4j database connection details
# # uri = "bolt://localhost:7687"
# # username = "neo4j"
# # password = "9049531968"

# # # Initialize the Neo4j driver
# # try:
# #     driver = GraphDatabase.driver(uri, auth=(username, password))
# # except Exception as e:
# #     print(f"Failed to connect to Neo4j: {e}")
# #     exit()

# # # Function to check if paper A cites paper B
# # def does_paper_a_cite_paper_b(tx, paper_a_id, paper_b_id):
# #     query = (
# #         "MATCH (a:Paper {paper_id: $paper_a_id})-[:CITATION*..3]->(b:Paper {paper_id: $paper_b_id}) "
# #         "RETURN count(*) > 0"
# #     )
# #     result = tx.run(query, paper_a_id=paper_a_id, paper_b_id=paper_b_id)
# #     return result.single()[0]

# # # Function to get the full classification of a paper
# # def get_classification_of_paper(tx, paper_id):
# #     query = (
# #         "MATCH (p:Paper {paper_id: $paper_id})-[:CLASSIFICATION*]->(c:Classification) "
# #         "RETURN c.name"
# #     )
# #     result = tx.run(query, paper_id=paper_id)
# #     return [record['c.name'] for record in result]

# # # Function to handle search button click
# # def search():
# #     # Get the paper IDs from the entry widgets
# #     paper_a_id = entry_paper_a_id.get()
# #     paper_b_id = entry_paper_b_id.get()
# #     paper_id = entry_paper_id.get()

# #     # Validate input
# #     if not paper_a_id or not paper_b_id or not paper_id:
# #         messagebox.showwarning("Warning", "Please enter all paper IDs")
# #         return

# #     # Open a new Neo4j session
# #     with driver.session() as session:
# #         try:
# #             # Check if paper A cites paper B
# #             result_a_b = does_paper_a_cite_paper_b(session, paper_a_id, paper_b_id)
# #             label_a_b.config(text="Directly Cites" if result_a_b else "Does Not Cite")

# #             # Check if paper A cites a paper that cites paper B
# #             result_a_cite_b = False
# #             for i in range(3):
# #                 result_a_cite_b = does_paper_a_cite_paper_b(session, paper_a_id, paper_b_id)
# #                 if result_a_cite_b:
# #                     break
# #             label_a_cite_b.config(text="Indirectly Cites" if result_a_cite_b else "Does Not Indirectly Cite")

# #             # Get the full classification of the paper
# #             result_classification = get_classification_of_paper(session, paper_id)
# #             label_classification.config(text="Classification: " + "/".join(result_classification))
# #         except Exception as e:
# #             messagebox.showerror("Error", f"Query execution failed: {e}")
# #             label_a_b.config(text="")
# #             label_a_cite_b.config(text="")
# #             label_classification.config(text="Error executing query")

# # # Create the main window
# # window = tk.Tk()
# # window.title("Research Papers Database")
# # window.geometry("400x300")
# # window.configure(bg="#f0f0f0")

# # # Create the widgets
# # label_paper_a_id = tk.Label(window, text="Paper A ID:", bg="#f0f0f0", font=("Arial", 12))
# # entry_paper_a_id = tk.Entry(window, font=("Arial", 12))
# # label_paper_b_id = tk.Label(window, text="Paper B ID:", bg="#f0f0f0", font=("Arial", 12))
# # entry_paper_b_id = tk.Entry(window, font=("Arial", 12))
# # button_search_citations = tk.Button(window, text="Search Citations", command=search, bg="#007BFF", fg="white", font=("Arial", 12))
# # label_a_b = tk.Label(window, text="", bg="#f0f0f0", font=("Arial", 12))
# # label_a_cite_b = tk.Label(window, text="", bg="#f0f0f0", font=("Arial", 12))
# # label_paper_id = tk.Label(window, text="Paper ID:", bg="#f0f0f0", font=("Arial", 12))
# # entry_paper_id = tk.Entry(window, font=("Arial", 12))
# # button_search_classification = tk.Button(window, text="Search Classification", command=search, bg="#007BFF", fg="white", font=("Arial", 12))
# # label_classification = tk.Label(window, text="", bg="#f0f0f0", font=("Arial", 12))

# # # Pack the widgets
# # label_paper_a_id.pack(pady=5)
# # entry_paper_a_id.pack(pady=5)
# # label_paper_b_id.pack(pady=5)
# # entry_paper_b_id.pack(pady=5)
# # button_search_citations.pack(pady=10)
# # label_a_b.pack(pady=5)
# # label_a_cite_b.pack(pady=5)
# # label_paper_id.pack(pady=5)
# # entry_paper_id.pack(pady=5)
# # button_search_classification.pack(pady=10)
# # label_classification.pack(pady=5)

# # # Run the main loop
# # window.mainloop()


# import tkinter as tk
# from tkinter import messagebox
# from neo4j import GraphDatabase

# # Neo4j database connection details
# uri = "bolt://localhost:7687"
# username = "neo4j"
# password = "9049531968"

# # Initialize the Neo4j driver
# try:
#     driver = GraphDatabase.driver(uri, auth=(username, password))
# except Exception as e:
#     print(f"Failed to connect to Neo4j: {e}")
#     exit()

# # Function to check if paper A cites paper B
# def does_paper_a_cite_paper_b(tx, paper_a_id, paper_b_id):
#     query = (
#         "MATCH (a:Paper {paper_id: $paper_a_id})-[:CITATION*..3]->(b:Paper {paper_id: $paper_b_id}) "
#         "RETURN count(*) > 0"
#     )
#     result = tx.run(query, paper_a_id=paper_a_id, paper_b_id=paper_b_id)
#     return result.single()[0]

# # Function to get the full classification of a paper
# def get_classification_of_paper(tx, paper_id):
#     query = (
#         "MATCH (p:Paper {paper_id: $paper_id})-[:CLASSIFICATION*]->(c:Classification) "
#         "RETURN c.name"
#     )
#     result = tx.run(query, paper_id=paper_id)
#     return [record['c.name'] for record in result]

# # Function to handle search button click
# def search():
#     # Get the paper IDs from the entry widgets
#     paper_a_id = entry_paper_a_id.get()
#     paper_b_id = entry_paper_b_id.get()
#     paper_id = entry_paper_id.get()

#     # Validate input for Paper A and Paper B IDs
#     if not paper_a_id or not paper_b_id:
#         messagebox.showwarning("Warning", "Please enter both Paper A and Paper B IDs")
#         return

#     # Open a new Neo4j session
#     with driver.session() as session:
#         try:
#             # Check if paper A cites paper B
#             result_a_b = does_paper_a_cite_paper_b(session, paper_a_id, paper_b_id)
#             label_a_b.config(text="Directly Cites" if result_a_b else "Does Not Cite")

#             # Check if paper A cites a paper that cites paper B
#             result_a_cite_b = False
#             for i in range(3):
#                 result_a_cite_b = does_paper_a_cite_paper_b(session, paper_a_id, paper_b_id)
#                 if result_a_cite_b:
#                     break
#             label_a_cite_b.config(text="Indirectly Cites" if result_a_cite_b else "Does Not Indirectly Cite")

#             # Get the full classification of the paper
#             if paper_id:  # Only execute this if Paper ID is provided
#                 result_classification = get_classification_of_paper(session, paper_id)
#                 label_classification.config(text="Classification: " + "/".join(result_classification))
#             else:
#                 label_classification.config(text="")  # Clear classification label if Paper ID is not provided

#         except Exception as e:
#             messagebox.showerror("Error", f"Query execution failed: {e}")
#             label_a_b.config(text="")
#             label_a_cite_b.config(text="")
#             label_classification.config(text="Error executing query")

# # Create the main window
# window = tk.Tk()
# window.title("Research Papers Database")
# window.geometry("400x300")
# window.configure(bg="#f0f0f0")

# # Create the widgets
# label_paper_a_id = tk.Label(window, text="Paper A ID:", bg="#f0f0f0", font=("Arial", 12))
# entry_paper_a_id = tk.Entry(window, font=("Arial", 12))
# label_paper_b_id = tk.Label(window, text="Paper B ID:", bg="#f0f0f0", font=("Arial", 12))
# entry_paper_b_id = tk.Entry(window, font=("Arial", 12))
# button_search_citations = tk.Button(window, text="Search Citations", command=search, bg="#007BFF", fg="white", font=("Arial", 12))
# label_a_b = tk.Label(window, text="", bg="#f0f0f0", font=("Arial", 12))
# label_a_cite_b = tk.Label(window, text="", bg="#f0f0f0", font=("Arial", 12))
# label_paper_id = tk.Label(window, text="Paper ID:", bg="#f0f0f0", font=("Arial", 12))
# entry_paper_id = tk.Entry(window, font=("Arial", 12))
# button_search_classification = tk.Button(window, text="Search Classification", command=search, bg="#007BFF", fg="white", font=("Arial", 12))
# label_classification = tk.Label(window, text="", bg="#f0f0f0", font=("Arial", 12))

# # Pack the widgets
# label_paper_a_id.pack(pady=5)
# entry_paper_a_id.pack(pady=5)
# label_paper_b_id.pack(pady=5)
# entry_paper_b_id.pack(pady=5)
# button_search_citations.pack(pady=10)
# label_a_b.pack(pady=5)
# label_a_cite_b.pack(pady=5)
# label_paper_id.pack(pady=5)
# entry_paper_id.pack(pady=5)
# button_search_classification.pack(pady=10)
# label_classification.pack(pady=5)

# # Run the main loop
# window.mainloop()


import tkinter as tk
from tkinter import messagebox
from neo4j import GraphDatabase

# Neo4j database connection details
uri = "bolt://localhost:7687"
username = "neo4j"
password = "9049531968"

# Initialize the Neo4j driver
try:
    driver = GraphDatabase.driver(uri, auth=(username, password))
except Exception as e:
    print(f"Failed to connect to Neo4j: {e}")
    exit()

# Function to check if paper A cites paper B
def does_paper_a_cite_paper_b(tx, paper_a_id, paper_b_id):
    query = (
        "MATCH (a:Paper {paper_id: $paper_a_id})-[:CITATION*..3]->(b:Paper {paper_id: $paper_b_id}) "
        "RETURN count(*) > 0"
    )
    result = tx.run(query, paper_a_id=paper_a_id, paper_b_id=paper_b_id)
    return result.single()[0]

# Function to get the full classification of a paper
# Function to get the full classification of a paper
def get_classification_of_paper(tx, paper_id):
    query = (
        "MATCH (p:Paper {paper_id: $paper_id})-[:CLASSIFICATION*]->(c:Classification) "
        "RETURN c.name"
    )
    result = tx.run(query, paper_id=paper_id)
    classifications = [record['c.name'] for record in result]
    print(f"Query Result for Paper {paper_id}: {classifications}")  # Debug print
    return classifications

# Function to handle search button click
def search():
    # Get the paper IDs from the entry widgets
    paper_a_id = entry_paper_a_id.get()
    paper_b_id = entry_paper_b_id.get()
    paper_id = entry_paper_id.get()

    # Validate input for Paper A and Paper B IDs
    if not paper_a_id or not paper_b_id:
        messagebox.showwarning("Warning", "Please enter both Paper A and Paper B IDs")
        return

    # Open a new Neo4j session
    with driver.session() as session:
        try:
            # Check if paper A cites paper B
            result_a_b = does_paper_a_cite_paper_b(session, paper_a_id, paper_b_id)
            label_a_b.config(text="Directly Cites" if result_a_b else "Does Not Cite")

            # Check if paper A cites a paper that cites paper B
            result_a_cite_b = False
            for i in range(3):
                result_a_cite_b = does_paper_a_cite_paper_b(session, paper_a_id, paper_b_id)
                if result_a_cite_b:
                    break
            label_a_cite_b.config(text="Indirectly Cites" if result_a_cite_b else "Does Not Indirectly Cite")

            # Get the full classification of the paper
            if paper_id:  # Only execute this if Paper ID is provided
                result_classification = get_classification_of_paper(session, paper_id)
                if result_classification:
                    label_classification.config(text="Classification: " + "/".join(result_classification))
                else:
                    label_classification.config(text="Classification: No classification found")
            else:
                label_classification.config(text="")  # Clear classification label if Paper ID is not provided

        except Exception as e:
            messagebox.showerror("Error", f"Query execution failed: {e}")
            label_a_b.config(text="")
            label_a_cite_b.config(text="")
            label_classification.config(text="Error executing query")

# Create the main window
window = tk.Tk()
window.title("Research Papers Database")
window.geometry("400x350")
window.configure(bg="#f0f0f0")

# Create the widgets
label_paper_a_id = tk.Label(window, text="Paper A ID:", bg="#f0f0f0", font=("Arial", 12))
entry_paper_a_id = tk.Entry(window, font=("Arial", 12))
label_paper_b_id = tk.Label(window, text="Paper B ID:", bg="#f0f0f0", font=("Arial", 12))
entry_paper_b_id = tk.Entry(window, font=("Arial", 12))
button_search_citations = tk.Button(window, text="Search Citations", command=search, bg="#007BFF", fg="white", font=("Arial", 12))
label_a_b = tk.Label(window, text="", bg="#f0f0f0", font=("Arial", 12))
label_a_cite_b = tk.Label(window, text="", bg="#f0f0f0", font=("Arial", 12))
label_paper_id = tk.Label(window, text="Paper ID:", bg="#f0f0f0", font=("Arial", 12))
entry_paper_id = tk.Entry(window, font=("Arial", 12))
button_search_classification = tk.Button(window, text="Search Classification", command=search, bg="#007BFF", fg="white", font=("Arial", 12))
label_classification = tk.Label(window, text="", bg="#f0f0f0", font=("Arial", 12))

# Pack the widgets
label_paper_a_id.pack(pady=5)
entry_paper_a_id.pack(pady=5)
label_paper_b_id.pack(pady=5)
entry_paper_b_id.pack(pady=5)
button_search_citations.pack(pady=10)
label_a_b.pack(pady=5)
label_a_cite_b.pack(pady=5)
label_paper_id.pack(pady=5)
entry_paper_id.pack(pady=5)
button_search_classification.pack(pady=10)
label_classification.pack(pady=5)

# Run the main loop
window.mainloop()
