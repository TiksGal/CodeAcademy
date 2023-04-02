from dotenv import dotenv_values

config = dotenv_values(".env")
# config = {'DOMAIN': 'example.org', 'ADMIN_EMAIL': 'admin@example.org', 'ROOT_URL': 'example.org/app'}

print(config["DOMAIN"])