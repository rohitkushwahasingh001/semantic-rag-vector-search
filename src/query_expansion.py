class MockGenerativeModel:
    def expand_query(self, query: str) -> str:
        expansions = {
            "How does the system handle peak load?":
                "Autoscaling automatically launches additional service instances when traffic increases during peak load.",

            "What prevents cascading failures in microservices?":
                "Circuit breakers temporarily block requests when services repeatedly fail to prevent cascading failures.",

            "How do asynchronous queues improve resilience?":
                "Message queues decouple services so upstream systems continue working when downstream services slow down."
        }

        return expansions.get(query, query)