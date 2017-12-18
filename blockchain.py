import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        # Create empty lists for our chain and our transactions.
        self.chain = []
        self.current_transactions = []

        # Create the genesis block.
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        """
        Create a new block in the chain.

        :param proof: <int> The proof given by the Proof of Work algorithm.
        :param previous_hash: (Optional) <str> Hash of the previous block.
        :return: <dict> New block.
        """

        Block = {
        
        }

    def new_transaction(self):
        """
        Create a new transaction to go into the next mined block.

        :param sender: <str> Address of the sender.
        :param recipient: <str> Address of the recipient.
        :param amount: <int> Amount.
        :return: <int> The index of the block that will hold this transaction.
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hash the passed-in block.
        pass

    @property
    def last_block(self):
        # Return the current last block of the chain.
        pass
