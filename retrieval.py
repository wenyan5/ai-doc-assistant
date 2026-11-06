from pathlib import Path
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


DOCS_DIR = Path(__file__).parent / "docs"


def load_chunks():
    chunks = []

    for file_path in sorted(DOCS_DIR.glob("*.md")):
        content = file_path.read_text(encoding="utf-8").strip()

        paragraphs = [
            paragraph.strip()
            for paragraph in re.split(r"\n\s*\n", content)
            if paragraph.strip()
        ]

        for chunk_id, paragraph in enumerate(paragraphs):
            chunks.append(
                {
                    "filename": file_path.name,
                    "chunk_id": chunk_id,
                    "text": paragraph,
                }
            )

    return chunks


def search_documents(question, top_k=3):
    chunks = load_chunks()

    if not chunks:
        return []

    texts = [chunk["text"] for chunk in chunks]

    vectorizer = TfidfVectorizer(
        analyzer="char",
        ngram_range=(2, 3),
    )

    vectors = vectorizer.fit_transform(texts + [question])

    question_vector = vectors[-1]
    document_vectors = vectors[:-1]

    scores = cosine_similarity(question_vector, document_vectors)[0]
    ranked_indexes = scores.argsort()[::-1][:top_k]

    results = []

    for index in ranked_indexes:
        result = chunks[index].copy()
        result["score"] = round(float(scores[index]), 3)
        results.append(result)

    return results


if __name__ == "__main__":
    question = input("请输入问题：").strip()

    if not question:
        print("问题不能为空。")
    else:
        results = search_documents(question)

        for number, result in enumerate(results, start=1):
            print(f"\n#{number} | {result['filename']} | score={result['score']}")
            print(result["text"])