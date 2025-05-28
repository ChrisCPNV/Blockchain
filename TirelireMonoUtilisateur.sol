// SPDX-License-Identifier: MIT

pragma solidity ^0.8.20;


contract TirelireMonoUtilisateur {

    address public proprietaire;

    uint public solde;

    uint public dateRetrait;


    constructor() {

        proprietaire = msg.sender;

    }


    // Déposer des fonds avec une date de retrait future

    function deposer(uint _dateRetrait) external payable {

        require(msg.sender == proprietaire, "Seul le proprietaire peut deposer");

        require(msg.value > 0, "Montant nul interdit");

        require(_dateRetrait > block.timestamp, "La date doit etre dans le futur");


        solde += msg.value;

        dateRetrait = _dateRetrait;

    }


    // Retirer les fonds si la date de retrait est passee

    function retirer() external {

        require(msg.sender == proprietaire, "Seul le proprietaire peut retirer");

        require(solde > 0, "Aucun fond a retirer");

        require(block.timestamp >= dateRetrait, "Date de retrait passee non atteinte");


        uint montant = solde;

        solde = 0;


        // Envoi sécurisé

        (bool succes, ) = proprietaire.call{value: montant}("");

        require(succes, "Echec de l'envoi");

    }


    // Consultation du solde

    function getDepot() external view returns (uint) {

        return solde;

    }


    // Consultation de la date de retrait

    function getDateRetrait() external view returns (uint) {

        return dateRetrait;

    }


    // Permet de recevoir des fonds par fallback

    receive() external payable {

        revert("Utiliser la fonction deposer");

    }

}