# 🔴 Question 1 :

Pourquoi le montant solde est-il remis à zéro avant l’envoi des fonds (solde = 0; avant le call vers proprietaire) ?

- Faites référence à la sécurité et aux risques spécifiques à Solidity (réentrance).

    Si on ne le faisait pas le solde pourrait risquer de s'additionner à chaque transaction. Et étant donné que le montant envoyé au propriétaire est égal au solde, cela pourrait mener à un envoi de fonds important que le propriétaire n'aurait jamais dû recevoir.

- Donnez un exemple de ce qui pourrait arriver si l’ordre était inversé.

# 🔴 Question 2 :

Quel est le rôle exact de la fonction receive() dans ce contrat ?

- Pourquoi est-elle implémentée ?

- Que se passerait-il si un utilisateur envoyait des Ethers directement au contrat sans utiliser la fonction deposer ?