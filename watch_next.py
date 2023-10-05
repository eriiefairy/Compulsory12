import spacy

# Load the spaCy model with word vectors (medium or large model)
nlp = spacy.load("en_core_web_md")  # You can also use "en_core_web_lg" for a larger model

# Find the most similar movie based on its description
with open('movies.txt', 'r') as f:
    movies = f.readlines()

query_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."


# Calculate similarity between two text strings using spaCy word vectors
def calculate_similarity(text1, text2):
    doc1 = nlp(text1)
    doc2 = nlp(text2)
    return doc1.similarity(doc2)


# Find the most similar movie based on its description
max_similarity = 0.0
most_similar_movie = None

for movie_description in movies:
    similarity = calculate_similarity(query_description, movie_description)
    if similarity > max_similarity:
        max_similarity = similarity
        most_similar_movie = movie_description.strip()

# Print the most similar movie
print("The most similar movie:", most_similar_movie)
