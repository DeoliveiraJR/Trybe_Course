from script_building_surface import parse_building_surface_data
from script_fenestration_surface import parse_fenestration_surface_data


def apply_rules_to_fenestration_surfaces(building_surfaces_data, fenestration_surfaces_data):
    for fenestration_surface in fenestration_surfaces_data:
        building_surface_name = fenestration_surf   ace['Building Surface Name']
        construction_name = fenestration_surface['Construction Name']
        surface_type = fenestration_surface['Surface Type']
        zone_name = None

        if construction_name in ['Exterior Door', 'Exterior Window']:
            for building_surface in building_surfaces_data:
                if building_surface['Name'] == building_surface_name:
                    zone_name = building_surface['Zone Name']
                    break

            if zone_name is not None:
                if 'sala' in zone_name and surface_type == 'GlassDoor':
                    fenestration_surface['Name'] = 'Pvs-' + fenestration_surface['Name']
                elif 'quarto' in zone_name and surface_type == 'GlassDoor':
                    fenestration_surface['Name'] = 'Pvq-' + fenestration_surface['Name']
                elif 'sala' in zone_name and surface_type == 'Window':
                    fenestration_surface['Name'] = 'js-' + fenestration_surface['Name']
                elif 'quarto' in zone_name and surface_type == 'Window':
                    fenestration_surface['Name'] = 'jq-' + fenestration_surface['Name']
                elif 'wc' in zone_name and surface_type == 'Window':
                    fenestration_surface['Name'] = 'jb-' + fenestration_surface['Name']

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
            content = content.replace(original_name, new_name, 1)   

        with open(file_path, 'w') as file:
            file.write(content)

        print('\n!!! Arquivo alterado com sucesso !!!')
