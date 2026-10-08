from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
import httpx
import os

app = FastAPI(
    title="Quran API (Text & Audio)",
    description="قرآن کا سادا ٹیکسٹ اور آڈیو تلاوت فراہم کرنے والی پبلک API اور ویب پورٹل"
)

# سٹیٹک فولڈر کو ماؤنٹ کرنا (HTML/CSS کے لیے)
app.mount("/static", StaticFiles(directory="static"), name="static")

# ہوم پیج پر index.html دکھانے کے لیے
@app.get("/", response_class=HTMLResponse)
async def home_page():
    path = os.path.join("static", "index.html")
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>index.html فائل نہیں ملی! براہ کرم static فولڈر چیک کریں۔</h1>"

# --- QURAN TEXT ROUTES ---

@app.get("/quran/ayah/{ayah_key}")
async def get_quran_ayah(ayah_key: str):
    url = f"https://api.alquran.cloud/v1/ayah/{ayah_key}/quran-simple"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()

@app.get("/quran/surah/{surah_number}")
async def get_quran_surah(surah_number: int):
    url = f"https://api.alquran.cloud/v1/surah/{surah_number}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()

@app.get("/quran/juz/{juz_number}")
async def get_quran_juz(juz_number: int):
    url = f"https://api.alquran.cloud/v1/juz/{juz_number}"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()


# --- QURAN AUDIO ROUTES ---

@app.get("/quran/ayah/audio/{ayah_key}")
async def get_quran_ayah_audio(ayah_key: str):
    url = f"https://api.alquran.cloud/v1/ayah/{ayah_key}/ar.alafasy"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()

@app.get("/quran/surah/audio/{surah_number}")
async def get_quran_surah_audio(surah_number: int):
    url = f"https://api.alquran.cloud/v1/surah/{surah_number}/ar.alafasy"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()

@app.get("/quran/juz/audio/{juz_number}")
async def get_quran_juz_audio(juz_number: int):
    url = f"https://api.alquran.cloud/v1/juz/{juz_number}/ar.alafasy"
    async with httpx.AsyncClient() as client:
        response = await client.get(url)
    return response.json()