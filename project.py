import requests
from bs4 import BeautifulSoup
import json

url = "https://www.panamericana.com.co/audifonos-tipo-diadema-bass-13-686721/p"
headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, "html.parser")

    # Encuentra TODOS los bloques JSON en el HTML
    scripts = soup.find_all("script", type="application/ld+json")

    for script in scripts:
        try:
            data = json.loads(script.string)
            # Solo procesamos si es un producto
            if data.get("@type") == "Product":
                print(data)
        except (json.JSONDecodeError, TypeError):
            continue  # Si el bloque no es un JSON válido, lo ignoramos
else:
    print(f"❌ Error al cargar la página. Código: {response.status_code}")
