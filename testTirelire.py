from web3 import Web3
import json
import time

# --- Configuration ---
w3 = Web3(Web3.HTTPProvider("http://10.229.43.182:8545"))

if not w3.is_connected():
    raise Exception("Erreur : Impossible de se connecter au nœud Ethereum")

deployer_address = "0xE7929A82A9219cd4CCe88514364Fe30578D8e713"
private_key = "0acf4c3f377ab35f9217761ed198f2525687ea6769482d85859f7c7a0f1fac32"
sender_address = w3.to_checksum_address(deployer_address)

contract_address = w3.to_checksum_address("0xbF406238980f21B34C33313c2347da3b0d5BC198")  # ← Ton contrat
with open("TirelireMonoUtilisateur.abi", "r") as abi_file:
    contract_abi = json.load(abi_file)

contract = w3.eth.contract(address=contract_address, abi=contract_abi)


# --- FONCTION : Déposer ---
def deposer(montant_eth: float, delai_en_secondes: int):
    date_retrait_timestamp = int(time.time()) + delai_en_secondes
    montant_wei = w3.to_wei(montant_eth, "ether")
    nonce = w3.eth.get_transaction_count(sender_address)

    tx = contract.functions.deposer(date_retrait_timestamp).build_transaction({
        'from': sender_address,
        'value': montant_wei,
        'gas': 200000,
        'gasPrice': w3.to_wei('20', 'gwei'),
        'nonce': nonce,
        'chainId': 32383,
    })

    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(f"Dépôt envoyé : {tx_hash.hex()}")
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Dépôt confirmé sur la blockchain.")
    print(f"Date de retrait fixée à : {date_retrait_timestamp} (heure Unix)")


# --- FONCTION : Retirer ---
def retirer():
    date_retrait = contract.functions.getDateRetrait().call()
    heure_actuelle = int(time.time())

    print(f"Date retrait fixée : {date_retrait}")
    print(f"Heure actuelle : {heure_actuelle}")

    if heure_actuelle < date_retrait:
        secondes_restantes = date_retrait - heure_actuelle
        print(f"Trop tôt pour retirer. Reviens dans {secondes_restantes} secondes.")
        return

    nonce = w3.eth.get_transaction_count(sender_address)
    tx = contract.functions.retirer().build_transaction({
        'from': sender_address,
        'gas': 150000,
        'gasPrice': w3.to_wei('20', 'gwei'),
        'nonce': nonce,
        'chainId': 32383,
    })

    signed_tx = w3.eth.account.sign_transaction(tx, private_key)
    tx_hash = w3.eth.send_raw_transaction(signed_tx.raw_transaction)
    print(f"Retrait envoyé : {tx_hash.hex()}")
    w3.eth.wait_for_transaction_receipt(tx_hash)
    print("Retrait confirmé sur la blockchain.")


# --- EXÉCUTION ---
if __name__ == "__main__":
    choix = input("Souhaitez-vous faire un dépôt ? (y/n) ").strip().lower()
    if choix == "y":
        montant = float(input("Montant en ETH : "))
        delai = int(input("Délai de blocage en secondes : "))
        deposer(montant, delai)

    choix2 = input("Souhaitez-vous tenter un retrait ? (y/n) ").strip().lower()
    if choix2 == "y":
        retirer()
