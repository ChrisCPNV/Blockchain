import hashlib

def main():
    print("Hash Calculator")
    print("Choisisser une option:")
    print("1. Hacher un texte")
    print("2. Hacher un fichier")
    choice = input("Votre choix: ")
    if choice == '1':
        text = """Block5
Isidore envoie 7 à Gary
Bob envoie 30 à Jan
Claire envoie 6 à Handy"""
        hash_value = hashlib.sha256(text.encode()).hexdigest()
        print(f"Le hachage SHA-256 du texte est: {hash_value}")
    elif choice == '2':
        file_path = input("Entrez le chemin du fichier à hacher: ")
        try:
            with open(file_path, 'rb') as file:
                file_data = file.read()
                hash_value = hashlib.sha256(file_data).hexdigest()
                print(f"Le hachage SHA-256 du fichier est: {hash_value}")
        except FileNotFoundError:
            print("Fichier non trouvé. Veuillez vérifier le chemin et réessayer.")
    else:
        print("Choix invalide. Veuillez choisir 1 ou 2.")

main()