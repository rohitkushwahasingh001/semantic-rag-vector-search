# Retrieval Benchmark Report

## Objective

This project evaluates two semantic retrieval strategies over a local technical corpus.

### Strategy A — Raw Vector Search
The original user query is directly embedded and used for vector similarity search.

### Strategy B — Query Expansion
The original query is first rewritten into a more embedding-friendly semantic form, then embedded and searched.

---

## Benchmark Queries

### Query 1
**How does the system handle peak load?**

**Observation:**

- Strategy A retrieved relevant chunks around load balancing and scaling.
- Strategy B ranked autoscaling as the most relevant result.

**Similarity improvement:**

- Strategy A top score: **0.5359**
- Strategy B top score: **0.9954**

---

### Query 2
**What prevents cascading failures in microservices?**

**Observation:**

- Both strategies retrieved the circuit breaker chunk.
- Strategy B produced stronger semantic alignment.

**Similarity improvement:**

- Strategy A top score: **0.7116**
- Strategy B top score: **0.8347**

---

### Query 3
**How do asynchronous queues improve resilience?**

**Observation:**

- Both strategies retrieved the message queue chunk.
- Strategy B improved relevance confidence.

**Similarity improvement:**

- Strategy A top score: **0.6758**
- Strategy B top score: **0.8353**

---

## Why Strategy B performed better

Query expansion introduced semantically related terms such as:

- autoscaling
- traffic spikes
- circuit breakers
- downstream failures

These terms improved alignment between the query embedding and the document embeddings.

---

## Conclusion

Across all benchmark queries, query expansion improved semantic retrieval quality.

It produced:

- higher cosine similarity
- better ranking of relevant chunks
- stronger semantic matching