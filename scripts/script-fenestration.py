import re


def parse_fenestration_surface_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    pattern = r"FenestrationSurface:Detailed,\n\s*([\w\d]+),\s*!\- Name\n\s*([\w\d\s]+),\s*!\- Surface Type\n\s*([\w\d\s]+),\s*!\- Construction Name\n\s*([\w\d\s]+),\s*!\- Building Surface Name\n\s*(?:[^,]+)?\s*,\s*!\- Outside Boundary Condition Object\n\s*(?:[^,]+)?\s*,\s*!\- View Factor to Ground\n\s*(?:[^,]+)?\s*,\s*!\- Frame and Divider Name\n\s*(?:[^,]+)?\s*,\s*!\- Multiplier\n\s*(\d+),\s*!\- Number of Vertices\n((?:\s*-?\d+\.\d+,\s*-?\d+\.\d+,\s*-?\d+\.\d+,\s*\n)*)"

    matches = re.findall(pattern, data)

    surfaces = []
    for match in matches:
        name, surface_type, construction_name, building_surface_name, num_vertices, vertex_data = match

        vertices = []
        vertex_data = re.findall(r"-?\d+\.\d+", vertex_data)
        for i in range(0, len(vertex_data), 3):
            x, y, z = map(float, vertex_data[i:i+3])
            vertices.append((x, y, z))

        surface = {
            'Name': name,
            'Surface Type': surface_type,
            'Construction Name': construction_name,
            'Building Surface Name': building_surface_name,
            'Number of Vertices': int(num_vertices),
            'Vertices': vertices
        }

        surfaces.append(surface)

    return surfaces

# Exemplo de uso:


file_path = './audium_garcia_base v11_R00-test.txt'
fenestration_surfaces_data = parse_fenestration_surface_data(file_path)

print('Fenestration_surfaces ===', fenestration_surfaces_data)

# Visualizando os dados extraídos de FenestrationSurface:Detailed
print("Fenestration Surfaces:")
for surface in fenestration_surfaces_data:
    print(surface)
