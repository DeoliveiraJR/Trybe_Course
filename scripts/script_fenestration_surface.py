import re


def parse_fenestration_surface_data(file_path):
    with open(file_path, 'r') as file:
        data = file.read()

    pattern = r"FenestrationSurface:Detailed,\s*([\w\d]+),\s*!- Name\s*([\w\d\s]+),\s*!- Surface Type\s*([\w\d\s]+),\s*!- Construction Name\s*([\w\d\s]+),\s*!- Building Surface Name\s*([\w\d\s]+),\s*!- Outside Boundary Condition Object\s*([^,\n]+)?\s*,\s*!- View Factor to Ground\s*([^,\n]+)?\s*,\s*!- Frame and Divider Name\s*([^,\n]+)?\s*,\s*!- Multiplier\s*(\d*)\s*,\s*!- Number of Vertices\n((?:\s*-?\d+\.\d+,\s*-?\d+\.\d+,\s*-?\d+\.\d+,\s*\n)*)"

    matches = re.findall(pattern, data)

    surfaces = []
    for match in matches:
        name, surface_type, construction_name, building_surface_name, boundary_condition_object, view_factor, frame_divider, multiplier, num_vertices, vertex_data = match

        vertices = []
        vertex_data = re.findall(r"-?\d+\.\d+", vertex_data)
        for i in range(0, len(vertex_data), 3):
            x, y, z = map(float, vertex_data[i:i + 3])
            vertices.append((x, y, z))

        multiplier_value = int(multiplier) if multiplier else None

        surface = {
            'Name': name,
            'Surface Type': surface_type,
            'Construction Name': construction_name,
            'Building Surface Name': building_surface_name,
            'Outside Boundary Condition Object': boundary_condition_object,
            'View Factor to Ground': view_factor,
            'Frame and Divider Name': frame_divider,
            'Multiplier': multiplier_value,
            'Number of Vertices': int(num_vertices),
            'Vertices': vertices
        }

        surfaces.append(surface)

    return surfaces

file_path = './audium_garcia_base v11_R00-test.txt'
fenestration_surfaces_data = parse_fenestration_surface_data(file_path)

print('Fenestration Surfaces ===', fenestration_surfaces_data)
