from script_building_surface import parse_building_surface_data
from script_fenestration_surface import parse_fenestration_surface_data


def apply_rules_to_fenestration_surfaces(building_surfaces_data, fenestration_surfaces_data):
    for fenestration_surface in fenestration_surfaces_data:
        building_surface_name = fenestration_surface['Building Surface Name']
        construction_name = fenestration_surface['Construction Name']
        surface_type = fenestration_surface['Surface Type']
        zone_name = None

        if construction_name in ['Exterior Door', 'Exterior Window']:
            for building_surface in building_surfaces_data:
                if building_surface['Name'] == building_surface_name:
                    zone_name = building_surface['Zone Name']
                    break

            if zone_name is not None:
                if 'sala' in zone_name and surface_type == 'Door':
                    fenestration_surface['Name'] = 'Pvs-' + fenestration_surface['Name']
                elif 'quarto' in zone_name and surface_type == 'Door':
                    fenestration_surface['Name'] = 'Pvq-' + fenestration_surface['Name']
                elif 'sala' in zone_name and surface_type == 'Window':
                    fenestration_surface['Name'] = 'js-' + fenestration_surface['Name']
                elif 'quarto' in zone_name and surface_type == 'Window':
                    fenestration_surface['Name'] = 'jq-' + fenestration_surface['Name']
                elif 'banheiro' in zone_name and surface_type == 'Window':
                    fenestration_surface['Name'] = 'jb-' + fenestration_surface['Name']

        elif construction_name == 'Interior Door':
            linked_building_surface_name = None
            linked_zone_name = None

            for building_surface in building_surfaces_data:
                if building_surface['Name'] == building_surface_name:
                    linked_fenestration_name = building_surface['Outside Boundary Condition Object']
                    break

            for fenestration_surface in fenestration_surfaces_data:
                if fenestration_surface['Name'] == linked_fenestration_name:
                    linked_building_surface_name = fenestration_surface['Building Surface Name']
                    break

            for building_surface in building_surfaces_data:
                if building_surface['Name'] == linked_building_surface_name:
                    linked_zone_name = building_surface['Zone Name']
                    break

            if linked_zone_name is not None and zone_name is not None:
                if 'sala' in linked_zone_name and 'quarto' in zone_name:
                    fenestration_surface['Name'] = 'PQ-' + fenestration_surface['Name']
                elif 'sala' in linked_zone_name and 'banheiro' in zone_name:
                    fenestration_surface['Name'] = 'PB-' + fenestration_surface['Name']
                elif 'banheiro' in linked_zone_name and 'quarto' in zone_name:
                    fenestration_surface['Name'] = 'PB-' + fenestration_surface['Name']
                elif 'sala' in linked_zone_name and 'circ' in zone_name:
                    fenestration_surface['Name'] = 'PS-' + fenestration_surface['Name']


if __name__ == "__main__":
    file_path = './audium_garcia_base v11_R00-test.txt'

    with open(file_path, 'r') as file:
        content = file.read()

        building_surfaces_data = parse_building_surface_data(file_path)
        fenestration_surfaces_data = parse_fenestration_surface_data(file_path)
        fenestration_surfaces_data_after = parse_fenestration_surface_data(file_path)

        # Visualizando os dados extraídos
        # print("Building Surfaces:")
        # for surface in building_surfaces_data:
        #     print(surface)

        # print("\nFenestration Surfaces (Antes das Regras):")
        # for surface in fenestration_surfaces_data:
        #     print(surface)

        apply_rules_to_fenestration_surfaces(building_surfaces_data, fenestration_surfaces_data_after)

        # print("\nFenestration Surfaces (Depois das Regras):")
        # for surface in fenestration_surfaces_data_after:
        #     print(surface)

        for key, fenestration_surface in enumerate(fenestration_surfaces_data):
            original_name = fenestration_surface['Name']
            new_name = fenestration_surfaces_data_after[key]['Name']
            content = content.replace(original_name, new_name, 1)

        with open(file_path, 'w') as file:
            file.write(content)

        print('\n!!! Arquivo alterado com sucesso !!!')
