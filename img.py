import urllib.request

def download_img(url,file_path,file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url,full_path)



url = input("Enter the img URL to download: ")
file_name = input("Enter the file name to save as: ")

download_img(url,'images/',file_name)