import re
from script_building_surface import parse_building_surface_data
from script_fenestration_surface import parse_fenestration_surface_data


def apply_rules_to_fenestration_surfaces(building_surfaces_data, fenestration_surfaces_data):
    # 1. Aplicar a primeira lógica
    for fenestration_surface in fenestration_surfaces_data:
        construction_name = fenestration_surface['Construction Name']

        if construction_name == 'Interior Door':
            building_surface_name = fenestration_surface['Building Surface Name']

            for building_surface in building_surfaces_data:
                if building_surface['Name'] == building_surface_name:
                    zone_name = building_surface['Zone Name']
                    break

            if 'quarto' in zone_name:
                fenestration_surface['Zone-name-1'] = 'quarto'
            elif 'sala' in zone_name:
                fenestration_surface['Zone-name-1'] = 'sala'
            elif 'wc' in zone_name:
                fenestration_surface['Zone-name-1'] = 'wc'
            elif 'circ' in zone_name:
                fenestration_surface['Zone-name-1'] = 'circ'

    # 2. Aplicar a segunda lógica
    for fenestration_surface in fenestration_surfaces_data:
        outside_boundary_condition_object = fenestration_surface.get('Outside Boundary Condition Object')

        for fenestration_surface_2 in fenestration_surfaces_data:
            if fenestration_surface_2['Name'] == outside_boundary_condition_object:
                fenestration_surface['Zone-name-2'] = fenestration_surface_2.get('Zone-name-1')
                break

    # 3. Aplicar a terceira lógica
    for fenestration_surface in fenestration_surfaces_data:
        zone_name_1 = fenestration_surface.get('Zone-name-1')
        zone_name_2 = fenestration_surface.get('Zone-name-2')
        name = fenestration_surface.get('Name')

        if zone_name_1 == 'sala' and zone_name_2 == 'quarto':
            fenestration_surface['Name'] = 'PQ-' + name
        elif zone_name_1 == 'quarto' and zone_name_2 == 'sala':
            fenestration_surface['Name'] = 'PQ-' + name
        elif zone_name_1 == 'sala' and zone_name_2 == 'wc':
            fenestration_surface['Name'] = 'PB-' + name
        elif zone_name_1 == 'wc' and zone_name_2 == 'sala':
            fenestration_surface['Name'] = 'PB-' + name
        elif zone_name_1 == 'wc' and zone_name_2 == 'quarto':
            fenestration_surface['Name'] = 'PB-' + name
        elif zone_name_1 == 'quarto' and zone_name_2 == 'wc':
            fenestration_surface['Name'] = 'PB-' + name
        elif zone_name_1 == 'sala' and zone_name_2 == 'circ':
            fenestration_surface['Name'] = 'PS-' + name
        elif zone_name_1 == 'circ' and zone_name_2 == 'sala':
            fenestration_surface['Name'] = 'PS-' + name


if __name__ == "__main__":
    file_path = './audium_garcia_base v11_R00-test.txt'

    with open(file_path, 'r') as file:
        content = file.read()

        building_surfaces_data = parse_building_surface_data(file_path)
        fenestration_surfaces_data = parse_fenestration_surface_data(file_path)
        fenestration_surfaces_data_after = parse_fenestration_surface_data(file_path)

        apply_rules_to_fenestration_surfaces(building_surfaces_data, fenestration_surfaces_data_after)

        for key, fenestration_surface in enumerate(fenestration_surfaces_data):
            original_name = fenestration_surface['Name']
            new_name = fenestration_surfaces_data_after[key]['Name']
            if original_name in content:
                content = content.replace(original_name, new_name)

        with open(file_path, 'w') as file:
            file.write(content)

        print('\n!!! Arquivo alterado com sucesso !!!')
