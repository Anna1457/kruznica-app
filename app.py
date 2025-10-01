import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from reportlab.pdfgen import canvas

# -------------------------------------------------
# Nadpis
# -------------------------------------------------
st.title("Kružnica a jej body")

# -------------------------------------------------
# Vstupy od používateľa
# -------------------------------------------------
x0 = st.number_input("Súradnica stredu X", value=0.0)
y0 = st.number_input("Súradnica stredu Y", value=0.0)
r = st.number_input("Polomer (m)", value=5.0)
n = st.number_input("Počet bodov na kružnici", value=8, step=1)
color = st.color_picker("Farba bodov", "#ff0000")

# -------------------------------------------------
# Výpočet bodov
# -------------------------------------------------
theta = np.linspace(0, 2*np.pi, int(n), endpoint=False)
x = x0 + r * np.cos(theta)
y = y0 + r * np.sin(theta)

# -------------------------------------------------
# Vykreslenie grafu
# -------------------------------------------------
fig, ax = plt.subplots()
ax.scatter(x, y, color=color, label="Body na kružnici")
circle = plt.Circle((x0, y0), r, fill=False, linestyle="--", label="Kružnica")
ax.add_patch(circle)

ax.set_xlabel("x (m)")
ax.set_ylabel("y (m)")
ax.set_aspect("equal")
ax.legend()

# nastavíme rozsah, aby to bolo pekne vidno
ax.set_xlim(x0 - r*1.5, x0 + r*1.5)
ax.set_ylim(y0 - r*1.5, y0 + r*1.5)

st.pyplot(fig)

# -------------------------------------------------
# Sidebar s informáciami
# -------------------------------------------------
st.sidebar.title("O projekte")
st.sidebar.write(" Autor: Anna Drozdová")
st.sidebar.write(" Predmet: Informatika")
st.sidebar.write(" Technológie: Python, Streamlit, Matplotlib, NumPy, ReportLab")
st.sidebar.write(" Kontakt: 277753@vutbr.cz")

# -------------------------------------------------
# Export do PDF
# -------------------------------------------------
if st.button("Exportovať do PDF"):
    c = canvas.Canvas("vystup.pdf")
    c.setFont("Helvetica", 12)
    c.drawString(100, 800, "Výsledok úlohy - Kružnica a jej body")
    c.drawString(100, 770, f"Stred kružnice: ({x0}, {y0})")
    c.drawString(100, 750, f"Polomer: {r} m")
    c.drawString(100, 730, f"Počet bodov: {n}")
    c.drawString(100, 710, f"Farba bodov: {color}")
    c.drawString(100, 680, "Autor: Anička")
    c.drawString(100, 660, "Predmet: Informatika")
    c.save()
    st.success("✅ PDF bolo uložené ako vystup.pdf v tomto priečinku")
