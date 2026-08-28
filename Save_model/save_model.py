from sentence_transformers import SentenceTransformer

model=SentenceTransformer('BAAI/bge-base-en-v1.5')

model.save('D:\lohith\LawRAG\Save_model\Model_files')