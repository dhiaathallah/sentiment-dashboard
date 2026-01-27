import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from utils.preprocessing import preprocess
from utils.predict import predict_sentiment

st.set_page_config(page_title="Dashboard Analisis Sentimen", layout="wide")

st.title("📊 Dashboard Analisis Sentimen")

option = st.radio(
    "Pilih metode input:",
    ("Upload Data (CSV / XLSX)", "Ketik Manual")
)

texts = []

if option == "Upload Data (CSV / XLSX)":
    file = st.file_uploader("Upload file", type=["csv", "xlsx"])
    if file:
        if file.name.endswith(".csv"):
            df = pd.read_csv(file)
        else:
            df = pd.read_excel(file)

        text_column = st.selectbox("Pilih kolom ulasan", df.columns)
        texts = df[text_column].astype(str).tolist()

else:
    user_text = st.text_area("Masukkan ulasan:")
    if user_text:
        texts = [user_text]

if st.button("🔍 Analisis") and texts:
    with st.spinner("Sedang memproses..."):
        processed = [preprocess(t) for t in texts]
        labels = predict_sentiment(processed)

    result_df = pd.DataFrame({
        "Ulasan": texts,
        "Sentimen": labels
    })

    st.subheader("📋 Hasil Klasifikasi")
    st.dataframe(result_df)

    csv = result_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="⬇️ Download CSV",
        data=csv,
        file_name="hasil_sentimen.csv",
        mime="text/csv"
    )

    import io

    buffer = io.BytesIO()
    with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
        result_df.to_excel(writer, index=False, sheet_name="Hasil Sentimen")

    st.download_button(
        label="⬇️ Download XLSX",
        data=buffer,
        file_name="hasil_sentimen.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )


    # Pie chart
    st.subheader("📈 Distribusi Sentimen")
    counts = result_df["Sentimen"].value_counts()
    colors = {
    "Positif": "#2ecc71",
    "Netral": "#f1c40f",
    "Negatif": "#e74c3c"
    }

    pie_colors = [colors[label] for label in counts.index]

    fig, ax = plt.subplots()
    ax.pie(
        counts,
        labels=[f"{l} ({counts[l]})" for l in counts.index],
        autopct="%1.1f%%",
        startangle=90,
        colors=pie_colors
    )
    ax.axis("equal")
    st.pyplot(fig)

    # Wordcloud
    st.subheader("☁️ Wordcloud per Kelas")
    for label in counts.index:
        text = " ".join(result_df[result_df["Sentimen"] == label]["Ulasan"])
        color_map = {
            "Positif": "Greens",
            "Netral": "YlOrBr",
            "Negatif": "Reds"
        }

        wc = WordCloud(
            width=800,
            height=400,
            background_color="white",
            colormap=color_map[label]
        )

        st.markdown(f"### {label}")
        st.image(wc.to_array())