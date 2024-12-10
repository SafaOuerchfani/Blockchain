const bitcoin = require('bitcoinjs-lib');
const bip32 = require('bip32');
const bip39 = require('bip39');

// Générer une phrase mnémonique
const mnemonic = bip39.generateMnemonic();
console.log('Phrase mnémonique générée :', mnemonic);

// Convertir la phrase mnémonique en seed
const seed = bip39.mnemonicToSeedSync(mnemonic);

// Créer un objet BIP32 à partir du seed
const root = bip32.fromSeed(seed); // Assurez-vous que `bip32` est bien importé

// Deriver la clé à partir du chemin BIP44
const keyPair = root.derivePath("m/44'/0'/0'/0/0");

// Obtenir l'adresse et la clé publique
const { address } = bitcoin.payments.p2pkh({ pubkey: keyPair.publicKey });
const privateKeyWIF = keyPair.toWIF(); // Convertir la clé privée en format WIF

// Afficher l'adresse, la clé publique et la clé privée
console.log('Adresse Bitcoin :', address);
console.log('Clé privée (WIF) :', privateKeyWIF);
console.log('Clé publique :', keyPair.publicKey.toString('hex'));
