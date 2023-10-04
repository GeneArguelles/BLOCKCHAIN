from blockchain import Blockchain

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

#instantiate new blockchain object
my_blockchain = Blockchain();

#add new transactions to newly created blockchain
my_blockchain.add_block(new_transactions);

#validate blockchain with built-in method
my_blockchain.chain[1].transactions = "fake_transactions";
print(my_blockchain.validate_chain());