# Semantic RAG and Vector Search Assessment

## Overview

This project implements a local semantic retrieval benchmark system over a technical text corpus.

The objective is to compare two retrieval strategies:

### Strategy A — Raw Vector Search
The user query is directly embedded and used for semantic retrieval.

### Strategy B — Query Expansion
The user query is first rewritten into a richer semantic form before embedding-based retrieval.

---

## Architecture

### 1. Data ingestion
A small local corpus of technical paragraphs is loaded.

### 2. Embedding generation
Each text chunk is converted into a dense semantic vector using sentence-transformers.

### 3. Vector retrieval
The query is embedded and compared against document vectors.

### 4. Top-k retrieval
The system returns the top 3 most relevant chunks.

### 5. Benchmarking
Strategy A and Strategy B retrieval outputs are compared.

---

## Project Structure

```text
data/
src/
tests/
benchmark_output.json
retrieval_benchmark.md
README.md