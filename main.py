import os
from langchain.llms import OpenAI
from langchain.document_loaders import ArxivLoader, PyPDFDirectoryLoader
from langchain.document_loaders.base import BaseLoader
from langchain.indexes.vectorstore import VectorstoreIndexCreator

os.environ["OPENAI_API_KEY"] = "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"

LOCAL_FILES = True


def load_local_documents(pdf_path: str):
    pdf_loader = PyPDFDirectoryLoader(pdf_path, silent_errors=True)
    return pdf_loader


def load_arxiv_documents(query: str):
    arxiv_loader = ArxivLoader(query=query, load_max_docs=5, load_all_available_meta=True)
    return arxiv_loader


if __name__ == "__main__":
    llm = OpenAI(temperature=0.1, max_tokens=1000)

    loader: BaseLoader = load_local_documents("pdfs/") if LOCAL_FILES else load_arxiv_documents("cat:cs.CV AND texture")
    docs = loader.load()
    print("Docs found:" + str(len(docs)))
    for d in docs:
        print(d.metadata)
        print("=" * 80)

    index = VectorstoreIndexCreator().from_loaders([loader])
    query = "What articles used Generative Adversarial Networks? Provide the source and page number for each article you find."
    resp = index.query_with_sources(llm=llm, question=query, chain_type="stuff")
    print(query)
    print(resp)
