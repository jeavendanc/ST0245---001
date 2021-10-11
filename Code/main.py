from compress import compress_csv

img = ".csv" #Image to compress

def main(file):
    compress = compress_csv()
    compress.compress_file(file)
    compress.show_img(file, compress.compressed_img)

main(img)
