adresses = {
    "0xb472211455322d3830f4aF4FF05A9ACb722B963d",
    "0x4062AE907bfEB248a5aa012438C2d70c8E3f820E",
    "0x0d9b80e13491bfEaa6371deBa696708480967552",
    "0x0A7B2EfdD9b619B4614a8AA4704EA3fAFd56D4c2",
    "0xa28f124b64cbddd06fee4a02cf44b095bc924417",
    "0x04963F034Ff1f184A3398a3550072C651D564590",
    "0x72a481Fbf0D231e91Bb21aCe1E7786b7c0d5CC72",
    "0x221F089078b47C04f1BfB1d4dB2e20C734a18222",
    "0x7967c1641F06A2f5706db0f542FEa3D4eae1DBBF",
    "0x3de11ADe51DBCD0BE4C6e3eC9e0FF6FcE9B17124",
    "0xBd718eb0400D92F212A9E95725BD87bB69033c5C",
    "0xf8bcDeC88068b88B848Fc5322d011EFFE934Ba6D",
    "0xCEeA4b389b4CF5bC3b7f8f9ed3bb52036b4a9b27",
    "0x8603E68F1E7873bD0EdD6bC036aB7DFCF9E1e935",
    "0x603CD4D806B9e25F85a624893C3f460135Dc17Ae",
    "0x75f81784678369d1C71B2EE3C0edAa6E0aFB48Ad",
    "0x6D5a9E3049fe419B4F063f0d8E54c640cA429d8a",
    "0xa63b4B935a3EaF6F0Ab83532a3843741746c5d5B",
    "0xE7929A82A9219cd4CCe88514364Fe30578D8e713"
}

names = {
    "Leticia Dépierraz",
    "Samuel Gergely",
    "Matviy Lyubivyy",
    "Thanavine Le Cocq",
    "Artur Tudor Boykovych",
    "Carlos Rafael Silva Carvalho",
    "Alonzo Pinto Dos Santos Gaspar",
    "Marco Mascellino",
    "Adrien Volery",
    "Anthony Vuagniaux",
    "Amael Jampen",
    "Simon Marakie Awelachew",
    "Deyan Gabriel Tucev",
    "Anderson Mendes Barros",
    "Hugo Rod",
    "Joel Tebe Rovira",
    "Vikki Dolt",
    "Jérémie Chevalley",
    "Chris Brandt"
}

url_rpc = "http://10.229.43.182:8545"

def main():
    print("Envoi de l'ETH")
    print("Choisir une option:")
    print("1. Envoyer de l'ETH")
    print("2. Afficher les adresses et les noms")
    choice = input("Votre choix: ")
    
    if choice == '1':
        # Demander l'adresse de destination et le montant à envoyer
        destination_address = input("Entrez l'adresse de destination: ")
        amount = float(input("Entrez le montant à envoyer (en ETH): "))
        # Appeler la fonction d'envoi d'ETH
        send_eth(destination_address, amount)
    elif choice == '2':
        # Afficher les adresses et les noms
        for address, name in zip(adresses, names):
            print(f"Adresse: {address}, Nom: {name}")
    else:
        print("Choix invalide. Veuillez choisir 1 ou 2.")

main() 