# 🔴 Question 1 :

Pourquoi le montant solde est-il remis à zéro avant l’envoi des fonds (solde = 0; avant le call vers proprietaire) ?

- Faites référence à la sécurité et aux risques spécifiques à Solidity (réentrance).

    Si on ne le faisait pas le solde pourrait risquer de s'additionner à chaque transaction. Et étant donné que le montant envoyé au propriétaire est égal au solde, cela pourrait mener à un envoi de fonds important que le propriétaire n'aurait jamais dû recevoir.

- Donnez un exemple de ce qui pourrait arriver si l’ordre était inversé.

    Si une personne réussit à faire crash le contrat juste après l'envoi etavant la remise du solde à 0, il pourrait techniquement dupliquer ses fonds.

# 🔴 Question 2 :

Quel est le rôle exact de la fonction receive() dans ce contrat ?

- Pourquoi est-elle implémentée ?

    C'est une fonction fallback, si la fonction permettant le depos ou l'envoi de fond crash pour une raison ou une autre, c'est cette fonction qui sera appelé pour que les fonds ne soit pas perdu et revienne au propriétaire.

- Que se passerait-il si un utilisateur envoyait des Ethers directement au contrat sans utiliser la fonction deposer ?

    Le contrat n'étant pas utiliser, la personne envoyant les fonds ne serait pas marqué comme propriétaire par le contrat et les fonds seraient perdu.