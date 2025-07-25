# Projet 1 – ByteSpider (Tiny Web Scraper & Recon)

## Rappel des consignes :

**Mission :**  
> Développe un mini web crawler capable de récupérer des pages, d’extraire des liens et de détecter des patterns (emails, endpoints cachés, etc.).  
> Utilise-le pour cartographier un petit site de test.

**Consignes :**

- Crée un script qui explore le site à partir d’une URL de départ.
- Récupère tous les liens internes.
- Cherche des patterns intéressants (emails et numéros de tel).
- Génère un rapport de reconnaissance (infos trouvées).

**Cible** : Site de test en local

## Ma démarche
Ce projet étant le premier projet, il fallait que je mette en place mon environnement de projet. Voici mon environnement : 
- Terminal : Kitty
- Shell : Fish
- IDE : Neovim avec NVChad
- Python 3.13.5
Je suppose que Neovim n'est pas le choix le plus simple mais c'est vraiment fun.

Pour plus de sécurité et d'après la consigne il faut faire tourner le site de test en local. Mon choix s'est naturellement tourné vers Docker pour des raisons de sécu, de facilité ainsi que pour me familiariser un peu plus avec cet outil. Alors on a : 

**Step 1 : Installer Docker**

**Step 2 : Lancer en local l'app avec Docker**

docker run --rm --name test-html -v $PWD/html:/usr/share/nginx/html:ro -p 8080:80 nginx

De ce que j'ai compris :
-  docker run lance un nouveau conteneur
-  --rm surpprime le conteneur une fois stoppé 
-  --name nomme le conteneur
-  -v $PWD/html:/usr/share/nginx/html:ro -> montage de volume qui lie un dossier à un dossier du conteneur
- nginx c'est un serveur web 
- `-p 8080:80`: redirige le port **8080 du conteneur** vers le port **80 de ta machine**

Bon je me rends compte que avoir utilisé Docker a bien compliqué la chose et est un peu overkill.
La prochaine fois j'utiliserais un simple : 
`python3 -m http.server 8080`

Voici l’arborescence de mon répertoire pour ce projet :
<img width="663" height="382" alt="Pasted image 20250725095442" src="https://github.com/user-attachments/assets/777c8186-ee69-491d-9e18-c257eeef4ce4" />

> - byte-spide-test/ html est le fichier cible que je lance en local avec Docker
> - venv signifie Virtual Environment — c’est un environnement Python isolé qui permet de gérer les librairies

Vous aller me dire pourquoi avoir utilisé le virtual environnement encore une fois c'est overkill et vous avez raison ! La prochaines fois j'installerais les librairies sur tout mon système. (Bien que ce soit pas recommandé en contexte d'entreprise par exemple.)

Ok maintenant on a notre environnement de travail et j'ai déjà appris : 
- Pour run en local utiliser python et pas docker
- Ne pas utiliser Virtual Environnement et installer directement les librairies

<img width="924" height="935" alt="Pasted image 20250724102001" src="https://github.com/user-attachments/assets/8c2aa6e1-5b30-4a60-ba35-21869936960a" />

Maintenant je vais attaquer le script en python.

J'avais en tête, au début du projet, de découper le script en 3 fonctions :
- Crawl -> Fonction principal qui va récupérer les données
- Parse -> Qui va analyser et parcourir les données 
- Detect -> Qui va reconnaitre les patternes

J'ai par la suite ajouté 2 fonctions au lieu de detect pour les patternes :
- find_emails
- find_phones

À ce moment là j'ai décider de simplifier mon code en reprenant la consigne :
- On me demande de récupérer les donnés -> Fonction crawl
- On me demande de trouver des liens -> Fonction find_links
- On me demande de trouver des emails -> Fonction find_emails
- On me demande de trouver des phones -> Fonction find_phones
- On me demande de générer un rapport -> Fonction report

J'ai donc une fonction principale qui est la fonction crawl et où je vais appeler toutes mes autres fonctions.

J'ai eu besoin de 3 librairie pour ce projet :
- requests -> récupérer le contenu de la page html
- beautifulsoup4 -> Analyser les données html
- re -> Importe le regex

Pour identifier les patterns j'ai utilisé du regex aka regular expression notamment pour les emails et les téléphones.

Après avoir bien avancé sur mes fonctions voici la sortie du script

<img width="735" height="585" alt="Pasted image 20250724101924" src="https://github.com/user-attachments/assets/314acfd6-cf08-4145-aff6-2f12f3c9736c" />


Enfin je vais avoir une dernière fonction report qui va me servir, comme son nom l'indique à enregistrer un rapport.

<img width="765" height="860" alt="Pasted image 20250724104449" src="https://github.com/user-attachments/assets/4cb9cc19-8bf4-478e-86ed-4bc3d91f2db5" />

Pour ce projet j'ai essayé au maximum de commenter mon code pour comprendre ce que je fais à chaque étape. (En espérant que ça puisse servir !)

## En résumé sur ce projet j'ai appris : 
 
- Mise en place de l'environnement, la prochaine fois pas de docker ni de venv
- Neovim peut ajouter de la complexité au début, mais m’apporte du plaisir à coder
- Refaire du python et utiliser des librairies
- Crawling de données 
- Faire du regex
- Générer un rapport 
- Refactorer mon code à partir de la consigne
