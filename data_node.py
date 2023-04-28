import pymongo

# Connect to MongoDB
client = pymongo.MongoClient('mongodb://localhost:27017/')

# Function to upload a file to MongoDB
def upload_file(filename, data):
    # Get a reference to the GridFS bucket
    bucket = client['mydb']['fs']
    # Create a new GridFS file
    with bucket.open_upload_stream(filename) as grid_in:
        # Write the data to the file
        grid_in.write(data)
    # Get the ID of the newly created file
    file_id = grid_in.document_id
    # Return the file ID
    return str(file_id)

# Function to download a file from MongoDB
def download_file(file_id):
    # Get a reference to the GridFS bucket
    bucket = client['mydb']['fs']
    # Get the file from the bucket
    file = bucket.find_one({
        '_id': pymongo.ObjectId(file_id)
    })
    # Read the data from the file
    data = file.read()
    # Return the data
    return data
