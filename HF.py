from transformers import pipeline

# Load zero-shot classification pipeline with GPU
classifier = pipeline(
    "zero-shot-classification", 
    model="facebook/bart-large-mnli",
    device=0  # Use GPU (0 = first GPU, -1 = CPU)
)

# Define candidate labels (contexts)
candidate_labels = ["Positive Long-Lasting", "Positive Buildable Coverage", "Positive Blends Well", "Positive Lightweight", "Positive Hydrating", "Negative Oxidizes", "Negative Cakey", "Use Cases Everyday Wear", "Use Cases Oily Skin", "Use Cases Natural Look"]


# Classify text
result = classifier(
    "Absolutely one of the nicest foundations Add a nice glow Aging skin Air Brushed feeling Air Brushed look All day hydrating skin ...", 
    candidate_labels
)
# print(result)
for i in result['labels']:
    print(i)
