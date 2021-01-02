import hashlib
import json
import os

BLOCKS_DIR = 'blocks/'
BLOCK_FILE_EXTENTION = '.json'

def get_hash(previous_block):
    # rb => read in binary
    with open(BLOCKS_DIR + previous_block, 'rb') as block_file:
        content = block_file.read()
    
    return hashlib.md5(content).hexdigest()

def check_integrity():
    """ 
        os.listdir(BLOCKS_DIR) => return a list of files 
        block_file.split('.')[0] => remove ".json" extension

        sorted(blocks_files_names, key= lambda x: int(x)) => key= lambda x: int(x) => convert every index to int for sorting in fixed order

        blocks_files_names[1:] => get all files from index 1 until the end
        
        block_data = json.load(block) => load block data from json

        previous_hash = block_data.get('previous_block').get('hash')
        previous_file_name = block_data.get('previous_block').get('file_name')
            => Get has and file name data

    """

    blocks_files = os.listdir(BLOCKS_DIR)
    blocks_files_names = []
    results = []

    for block_file in blocks_files:
        blocks_files_names.append(block_file.split('.')[0])

    blocks_files_names = sorted(blocks_files_names, key= lambda x: int(x))

    # Check Integrity
    for block_file in blocks_files_names[1:]:

        # Open Block File
        with open(BLOCKS_DIR + block_file + BLOCK_FILE_EXTENTION) as block:
            # Load Block File Data from json 
            block_data = json.load(block)

        # Get Block Previous hash and filename
        previous_hash = block_data.get('previous_block').get('hash')
        previous_file_name = block_data.get('previous_block').get('file_name')
        
        # Regenerate Previous Block Hash to check its Integrity with its stored hash
        real_hash = get_hash(previous_file_name)

        # If Previous Block Has is Equal its regenerated hash then all Ok 
        if previous_hash == real_hash:
            result = "Ok"
        else:
            result = "Was Changed"

        print(f'Block {previous_file_name}: {result}')
        
        results.append({
            'block': previous_file_name.split('.')[0],
            'result': result,
        })
    
    print(results)
    return results




def create_block(anime_name, anime_category, watched_before):
    blocks_count = len(os.listdir(BLOCKS_DIR))
    previous_block_name = str(blocks_count) + BLOCK_FILE_EXTENTION

    block = {
        "anime": anime_name,
        "category": anime_category,
        "watched_before": watched_before,
        "previous_block": {
            "hash": get_hash(previous_block_name),
            "file_name": previous_block_name
        }
    }

    # Generate Current Block File Name
    """ 
        To generate block current file name
        1. Get all "blocks files" in "blocks" directory => os.listdir(BLOCKS_DIR)
        2. Get the length of the files => len(os.listdir(BLOCKS_DIR))
        3. increment the number of files by 1 => (len(os.listdir(BLOCKS_DIR)) + 1)
        4. convert outout to string for concatenation => str(len(os.listdir(BLOCKS_DIR)) + 1)
        5. Append "blocks" directory name to the new file => BLOCKS_DIR + ...
    """

    current_block_name = BLOCKS_DIR + str(blocks_count + 1) + BLOCK_FILE_EXTENTION

    with open(current_block_name, 'w') as block_file:
        json.dump(block, block_file, indent=4, ensure_ascii=False)
        # Add New Line in the end of the file
        # All unix based systems files should end with a new line
        block_file.write('\n')

def main():
    # create_block(anime_name="Naruto Shippoden", anime_category="Ninja", watched_before="yes")
    check_integrity()




# Creating Entry Point
# Means if the file was run itself or is just imported
if __name__ == "__main__":
    main()
