# Retrieval Baseline Results

- Date: 2026-11-05
- Retrieval method: character-level TF-IDF with cosine similarity
- Documents: 6 NovaDesk Markdown documents
- Questions: 10
- Result: 10/10 expected source files appeared in the top 3 results

## Observations

- The expected source file appeared in the top 3 results for every test question.
- A document can appear multiple times because different paragraphs from the same file are ranked separately.
- Document titles may appear as retrieval results because headings are currently treated as chunks.