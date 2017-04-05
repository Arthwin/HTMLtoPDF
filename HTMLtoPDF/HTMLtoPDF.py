import pdfkit
import os

if __name__ == "__main__":
    '''
    # Read Data
    files = os.listdir('IN/') # List all files in root directory
    truefiles = []
    databasen = ''
    for file in files:
        if '.xlsx' in file: # Find all Excel Files
            truefiles.append(file)

    '''
    pdfkit.from_file('IN/test.eml', 'out.pdf')