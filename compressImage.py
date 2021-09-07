import os
import tinify
import sys

def compress_image(image_source, output_file_path):
    try:
        image_file_name = os.path.basename(image_source)

        if image_source.startswith('https'):
            source = tinify.from_url(image_source)
        else:
            source = tinify.from_file(image_source)
        print('{0} compressed successfully'.format(image_file_name))
    except tinify.errors.AccountError:
        print('Invalid API Key')
        return False
    except tinify.errors.ConnectionError:
        print('Please check your internet connection')
        return False
    except tinify.errors.ClientError:
        print('File tpye is not supported')
        return False
    else:
        # export compressed image file
        source.to_file(output_file_path)
        print('File exported to {0}'.format(output_file_path))
        return True

API_KEY = 'xyz'  #get api key from tiny png
tinify.key = API_KEY
FOLDER_PATH = '/Users/xyz/Work/python/ImagesToCompress/' #folder conating images to compress
for root, dirs, files in os.walk(FOLDER_PATH):
    for file in files:
        if file.endswith(".png"):
              image_folder = root
              outputPath = root.replace('ImagesToCompress', 'Outputs')
              output_folder = outputPath
              file_to_compress = os.path.join(image_folder, file)
              CHECK_FOLDER = os.path.isdir(output_folder)

              # If folder doesn't exist, then create it.
              if not CHECK_FOLDER:
                  os.makedirs(output_folder)
                  print("created folder : ", output_folder)
              else:
                  print(output_folder, "folder already exists.")
                  print(f'output folder is {output_folder}')
              compress_image(file_to_compress, os.path.join(output_folder, file))  #compress image
