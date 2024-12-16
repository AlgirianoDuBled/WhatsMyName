import requests
from bs4 import BeautifulSoup

def get_name_meaning(name):
    # Maak de zoek-URL aan
    url = f"https://en.wikipedia.org/wiki/{name}"
    
    # Voer de HTTP-aanroep uit
    response = requests.get(url)
    
    # Controleer of de aanroep succesvol was
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Zoek naar de eerste paragraaf die meestal de betekenis bevat
        paragraphs = soup.find_all('p')
        if paragraphs:
            meaning = paragraphs[0].text
            return meaning
        else:
            return "Geen betekenis gevonden."
    else:
        return "Naam niet gevonden."

# Voorbeeld om een naam op te zoeken
name = input("Voer de naam in: ")
meaning = get_name_meaning(name)
print(f"Betekenis van {name}: {meaning}")
