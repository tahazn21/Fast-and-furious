# Lecture du code HTML depuis le fichier txt
with open('code_html.txt', 'r') as code_file:
    code_html = code_file.read()

# Création des 100 fichiers HTML
for i in range(1, 101):
    nom_fichier = f'film{i}.html'
    with open(nom_fichier, 'w') as html_file:
        html_file.write(code_html)

print("Création des fichiers HTML terminée.")
