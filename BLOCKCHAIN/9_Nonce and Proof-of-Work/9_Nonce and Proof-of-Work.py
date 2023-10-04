new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# import sha256
from hashlib import sha256
# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 2
nonce = 0

# creating the proof 
proof = sha256((str(nonce)+str(new_transactions)).encode()).hexdigest()
# printing proof
print(proof)
  
# finding a proof that has 2 leading zeros
while (proof[:2] != '0' * difficulty):
  nonce += 1
  proof = sha256((str(nonce) + str(new_transactions)).encode()).hexdigest()

# printing final proof that was found
final_proof = proof
print(final_proof)

--------------------------------------------------------------------

#9_Nonce and Proof-of-Work
from hashlib import sha256

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},
               	{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# import sha256
from hashlib import sha256

# sets the amount of leading zeros that must be found in the hash produced by the nonce
difficulty = 2
nonce = 0

proof = sha256(nonce.encode() + new_transactions.encode())

difficulty.str()
nonce.str()

hash_result = sha256(text.encode())
print(hash_result.hexdigest())

# text to hash
text = "I am excited to learn about blockchain!";

# print result
hash_result = sha256(text.encode())
print(hash_result.hexdigest())