from src.rag_pipeline import RAGPipeline


def print_banner():

    print("\n" + "=" * 70)

    print(
        "📚 Document Q&A Bot (RAG)"
    )

    print("=" * 70)

    print(
        "\nAsk questions about your documents."
    )

    print(
        "Type 'exit', 'quit' or press Ctrl+C to stop.\n"
    )


def print_sources(
    sources
):

    if not sources:
        return

    print("\nSources:")

    for source in sources:

        print(
            f"- {source['source']} "
            f"(Page {source['page']})"
        )


def main():

    print_banner()

    try:

        rag = RAGPipeline()

    except Exception as error:

        print(
            f"\nFailed to load RAG pipeline:\n{error}"
        )

        return

    while True:

        try:

            question = input(
                "\n❓ Question: "
            ).strip()

            if not question:
                continue

            if question.lower() in [
                "exit",
                "quit",
                "q"
            ]:

                print(
                    "\n👋 Goodbye!"
                )

                break

            response = rag.ask(
                question
            )

            print("\n" + "=" * 70)

            print("💡 Answer")

            print("=" * 70)

            print(
                response["answer"]
            )

            print_sources(
                response["sources"]
            )

        except KeyboardInterrupt:

            print(
                "\n\n👋 Goodbye!"
            )

            break

        except Exception as error:

            print(
                f"\n❌ Error: {error}"
            )


if __name__ == "__main__":
    main()