import pymongo

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Get a reference to the files collection
files = client['mydb']['files']

# Function to create a new file
def create_file(filename, size):
    # Create a new document in the files collection
    files.insert_one({
        'filename': filename,
        'size': size,
        'nodes': []
    })

# Function to add a node to a file
def add_node(filename, node):
    # Update the nodes field in the document for the specified file
    files.update_one({
        'filename': filename
    }, {
        '$push': {
            'nodes': node
        }
    })

# Function to get the nodes for a file
def get_nodes(filename):
    # Get the document for the specified file
    file_doc = files.find_one({
        'filename': filename
    })
    # Return the nodes field from the document
    return file_doc['nodes']

# Function to delete a file
def delete_file(filename):
    # Delete the document for the specified file
    files.delete_one({
        'filename': filename
    })
