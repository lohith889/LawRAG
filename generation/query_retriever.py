def retrival(query:str)->list[str]:
    import chromadb

    client=chromadb.PersistentClient(path="D:\lohith\LawRAG\database")
    collection=client.get_collection(name='law_document')

    results=collection.query(
        query_texts=[query],
        n_results=5
    )
    return results['documents']