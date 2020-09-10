
from bs4 import BeautifulSoup
import operator

def main():
    champ_list = []
    my_build = []
    parse(champ_list)
    #build(champ_list, my_build)
    #components(champ_list)
    #tally_1st(champ_list)
    components_1st(champ_list)


def parse(champ_list):
    with open('html.txt') as f:
        soup = BeautifulSoup(f, features='html.parser')
        champ_spans = soup.find_all(class_='champion')
        for span in champ_spans:
            name = str(span.span)
            name = name[6:-7]
            champ_list.append({'name': name, 'items': [], 'percents': [], 'components': []})
        champ_spans = soup.find_all(class_='champion')
        item_spans = soup.find_all(class_='items')
        place = 0
        for span in item_spans:
            champ_list[int(place / 5)
                       ]['items'].append(span.find(class_='name').string)
            champ_list[int(place / 5)
                       ]['percents'].append(float(span.span.string[:-1]))
            components = span.find(class_='combination').children
            for i in range(5):
                next(components)
            champ_list[int(place / 5)
                       ]['components'].append(next(components).attrs['alt'])
            for i in range(3):
                next(components)
            champ_list[int(place / 5)
                       ]['components'].append(next(components).attrs['alt'])
            place += 1
        print(champ_list)


def tally(champ_list):
    items_list={}
    for champ in champ_list:
        for item_num, item in enumerate(champ['items']):
            if item not in items_list.keys():
                items_list[item]=float(champ['percents'][item_num])
            else:
                items_list[item] = items_list[item] + \
                    float(champ['percents'][item_num])
    sorted_items = sorted(items_list.items(),
                          key=operator.itemgetter(1), reverse=True)
    for x in sorted_items:
        print(x[0],x[1])

def build(champ_list, my_build):
    previous=100
    current_percent=0
    current_champion=''
    current_item=''
    champ_list=[champ for champ in champ_list if champ['name'] in my_build]
    print(champ_list)
    for i in range(20):
        current_percent = 0
        for champ in champ_list:
            for percent_enum, percent in enumerate(champ['percents']):
                if percent > current_percent and percent < previous:
                    current_champion = champ['name']
                    current_percent = champ['percents'][percent_enum]
                    current_item = champ['items'][percent_enum]
        previous = current_percent
        print(current_champion,'|', current_item,'|', current_percent)


def components(champ_list):
    items_list = {}
    for champ in champ_list:
        for item_num, item in enumerate(champ['components']):
            if item not in items_list.keys():
                items_list[item] = float(champ['percents'][round(item_num/2)])
            else:
                items_list[item] = items_list[item] + \
                    float(champ['percents'][round(item_num/2)])
    sorted_items = sorted(items_list.items(),
                          key=operator.itemgetter(1), reverse=True)
    for x in sorted_items:
        print(x[0], x[1])


def tally_1st(champ_list):
    items_list = {}
    for champ in champ_list:
        if champ['items'][0] not in items_list.keys():
            items_list[champ['items'][0]] = float(champ['percents'][0])
        else:
            items_list[champ['items'][0]] = items_list[champ['items'][0]] + \
                float(champ['percents'][0])
    sorted_items = sorted(items_list.items(),
                          key=operator.itemgetter(1), reverse=True)
    for x in sorted_items:
        print(x[0], x[1])

def components_1st(champ_list):
    items_list = {}
    for champ in champ_list:
        if champ['components'][0] not in items_list.keys():
            items_list[champ['components'][0]] = float(champ['percents'][0])
        else:
            items_list[champ['components'][0]] = items_list[champ['components'][0]] + \
                float(champ['percents'][0])

        if champ['components'][1] not in items_list.keys():
            items_list[champ['components'][1]] = float(champ['percents'][0])
        else:
            items_list[champ['components'][1]] = items_list[champ['components'][1]] + \
                float(champ['percents'][0])
    sorted_items = sorted(items_list.items(),
                          key=operator.itemgetter(1), reverse=True)
    for x in sorted_items:
        print(x[0], x[1])

if __name__ == "__main__":
    main()
