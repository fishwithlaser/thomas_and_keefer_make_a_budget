from .input_to_database import files_in_the_import_folder_to_database

if __name__ == "__main__":
    import sys
    if 'import' in sys.argv:
        files_in_the_import_folder_to_database()

    
    
