# save.py permet de garder un historique des scores des joueurs et de les implémenter dans un fichier json

import json
import sys
import os

# Fonction pour ajouter un nouveau score au fichier JSON
def ajouter_score(score, pseudo):
    if os.path.exists("score.json"):
        with open("score.json", "r") as fichier_json:
            try:
                data = json.load(fichier_json)
            except json.JSONDecodeError:
                data = {"scores": []}
    else:
        data = {"scores": []}

    if "scores" not in data:
        data["scores"] = []

    nouveau_score = {
        "score": score,
        "pseudo": pseudo
    }

    data["scores"].append(nouveau_score)

    with open("score.json", "w") as fichier_json:
        json.dump(data, fichier_json, indent=4)

def main():
    if len(sys.argv) != 3:
        print("Utilisation : python save.py <score> <pseudo>")
        sys.exit(1)

    score = int(sys.argv[1])
    pseudo = sys.argv[2]

    # Ajouter le nouveau score au fichier JSON
    ajouter_score(score, pseudo)
    print("Nouveau score ajouté avec succès.")

if __name__ == "__main__":
    main()
