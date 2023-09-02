# %%
import chromadb

# %%
client = chromadb.Client()
# %%
collection = client.create_collection("my-collection")
# %%
# The collection is where embeddings, documents, and any additional metadata are 
# stored to query later for various applications.

# add the documents in the db
collection.add(
    documents=["This is a document about cat", "This is a document about car", "This is a document about bike"],
    metadatas=[{"category": "animal"}, {"category": "vehicle"}, {"category": "vehicle"}],
    ids=["id1", "id2","id3"]
)
# %%
# ChromaDB will store the text documents and handle tokenization, vectorization, 
# and indexing automatically without any extra commands.
results = collection.query(
    query_texts=["vehicle"],
    n_results=1
)
# %%
results
# %%
from faker import Faker

fake = Faker()
# %%
bus_name = [fake.bs() for i in range(10)]
# %%
last_name = [fake.last_name() for i in range(10)]
# %%
list_name = bus_name + last_name
# %%
list_name
# %%
collection = client.create_collection("name-collection")
# %%
collection.add(
    documents=list_name, 
    ids = [str(i) for i in range(20)]
)
# %%
results = collection.query(
    query_texts=["Burke Co"],
    n_results=2
)
# %%
results
# %%
