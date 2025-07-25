import requests
from bs4 import BeautifulSoup
import re

# Premiere fonction pour crawl le site
def crawl(url):
    print(f"ByteSpider Crawling : {url}...")
    # Ping du site
    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    #Récupérer le code html de la page
    length = len(response.text)
    print(f"HTML récupéré : {length} éléments")
    #Stocker le resultat pour analyse
    out = response.text

    #LIENS 
    links = find_links(out)
    print(f"Liens trouvés :")
    for link in links:
        print(link)

    #EMAILS 
    emails = find_emails(out)
    print(f"Emails trouvés :")
    for email in emails:
        print(email)

    #PHONES 
    phones = find_phones(out)
    print(f"Téléphones trouvés :")
    for phone in phones:
        print(phone)

    #REPORT 
    report(url, response.status_code, links, emails, phones)

def find_links(html_content):
    # Création de l'arbre DOM
    soup = BeautifulSoup(html_content, 'html.parser')
    links = []
    for a_tag in soup.find_all('a'):
        #Ici on récupère la balise href, donc le lien
        href = a_tag.get('href')
        #On ajoute le lien a notre tableau links
        links.append(href)
    return links

def find_emails(out):
    email_pattern = r"[-A-Za-z0-9!#$%&'*+/=?^_`{|}~]+" \
                    r"(?:\.[-A-Za-z0-9!#$%&'*+/=?^_`{|}~]+)*" \
                    r"@(?:[A-Za-z0-9](?:[-A-Za-z0-9]*[A-Za-z0-9])?\.)+" \
                    r"[A-Za-z0-9](?:[-A-Za-z0-9]*[A-Za-z0-9])?"
    emails = re.findall(email_pattern, out)
    return emails

def find_phones(out):
        phone_pattern = r'(?:\+33\s?|0)[1-9](?:[\s-]?\d{2}){4}'
        phones = re.findall(phone_pattern, out)
        return phones

def report(url, status_code, links, emails, phones, filename="rapport.txt"):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write("===== Rapport ByteSpider =====\n")
        f.write(f"URL crawlée        : {url}\n")
        f.write(f"Code HTTP          : {status_code}\n\n")

        f.write("---- Liens trouvés ----\n")
        if links:
            for link in links:
                f.write(f"- {link}\n")
        else:
            f.write("Aucun lien trouvé.\n")
        f.write("\n")

        f.write("---- Emails trouvés ----\n")
        if emails:
            for email in emails:
                f.write(f"- {email}\n")
        else:
            f.write("Aucun email trouvé.\n")
        f.write("\n")

        f.write("---- Téléphones trouvés ----\n")
        if phones:
            for phone in phones:
                f.write(f"- {phone}\n")
        else:
            f.write("Aucun numéro trouvé.\n")
        f.write("\n")

    print(f"\n✅ Rapport enregistré dans '{filename}'")

# Saisie utilisateur url
user_url = input("Entrer l'url à crawler : ")
crawl(user_url)
