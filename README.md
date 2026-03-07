# 🖼️ Billede – jagtbare arter

![Last Commit](https://img.shields.io/github/last-commit/luka2945/Billede?style=for-the-badge)
![Repo Size](https://img.shields.io/github/repo-size/luka2945/Billede?style=for-the-badge)
![GitHub Pages](https://img.shields.io/badge/GitHub%20Pages-Live-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Project-Active-brightgreen?style=for-the-badge)

Dette repository indeholder billeder af danske jagtbare arter, som kan bruges direkte via en offentlig URL.

Projektet bruges primært sammen med jagttids-kalender projektet, men kan også bruges af andre projekter, apps eller hjemmesider.

Alle billeder hostes via GitHub Pages, så de kan tilgås direkte fra internettet.

---

# 🌐 Billed-URL

Alle billeder følger samme URL-struktur:

https://luka2945.github.io/Billede/af/FILNAVN.webp

Eksempler:

https://luka2945.github.io/Billede/af/graaand.webp  
https://luka2945.github.io/Billede/af/ringdue.webp  
https://luka2945.github.io/Billede/af/skovsneppe.webp  
https://luka2945.github.io/Billede/af/raev.webp  

Filnavnet svarer til artens navn skrevet med små bogstaver uden mellemrum.

---

# 📂 Repository struktur

Projektet er opdelt sådan:

input/  
    originale billeder  

af/  
    billeder der publiceres online  

build_urls.py  
    script der genererer URL-oversigt  

urls.json  
    automatisk genereret liste med alle billede-URL'er  

urls.txt  
    simpel tekstliste med alle URL'er  

---

# ⚙️ Generer URL'er automatisk

Scriptet `build_urls.py` bruges til automatisk at:

• finde alle billeder i `input`  
• kopiere dem til `af`  
• generere en oversigt med URL'er  

Kør scriptet sådan:

python build_urls.py

Efterfølgende oprettes automatisk:

af/urls.json  
af/urls.txt  

---

# 📦 urls.json

Denne fil indeholder en komplet oversigt over alle arter og deres billed-URL.

Eksempel:

{
  "graaand": "https://luka2945.github.io/Billede/af/graaand.webp",
  "ringdue": "https://luka2945.github.io/Billede/af/ringdue.webp",
  "skovsneppe": "https://luka2945.github.io/Billede/af/skovsneppe.webp"
}

Dette gør det nemt for andre projekter at hente billeder automatisk.

---

# ➕ Tilføj nye arter

1. Læg billedet i mappen `input`
2. Kør scriptet:

python build_urls.py

3. Upload ændringerne til GitHub

Så bliver billedet automatisk tilgængeligt online.

---

# 🦌 Brug i andre projekter

Billederne kan bruges direkte i fx:

• jagt apps  
• hjemmesider  
• databaser  
• jagt-kalendere  
• GitHub projekter  

Eksempel i HTML:

<img src="https://luka2945.github.io/Billede/af/graaand.webp">

---

# 📜 Kilder

Billeder af arter stammer fra:

https://www.naturporten.dk/leksikon

Danmarkskort over regioner stammer fra:

https://wikitree.com/photo.php/6/6e/Project_Danmark-4.png

Alle rettigheder til billeder tilhører deres respektive ejere.

---

# 👤 Lavet af
Lavet af Lukas Jermiin

GitHub profil
Se projektet

Til brug i jagt- og naturprojekter.
