```python
import sys
import os

def extract_submesh_data(input_filename, output_filename):
    if not os.path.exists(input_filename):
        print(f"Error: File '{input_filename}' not found.")
        sys.exit(1)

    print(f"Reading from {input_filename}...")
    
    extracting = False
    written_lines = 0

    with open(input_filename, 'r', encoding='utf-8', errors='ignore') as f_in, \
         open(output_filename, 'w', encoding='utf-8') as f_out:
        
        for line in f_in:
            if '0 SubMeshTrianglesNew data' in line or 'SubMeshTrianglesNew data' in line:
                extracting = True

            if extracting:
                f_out.write(line)
                written_lines += 1
                
                # Exit condition: End of the struct array or reaching section boundary
                # The data block for 77784 UInt8 items roughly spans ~310,000 lines
                if written_lines > 350000:
                    break

    print(f"Extraction completed successfully. Extracted {written_lines} lines to '{output_filename}'.")

if __name__ == "__main__":
    # Update input filename if your file has a different name
    input_file = "mesh_data.txt"
    output_file = "extracted_triangles.txt"
    
    extract_submesh_data(input_file, output_file)
```