import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
from huggingface_hub import hf_hub_download

LABELS = {0: "Negatif", 1: "Netral", 2: "Positif"}

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# BASE MODEL (ARSITEKTUR)
BASE_MODEL = "indobenchmark/indobert-base-p1"

# FILE MODEL KAMU DI HUGGINGFACE
REPO_ID = "dheaathallah/indobert_byond"
FILENAME = "best_indobert_model.pth"

# LOAD TOKENIZER & MODEL BASE
tokenizer = AutoTokenizer.from_pretrained(BASE_MODEL)
model = AutoModelForSequenceClassification.from_pretrained(
    BASE_MODEL,
    num_labels=3
)

# DOWNLOAD & LOAD BOBOT KAMU
model_path = hf_hub_download(repo_id=REPO_ID, filename=FILENAME)
state_dict = torch.load(model_path, map_location=device)
model.load_state_dict(state_dict)

model.to(device)
model.eval()

def predict_sentiment(texts):
    inputs = tokenizer(
        texts,
        padding=True,
        truncation=True,
        max_length=128,
        return_tensors="pt"
    ).to(device)

    with torch.no_grad():
        outputs = model(**inputs)
        preds = torch.argmax(outputs.logits, dim=1)

    return [LABELS[p.item()] for p in preds]
