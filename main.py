import hashlib

class DaveCoin:

    # Constants
    GENESIS_BLOCK_HASH = "First"

    def __init__(self, previous_block, transactions):
        self.previous_block = previous_block
        self.transactions = transactions

        # Join transactions and previous block hash to create block data
        transaction_strings = [f"{trans['sender']} sent {trans['amount']} DC to {trans['receiver']}" for trans in transactions]
        self.block_data = "-".join(transaction_strings) + "-" + previous_block

        # Calculate block hash using the block data
        self.block_hash = self.calculate_hash()

    def calculate_hash(self):
        """Calculate the hash of the block data."""
        return hashlib.sha256(self.block_data.encode()).hexdigest()

# Dummy transactions
trans_1 = {"sender": "David", "amount": 0.008, "receiver": "Tris"}
trans_2 = {"sender": "Sara", "amount": 0.56, "receiver": "David"}
trans_3 = {"sender": "Liz", "amount": 9.00, "receiver": "Joseph"}
trans_4 = {"sender": "Marla", "amount": 0.78, "receiver": "David"}
trans_5 = {"sender": "David", "amount": 1.34, "receiver": "Ashley"}
trans_6 = {"sender": "Nicole", "amount": 1.20, "receiver": "Tris"}
trans_7 = {"sender": "Ariana", "amount": 12.00, "receiver": "Doja"}
trans_8 = {"sender": "Henry", "amount": 1.00, "receiver": "Bill"}
trans_9 = {"sender": "Trippy", "amount": 4.00, "receiver": "Bill"}

# Create an instance of the DaveCoin class and pass in transactions
block_one = DaveCoin(DaveCoin.GENESIS_BLOCK_HASH, [trans_1, trans_2, trans_3])

# Output block data and hash
print(block_one.block_data)
print(block_one.block_hash)

# Create block two using the hash of the first block as the previous hash
block_two = DaveCoin(block_one.block_hash, [trans_4, trans_5, trans_6])

# Output block data and hash for the second block
print(block_two.block_data)
print(block_two.block_hash)

# Create block three using the hash of the second block as the previous hash
block_three = DaveCoin(block_two.block_hash, [trans_8, trans_9])

# Output block data and hash for the third block
print(block_three.block_data)
print(block_three.block_hash)