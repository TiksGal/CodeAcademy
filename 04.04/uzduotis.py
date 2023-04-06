import json

with open('example.json') as f:
    data = json.load(f)

result = []
for color in data['colors']:
    rgba = color['code']['rgba']
    r, g, b = rgba[0], rgba[1], rgba[2]
    hex_value = "#{:02x}{:02x}{:02x}".format(r, g, b)
    result.append({
        "color": color['color'],
        "rgb": f"{r}, {g}, {b}",
        "hex": hex_value
    })

with open('rezultatai.json', 'w') as f:
    json.dump(result, f)
