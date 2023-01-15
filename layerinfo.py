from csv import reader

level_1 = {
    'Main': 'map1/map1_Main .csv',
    'Enemies': 'map1/map1_Enemies.csv',
    'Lava': 'map1/map1_Lava.csv'}

level_2 = {'Main': 'map2/map2_Main.csv',
           'Enemies': 'map2/map2_Enemies.csv',
           'Portal': 'map2/map2_Portals'}

def import_csv_layout(path):
    terr_map = []
    with open(path) as map:
        level = reader(map, delimiter = ',')
        for row in level:
            terr_map.append(list(row))
        return terr_map
