from src.rag_pipeline import RAGPipeline

rag = RAGPipeline()

question = "Who won the FIFA World Cup in 1998?"

response = rag.ask(question)

print("\nQUESTION:")
print(question)

print("\nANSWER:")
print(response["answer"])

if response["sources"]:

    print("\nSOURCES:")

    for source in response["sources"]:

        print(
            f"- {source['source']} "
            f"(Page {source['page']})"
        )