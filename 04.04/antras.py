import requests

def save_cat_images(number: int):
    for i in range(number):
        r = requests.get('https://cataas.com/cat')
        with open(f'cat{i}.jpg', 'wb') as f:
            f.write(r.content)
            print(f'Cat image {i} saved to file.')
            
print(save_cat_images(5))