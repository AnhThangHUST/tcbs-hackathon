import nltk.data
from elasticsearch import Elasticsearch
from sentence_transformers import SentenceTransformer

from service.thesaurus import createThesaurus

elasticsearch_client = Elasticsearch()
model_embedding = SentenceTransformer('VoVanPhuc/sup-SimCSE-VietNamese-phobert-base')
nltk.data.path.append("/home/thangna/hackathon/nltk_data")
tokenizer = nltk.data.load('tokenizers/punkt/PY3/english.pickle')
global_thesaurus = createThesaurus()

def embed_batch_text(batch_text):
    batch_embedding = model_embedding.encode(batch_text)
    return [vector.tolist() for vector in batch_embedding]
