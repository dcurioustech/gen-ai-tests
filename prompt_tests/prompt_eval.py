# Prompt Evaluation Demo using BERTScore and Cosine Similarity

# 📥 Import Libraries
from bert_score import score
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 🔧 Initialize SentenceTransformer Model
model = SentenceTransformer('all-MiniLM-L6-v2')

# 🧠 Sample Data
examples = [
    {
        "prompt": "What is the capital of France?",
        "expected_answer": "Paris is the capital of France.",
        "generated_answer": "The capital of France is Paris."
    },
    {
        "prompt": "Explain the process of photosynthesis.",
        "expected_answer": "Photosynthesis is the process by which green plants convert sunlight into energy.",
        "generated_answer": "Plants make energy using sunlight, a process called photosynthesis."
    },
    {
        "prompt": "Who wrote 'Pride and Prejudice'?",
        "expected_answer": "Jane Austen wrote 'Pride and Prejudice'.",
        "generated_answer": "The author of Pride and Prejudice is Jane Austen."
    }
]

# 🧪 BERTScore Evaluation Function
def evaluate_bertscore(candidate, reference):
    P, R, F1 = score([candidate], [reference], lang="en", verbose=False)
    return F1[0].item()

# 🧪 Cosine Similarity Evaluation Function
def evaluate_cosine_similarity(candidate, reference):
    embeddings = model.encode([candidate, reference])
    cos_sim = cosine_similarity([embeddings[0]], [embeddings[1]])
    return cos_sim[0][0]

# 📊 Evaluation Runner
def evaluate(prompt, expected, generated):
    print(f"Prompt: {prompt}")
    print(f"Expected Answer: {expected}")
    print(f"Generated Answer: {generated}")

    bertscore = evaluate_bertscore(generated, expected)
    cos_sim = evaluate_cosine_similarity(generated, expected)

    print(f"\nBERTScore F1: {bertscore:.4f}")
    print("A BERTScore F1 score close to 1 indicates high semantic similarity.")
    print(f"Cosine Similarity: {cos_sim:.4f}")
    print("A Cosine score close to 1 indicates high semantic similarity.")
    print("-" * 50)

# 🚀 Run Evaluation on Examples
for example in examples:
    evaluate(example["prompt"], example["expected_answer"], example["generated_answer"])
