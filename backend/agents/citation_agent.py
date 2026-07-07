def citation_agent(state):

    citations = []

    seen = set()

    for chunk in state["verified_chunks"]:

        key = (
            chunk["document_id"],
            chunk["page"]
        )

        if key not in seen:

            seen.add(key)

            citations.append({

                "document_id": chunk["document_id"],

                "document": chunk["document"],

                "page": chunk["page"]

            })

    return {
        "citations": citations
    }