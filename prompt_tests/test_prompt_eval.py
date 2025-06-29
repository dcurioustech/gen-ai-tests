import pytest
from prompt_eval import evaluate_bertscore, evaluate_cosine_similarity

def test_bertscore_identical():
    s = "The quick brown fox jumps over the lazy dog."
    score = evaluate_bertscore(s, s)
    print(f"BERTScore between identical sentences: {score}")
    assert score == pytest.approx(1.0, abs=0.05)

def test_bertscore_unrelated():
    s1 = "The quick brown fox jumps over the lazy dog."
    s2 = "Quantum mechanics describes the behavior of particles at atomic scales."
    score = evaluate_bertscore(s1, s2)
    print(f"BERTScore between unrelated sentences: {score}")
    assert score < 0.8

def test_cosine_similarity_identical():
    s = "The quick brown fox jumps over the lazy dog."
    sim = evaluate_cosine_similarity(s, s)
    print(f"Cosine similarity between identical sentences: {sim}")
    assert sim == pytest.approx(1.0, abs=0.01)

def test_cosine_similarity_unrelated():
    s1 = "The quick brown fox jumps over the lazy dog."
    s2 = "Photosynthesis occurs in plants."
    sim = evaluate_cosine_similarity(s1, s2)
    print(f"Cosine similarity between unrelated sentences: {sim}")
    assert sim < 0.8
