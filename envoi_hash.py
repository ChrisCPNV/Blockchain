from web3 import Web3
import time

addresses = {
    "Leticia Dépierraz": "0xb472211455322d3830f4aF4FF05A9ACb722B963d",
    "Samuel Gergely": "0x4062AE907bfEB248a5aa012438C2d70c8E3f820E",
    "Matviy Lyubivyy": "0x0d9b80e13491bfEaa6371deBa696708480967552",
    "Thanavine Le Cocq": "0x0A7B2EfdD9b619B4614a8AA4704EA3fAFd56D4c2",
    "Carlos Rafael Silva Carvalho": "0x04963F034Ff1f184A3398a3550072C651D564590",
    "Alonzo Pinto Dos Santos Gaspar": "0x72a481Fbf0D231e91Bb21aCe1E7786b7c0d5CC72",
    "Marco Mascellino": "0x221F089078b47C04f1BfB1d4dB2e20C734a18222",
    "Adrien Volery": "0x7967c1641F06A2f5706db0f542FEa3D4eae1DBBF",
    "Anthony Vuagniaux": "0x3de11ADe51DBCD0BE4C6e3eC9e0FF6FcE9B17124",
    "Amael Jampen": "0xBd718eb0400D92F212A9E95725BD87bB69033c5C",
    "Simon Marakie Awelachew": "0xf8bcDeC88068b88B848Fc5322d011EFFE934Ba6D",
    "Deyan Gabriel Tucev": "0xCEeA4b389b4CF5bC3b7f8f9ed3bb52036b4a9b27",
    "Anderson Mendes Barros": "0x8603E68F1E7873bD0EdD6bC036aB7DFCF9E1e935",
    "Hugo Rod": "0x603CD4D806B9e25F85a624893C3f460135Dc17Ae",
    "Joel Tebe Rovira": "0x75f81784678369d1C71B2EE3C0edAa6E0aFB48Ad",
    "Vikki Dolt": "0x6D5a9E3049fe419B4F063f0d8E54c640cA429d8a",
    "Jérémie Chevalley": "0xa63b4B935a3EaF6F0Ab83532a3843741746c5d5B",
    "Chris Brandt": "0xE7929A82A9219cd4CCe88514364Fe30578D8e713",
    "public": "0x0000000000000000000000000000000000000000"
}

from_address = "0xE7929A82A9219cd4CCe88514364Fe30578D8e713"
private_key = "0acf4c3f377ab35f9217761ed198f2525687ea6769482d85859f7c7a0f1fac32"

amount_to_send = 0.1

def send_metadata():
    w3 = Web3(Web3.HTTPProvider("http://10.229.43.182:8545"))

    if not w3.is_connected():
        print("Erreur de connexion à l'API RPC.")
        return None
    
    nonce = w3.eth.get_transaction_count(from_address)

    metadata = {
        'name': 'pdf_file',
        'hash': '91c7360e7383436ef5c69a65286a249b9af9dec30076837fe3c8de6cb5b87761',
        'description': 'Hash du fichier pdf',
        'path': r'C:\Users\pl52dsy\Documents\deuxieme\Trimestre4\I107\hashpdf_Chris.pdf'
    }

    metadata_hex = w3.to_hex(str(metadata).encode('utf-8'))

    transaction = {
        'from': from_address,
        'to': "0x0000000000000000000000000000000000000000",
        'value': 0,
        'gas': 2000000,
        'gasPrice': w3.to_wei('20', 'gwei'),
        'nonce': nonce,
        'chainId': 32383,
        'data': metadata_hex
    }

    signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
    txn_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)

    print(f"Transaction envoyée à la blockchain avec le hash: {txn_hash.hex()}")

def send_eth_all(amount):
    w3 = Web3(Web3.HTTPProvider("http://10.229.43.182:8545"))

    if not w3.is_connected():
        print("Erreur de connexion à l'API RPC.")
        return None
    
    amount_wei = w3.to_wei(amount, 'ether')
    nonce = w3.eth.get_transaction_count(from_address)

    for index, address in addresses.items():

        transaction = {
            'to': address,
            'value': amount_wei,
            'gas': 2000000,
            'gasPrice': w3.to_wei('20', 'gwei'),
            'nonce': nonce,
            'chainId': 32383
        }

        signed_txn = w3.eth.account.sign_transaction(transaction, private_key)
        txn_hash = w3.eth.send_raw_transaction(signed_txn.raw_transaction)

        print(f"Transaction envoyée à: {index} avec le hash: {txn_hash.hex()}")
        nonce += 1

def get_balance(address):
    # Créer une instance de Web3
    w3 = Web3(Web3.HTTPProvider("http://10.229.43.182:8545"))
    
    # Vérifier si la connexion est établie
    if not w3.is_connected():
        print("Erreur de connexion à l'API RPC.")
        return None
    
    # Obtenir le solde d'une adresse
    balance = w3.eth.get_balance(address)
    
    # Convertir le solde en Ether
    ether_balance = w3.from_wei(balance, 'ether')
    
    return ether_balance

def get_metadata(adresse):
    # Créer une instance de Web3
    w3 = Web3(Web3.HTTPProvider("http://10.229.43.182:8545"))
    
    # Vérifier si la connexion est établie
    if not w3.is_connected():
        print("Erreur de connexion à l'API RPC.")
        return None
    
    block_end = w3.eth.block_number

    for block_number in range(0, block_end + 1):
        try:
            block = w3.eth.get_block(block_number, full_transactions=True)
            for transaction_hash in block.transactions:
                if transaction_hash.input and transaction_hash.input != '0x' and transaction_hash['from'] == adresse:
                    print(f"Transaction trouvée dans le bloc {block_number}:")
                    print(f"Hash de la transaction: {transaction_hash.hash.hex()}")
                    print(f"Données: {transaction_hash.input}")
                    print(f"Valeur: {w3.from_wei(transaction_hash.value, 'ether')} ETH")
                    print(f"Nonce: {transaction_hash.nonce}")
                    print("---------------------------------------------------")

            if block_number % 100 == 0:
                print(f"--> Jusqu'au bloc {block_number}")
                time.sleep(0.05)  # Pause pour éviter de surcharger le noeud


        except Exception as e:
            print(f"Erreur lors de la récupération des transactions du bloc {block_number}: {e}")

def main():
    print("Envoi de l'ETH")
    print("Choisir une option:")
    print("1. Envoyer de l'ETH")
    print("2. Afficher les soldes")
    print("3. Envoie de metadatas à la blockchain")
    print("4. Récupérer des metadatas")
    choice = input("Votre choix: ")
    
    if choice == '1':
        send_eth_all(amount_to_send)
    elif choice == '2':
        # Afficher les adresses et les noms ainsi que la balance
        for name, address in addresses.items():
            print(f"{name}: {address} - Solde: {get_balance(address)} ETH")
    elif choice == '3':
        send_metadata()
    elif choice == '4':
        # Demander à l'utilisateur de choisir une adresse
        from_address = input("Entrez l'adresse pour récupérer les métadonnées: ")
        get_metadata(from_address)
    else:
        print("Choix invalide. Veuillez choisir 1 ou 2.")

main() 