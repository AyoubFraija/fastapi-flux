import requests

url = "http://localhost:8000/generate-image/"
data = {
    # Realistic photo of an ID photo of a brown-haired woman around 40 years old.
    # Realistic photo of a passport-style photo of a woman with short blonde hair in her early 40s
    # High-quality ID photo of a man with dark skin and a bald head, around 35 years old.

    #prompts:
    # Realistic photo of a passport-style photo of a woman with short blonde hair in her early 40s.
    # High-quality ID photo of a man with dark skin and a bald head, around 35 years old.
    # Professional photo of a middle-aged woman with curly red hair, wearing glasses, taken for identification purposes.
    # Realistic ID-style photo of a man with a trimmed beard and straight black hair, around 45 years old.
    #Portrait-style photo of a woman in her late 30s with shoulder-length brown hair, wearing a neutral expression,
    "prompt": "Professional photo of a middle-aged woman with curly red hair, wearing glasses, taken for identification purposes. \"FLUX 1.1 Pro\"",
    "prompt_upsampling": True
}

# Générer une image
response = requests.post(url, json=data)

# Récupérer le nom du fichier depuis les headers
filename = response.headers['Content-Disposition'].split('filename=')[1]

# Sauvegarder l'image reçue
with open(filename, "wb") as f:
    f.write(response.content)

# Lister toutes les images générées
response = requests.get("http://localhost:8000/list-images")
print(response.json())

# curl -X POST http://localhost:8000/generate-image/ \
# -H "Content-Type: application/json" \
# -d '{"prompt": "Realistic photo of a passport-style photo of a woman with short blonde hair in her early 40s \"FLUX 1.1 Pro\"", "prompt_upsampling": true}' \
# --output image_generee.png

# --version1
# import requests

# url = "http://localhost:8000/generate-image/"
# data = {
#     "prompt": "photo realiste d'une photo d'identite  d'un homme  de 20 ans, fond noir, haute  \"FLUX 1.1 Pro\"",
#     "prompt_upsampling": True
# }

# response = requests.post(url, json=data)

# # Sauvegarder l'image reçue en PNG
# with open("image_generee.png", "wb") as f:
#     f.write(response.content)