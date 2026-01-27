import os
import torch
import gdown
from transformers import BertTokenizer, BertForSequenceClassification

LABELS = {0: "Negatif", 1: "Netral", 2: "Positif"}

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# ===== 1) DOWNLOAD MODEL DARI GOOGLE DRIVE =====
MODEL_PATH = "best_indobert_model.pth"
DRIVE_ID = "1vvsdd0JC3CDSiOCsjWY-7XrXSuqMujpT"

if not os.path.exists(MODEL_PATH):
    url = f"https://drive.google.com/uc?id={DRIVE_ID}"
    gdown.download(url, MODEL_PATH, quiet=False)

# ===== 2) LOAD TOKENIZER & MODEL =====
tokenizer = BertTokenizer.from_pretrained("indobenchmark/indobert-base-p1")

model = BertForSequenceClassification.from_pretrained(
    "indobenchmark/indobert-base-p1",
    num_labels=3
)

model.load_state_dict(torch.load(MODEL_PATH, map_location=device))
model.to(device)
model.eval()

# ===== 3) FUNCTION PREDIKSI =====
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
