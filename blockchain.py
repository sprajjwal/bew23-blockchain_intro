from time import time
import hashlib

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.count = 0

    def new_block(self, proof, previous_hash=None):
        """ Helper that creates a new Block """
        block = {
            'index': self.count + 1,
            'timestamp': time(),
            'proof': proof,
            'transactions': self.current_transactions,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        self.count += 1
        self.current_transactions = []
        self.chain.append(block)
        return block
    
    def new_transaction(self, sender, recipient, amount):
        """ This method creates new transactions"""
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount
        })

    @staticmethod
    def hash(block):
        """ Hashes a block and returns it """
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
    
    @property
    def last_block(self):
        """ gets the latest block and returns it """
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """ This method is where you the consensus algorithm is implemented.
            It takes two parameters including self and last_proof"""
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof +=1
        return proof

    @staticmethod

    def valid_proof(last_proof, proof):
        """This method validates proof"""
        guess = str(last_proof) + str(proof)
        guess_encoded = guess.encode()
        guess_hash = hashlib.sha256(guess_encoded).hexigest()
        return guess_hash[:4] == "0000"