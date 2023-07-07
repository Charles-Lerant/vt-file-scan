
import os
from vt import Client

# Initialize the VirusTotal client
api_key = 'xxx'  # Replace with your actual VirusTotal API key
vt_client = Client(api_key)

# Specify the directory path containing the files to scan
directory_path = 'C:\\Users\\anyuser\\Desktop\\virus_total\\'

# Iterate over files in the directory
for file_name in os.listdir(directory_path):
    file_path = os.path.join(directory_path, file_name)
    #print(file_path)
    # Check if the path is a file (not a directory)
    if os.path.isfile(file_path):
        print(f"Scanning file: {file_name}")
        with open(file_path, 'rb') as file:
            # Submit the file for scanning
            response = vt_client.scan_file(file,wait_for_completion=True)
            analysis_id = response.id

            # Retrieve the analysis report
            report = vt_client.get_object("/analyses/{}".format(analysis_id))
            
            # Print the analysis results
            print(f"Scan results for file: {file_name}")
            print(f"Scan ID: {report.id}")
            #print(f"SHA-256: {report.sha256}")
            #print(f"Positives: {report.positives}")
            print(f"Total: {report.stats}")
            print("---")

vt_client.close()          
            
