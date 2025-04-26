from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from PIL import Image
import io

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API de Redimensionar Imagen funcionando"}

@app.post("/resize/")
async def resize_image(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    
    resized_image = image.resize((300, 300))  # Puedes cambiar tamaño aquí
    
    img_bytes = io.BytesIO()
    resized_image.save(img_bytes, format="PNG")
    img_bytes.seek(0)
    
    return StreamingResponse(img_bytes, media_type="image/png")
