from transformers import pipeline

from embeddings import MockTextEmbeddingModel
from retrieval import Retriever
from query_expansion import MockGenerativeModel
from pipeline import RAGPipeline
from benchmark import format_results, save_benchmark


def load_documents(path: str):
    with open(path, "r") as f:
        docs = [line.strip() for line in f.readlines() if line.strip()]
    return docs


def print_results(title, results):
    print(f"\n{title}\n")
    for i, result in enumerate(results, start=1):
        print(f"Result {i}")
        print("Score:", round(result["score"], 4))
        print(result["document"])
        print()


def main():
    docs = load_documents("data/technical_docs.txt")

    pipeline = RAGPipeline(docs)

    queries = [
        "How does the system handle peak load?",
        "What prevents cascading failures in microservices?",
        "How do asynchronous queues improve resilience?",
    ]

    all_results = []

    for query in queries:
        
        results_a = pipeline.strategy_a(query)

        expanded_query, results_b = pipeline.strategy_b(query)

        print(f"\n{'='*70}")
        print(f"Original Query: {query}")
        print(f"Expanded Query: {expanded_query}")

        print_results("Strategy A — Raw Vector Search", results_a)
        print_results("Strategy B — Expanded Query Search", results_b)

        benchmark_data = format_results(query, expanded_query, results_a, results_b)
        all_results.append(benchmark_data)

    save_benchmark(all_results)

    print("\nBenchmark saved to benchmark_output.json")

if __name__ == "__main__":
    main()