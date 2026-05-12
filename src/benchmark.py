import json


def format_results(query, expanded_query, results_a, results_b):
    return {
        "query": query,
        "strategy_a": {
            "top_chunks": [r["document"] for r in results_a]
        },
        "strategy_b": {
            "expanded_query": expanded_query,
            "top_chunks": [r["document"] for r in results_b]
        }
    }


def save_benchmark(data, filename="benchmark_output.json"):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4)