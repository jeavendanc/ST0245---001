from compress import compress_csv

img = "./csv/enfermo_csv/jesus.csv"

def main(file):
    compress = compress_csv()
    compress.compress_file(file)
    compress.show_img(file, compress.compressed_img)

main(img)
