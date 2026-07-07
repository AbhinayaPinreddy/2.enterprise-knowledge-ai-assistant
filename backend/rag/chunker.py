from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter(
    chunk_size=800,
    chunk_overlap=200,
    separators=["\n\n", "\n", ".", " ", ""]
)


def split_pages_into_chunks(pages, document_id):

    all_chunks = []

    chunk_id = 0

    for page in pages:

        page_chunks = splitter.split_text(page["text"])

        for chunk in page_chunks:

            all_chunks.append({
                "chunk_id": chunk_id,
                "document_id": document_id,
                "page": page["page"],
                "text": chunk
            })

            chunk_id += 1

    return all_chunks