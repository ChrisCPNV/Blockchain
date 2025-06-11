// SPDX-License-Identifier: Unlicense

pragma solidity ^0.8.4;

import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";


contract ChrisCPNVNFT is ERC721URIStorage, Ownable {

	uint256 public mintPrice = 0.05 ether;

	uint256 public totalSupply;

	uint256 public maxSupply;

	bool public isMintEnabled = true;

	mapping(address => uint256) public mintedWallets;


	constructor(address initialOwner) ERC721('Chris CPNV NFT', 'CNFT') Ownable(initialOwner) {

		maxSupply = 5;

	}


	function toggleIsMintEnabled() external onlyOwner {

		isMintEnabled = !isMintEnabled;

	}

	function setMaxSupply(uint256 maxSupply_) external onlyOwner {

		maxSupply = maxSupply_;

	}

	function mint(string memory metadata) external payable {

		require(isMintEnabled, 'minting not enabled');

		require(mintedWallets[msg.sender] < 5, 'exceeds max per wallet');

		require(msg.value == mintPrice, 'wrong value');

		require(maxSupply > totalSupply, 'sold out');


		mintedWallets[msg.sender]++;

		totalSupply++;

		uint256 tokenId = totalSupply;

		_safeMint(msg.sender, tokenId);

		_setTokenURI(tokenId, metadata);

	}

}
