import re


def parse_building_surface_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    # Ajustando a expressão regular para tornar o campo "View Factor to Ground" opcional
    pattern = r"BuildingSurface:Detailed,\n\s*([\w\d]+),\s*!\- Name\n\s*([\w\d\s]+),\s*!\- Surface Type\n\s*([\w\d\s]+),\s*!\- Construction Name\n\s*([\w\d\s]+),\s*!\- Zone Name\n\s*([\w\d\s]+),\s*!\- Outside Boundary Condition\n\s*([\w\d\s]+),\s*!\- Outside Boundary Condition Object\n\s*([\w\d\s]+),\s*!\- Sun Exposure\n\s*([\w\d\s]+),\s*!\- Wind Exposure\n\s*(?:[^,]+)?\s*,\s*!\- View Factor to Ground\n\s*(\d+),\s*!\- Number of Vertices\n((?:\s*-?\d+\.\d+,\s*-?\d+\.\d+,\s*-?\d+\.\d+,\s*\n)*)"

    matches = re.findall(pattern, data)

    surfaces = []   
    for match in matches:
        # name, surface_type, construction_name, zone_name, outside_boundary, boundary_object, vertex_data = match
        name, surface_type, construction_name, zone_name, outside_boundary, boundary_object, sun_exposure, wind_exposure, num_vertices, vertex_data = match

        vertices = []
        vertex_data = re.findall(r"-?\d+\.\d+", vertex_data)
        for i in range(0, len(vertex_data), 3):
            x, y, z = map(float, vertex_data[i:i+3])
            vertices.append((x, y, z))

        surface = {
            'Name': name,
            'Surface Type': surface_type,
            'Construction Name': construction_name,
            'Zone Name': zone_name,
            'Outside Boundary Condition': outside_boundary,
            'Outside Boundary Condition Object': boundary_object,
            'Sun Exposure': sun_exposure,
            'Wind Exposure': wind_exposure,
            'Number of Vertices': int(num_vertices),
            'Vertices': vertices
        }

        surfaces.append(surface)

    return surfaces

# Exemplo de uso:


file_path = './audium_garcia_base v11_R00-test.txt'
surfaces_data = parse_building_surface_data(file_path)


print('Building_surfaces ===', surfaces_data)

# Visualizando os dados extraídos
# for surface in surfaces_data:
#     print(surface)
