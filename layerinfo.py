from csv import reader
level_1 = {
    'Main': '',
    'Enemies': '',
    'Lava': ''
}

level_2 = {
    'Main': '',
    'Enemies': '',
    'Portal': ''
}

def import_csv_layout(path):
    terr_map = []
    with open(path) as map:
        level = reader(map, delimiter = ',')
        for row in level:
            terr_map.append(list(row))
        return terr_map
