import re

normalisasi = {
    "gk":"tidak","ga":"tidak","gak":"tidak","nggak":"tidak","enggak":"tidak",
    "tdk":"tidak","tak":"tidak","gx":"tidak","kagak":"tidak","kaga":"tidak",
    "udh":"sudah","udah":"sudah","blm":"belum","belom":"belum",
    "lg":"lagi","sgt":"sangat",
    "yg":"yang","dg":"dengan","dgn":"dengan",
    "knpa":"kenapa","krena":"karena",
    "jd":"jadi","jdi":"jadi","pdhl":"padahal","hrs":"harus",
    "bgt":"banget","bgtt":"banget","bangettt":"banget","parahh":"parah",
    "bener":"benar","bnr":"benar","bnyk":"banyak","byk":"banyak",
    "sm":"sama","tp":"tapi","tpi":"tapi","krn":"karena","jg":"juga",
    "aja":"saja","aj":"saja",
    "mantab":"mantap","mantul":"mantap",
    "eror":"error","erorr":"error",
    "beyond":"byond","byon":"byond","bion":"byond"
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"[^a-z\s]", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text

def normalize_repeated_char(text):
    return re.sub(r'(.)\1{2,}', r'\1', text)

def normalize_text(text):
    tokens = text.split()
    tokens = [normalisasi[t] if t in normalisasi else t for t in tokens]
    return ' '.join(tokens)

def preprocess(text):
    text = clean_text(text)
    text = normalize_repeated_char(text)
    text = normalize_text(text)
    return text
