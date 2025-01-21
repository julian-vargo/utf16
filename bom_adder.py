import os
import chardet  # Library for encoding detection

# Directory containing TextGrid files
input_folder = r"C:\Users\julia\Downloads\research\muhsic\mfa_english_input"
file_type = ".TextGrid"

for filename in os.listdir(input_folder):
    if filename.endswith(file_type):
        file_path = os.path.join(input_folder, filename)
        try:
            # Detect the file encoding
            with open(file_path, 'rb') as f:
                raw_data = f.read()
                result = chardet.detect(raw_data)
                detected_encoding = result['encoding']
            
            print(f"Detected encoding for {filename}: {detected_encoding}")
            with open(file_path, 'r', encoding=detected_encoding) as f:
                content = f.read()
            with open(file_path, 'w', encoding='utf-16') as f:
                f.write(content)
            
            print(f"Successfully converted {filename} to UTF-16 with BOM")
        
        except Exception as e:
            print(f"Error processing {filename}: {e}")
