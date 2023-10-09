import json
import sys


class ScoreRepository:
    """Classe pour gérer la sauvegarde des scores dans un fichier JSON"""

    def __init__(self, fichier):
        self.fichier = fichier

    def obtenir_donnees(self):
        """Lit les données depuis le fichier JSON"""
        try:
            with open(self.fichier) as f:
                return json.load(f)
        except FileNotFoundError:
            return {"scores": []}
        except json.JSONDecodeError:
            return {"scores": []}

    def ajouter_score(self, score, pseudo):
        """Ajoute un nouveau score au fichier JSON

        Arguments:
            score (int): Score à ajouter
            pseudo (str): Pseudo du joueur

        Retourne:
            dict: Données mises à jour
        """
        donnees = self.obtenir_donnees()

        nouveau_score = {
            "score": score,
            "pseudo": pseudo
        }

        donnees["scores"].append(nouveau_score)

        self.ecrire_donnees(donnees)

        return donnees

    def ecrire_donnees(self, donnees):
        """Ecrit les données dans le fichier JSON"""
        with open(self.fichier, "w") as f:
            json.dump(donnees, f, indent=4)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Utilisation : python save.py <score> <pseudo>")
        sys.exit(1)

    score = int(sys.argv[1])
    pseudo = sys.argv[2]

    repo = ScoreRepository("scores.json")
    donnees = repo.ajouter_score(score, pseudo)
    print("Nouveau score ajouté !")
    print(donnees)