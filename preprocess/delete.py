import os
import random
from   tqdm         import tqdm


######################
#
######################
def delete_files(dir1: str, dir2: str) -> bool:
    """
    Desc: 
        This method compares two directories and deletes files if not present.
    Args:
        dir1 (str): Path to the directory 1.
        dir2 (str): Path to the directory 2.
    Returns:
        True, if the deletion was complete, otherwise False.
    """
    try:
        if not os.path.isdir(dir1) or not os.path.isdir(dir2):
            return False
        
        dir1_files = set(os.listdir(dir1))
        dir2_files = set(os.listdir(dir2))
        
        for idx, file in enumerate(dir1_files):
            print(f"Processing file {idx}...")
            
            file_path = os.path.join(dir1, file)
            if os.path.isfile(file_path):
                
                if file not in dir2_files:
                    # Delete the file is it is not present in dir2
                    os.remove(file_path)
                    print(f"Deleted file: '{file}'")
                    
        return True
        
    except Exception as delete_ex:
        print(f"Deletion error: {delete_ex}.")
        return False
    

######################
#
######################
def delete_n_random_files(dir: str, n: int) -> bool: 
    """
    Desc: 
        This method deletes 'n' random files from the provided directory.
    Args:
        dir (str): Path to the directory.
        n (int): The number of random files to be deleted.
    Returns:
        True, if the deletion was complete, otherwise False.
    """
    try:
        if not os.path.isdir(dir):
            print(f"Directory '{dir}' does not exist.")
            return False
        
        # Get all files (not directories) in the specified directory
        all_files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]
        
        if len(all_files) < n:
            print(f"Cannot delete '{n}' files, directory only contains '{len(all_files)}' files.")
            return False
        
        files_to_delete = random.sample(all_files, n)
        
        for file in tqdm(files_to_delete):
            file_path = os.path.join(dir, file)
            os.remove(file_path)
        
        return True
    
    except Exception as delete_ex:
        print(f"Error occurred while deleting: {str(delete_ex)}.")
        return False


######################
#
######################
def delete_files_name_contains(dir: str, word: str) -> bool:
    """
    Desc:
        Deletes all files in a directory whose filenames contain a specific word (case-insensitive).
    Parameters:
        dir (str): The directory to search for files.
        word (str): Substring to search for in filenames.
    Returns:
        bool: True if deletion completes (even if no files matched), False if an error occurred.
    """
    try:
        if not os.path.isdir(dir):
            print(f"Directory '{dir}' does not exist.")
            return False

        all_files = [f for f in os.listdir(dir) if os.path.isfile(os.path.join(dir, f))]

        for file in tqdm(all_files, desc="Deleting files"):
            if word.lower() in file.lower():
                file_path = os.path.join(dir, file)
                os.remove(file_path)

        return True

    except Exception as delete_ex:
        print(f"Error occurred while deleting: {str(delete_ex)}.")
        return False


######################
#
######################
if __name__ == "__main__":
    
    dir1 = "path_to_dir1"
    dir2 = "path_to_dir2"
    delete_files(dir1, dir2)