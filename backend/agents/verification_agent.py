from pandas import unique


def verification_agent(state):

    unique = []

    seen = set()

    for chunk in state["retrieved_chunks"]:

        key = (
            chunk["document_id"],
            chunk["page"]
        )

        if key not in seen:

            seen.add(key)

            unique.append(chunk)
    print("\n========== VERIFIED ==========")
    print(len(unique))
    print("=============================\n")
    return {
        "verified_chunks": unique
    }