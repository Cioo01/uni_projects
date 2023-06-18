import random
import time
import sys
from xml.etree import ElementTree as ET


sys.setrecursionlimit(20000)
final_result = ""

class OligoNode:
    def __init__(self):
        self.olig = ""
        self.next_to_visit_list = []
        self.index = 0
        self.visited = 0
        self.matches = 0

def Hamilton(list, list_of_visited, probe, length, current, result):
    list_of_visited.append(current.index)
    current.visited += 1
    for i in range(len(current.next_to_visit_list)):
        if list[current.next_to_visit_list[i]].visited < list[current.next_to_visit_list[i]].matches:
            Hamilton(list, list_of_visited, probe, length, list[current.next_to_visit_list[i]], result)
    if list_of_visited[0] == current.index:
        for j in range(probe-1, -1, -1):
            result.insert(0, list[current.index].olig[j])
    else:
        result.insert(0, list[current.index].olig[probe - 1])

def next_to_visit(list, parent, probe):
    for i in range(len(list)):
        if (i != parent.index) and (list[i].olig[:probe-1] == parent.olig[1:probe]):
            parent.next_to_visit_list.append(i)

def convert_intensity(intensity):
    if intensity == 0:
        return 0
    elif intensity in (1, 2):
        return 1
    elif intensity == 3:
        return random.randint(1,2)
    elif intensity == 4:
        return 2
    elif intensity == 5:
        return random.randint(2,3)
    elif intensity in (8, 9):
        return random.randint(7, 8)
    elif intensity in (6, 7, 8):
        return random.randint(4, 6)  
    elif intensity >= 9:
        return 9 

def main():
    global final_result
    random.seed(time.time())
    if len(sys.argv) < 2:
        print("Podaj nazwe programu, a potem nazwe pliku testowego")
        return False
    tree = ET.parse(sys.argv[1])
    root = tree.getroot()

    length = int(root.attrib["length"])
    start = root.attrib["start"]

    probe = len(start)
    begin_index = 0

    nodes = []
    list_of_visited = []

    probe_element = root.find("probe")
    cells = probe_element.findall("cell")

    tracker = 0
    intensity = 0
    oligonucleotide = ""
    number_of_oligs = 0

    for cell in cells:
        intensity = int(cell.get("intensity"))
        oligonucleotide = cell.text

        oligo = OligoNode()
        oligo.index = tracker
        oligo.olig = oligonucleotide
        oligo.matches = convert_intensity(intensity)
        number_of_oligs += convert_intensity(intensity)
        nodes.append(oligo)

        if start == oligonucleotide:
            begin_index = tracker
        tracker += 1

    for i in range(len(nodes)):
        next_to_visit(nodes, nodes[i], probe)

    partial_result = []
    Hamilton(nodes, list_of_visited, probe, length, nodes[begin_index], partial_result)
    final_result += "".join(partial_result)
    partial_result.clear()

    found = False
    while len(list_of_visited) < number_of_oligs and len(final_result) < length:
        found = False
        index = 0
        for j in range(probe - 2, -1, -1):
            for i in range(len(nodes)):
                if nodes[i].visited < nodes[i].matches:
                    if j == 0:
                        index = i
                        found = True
                        final_result += nodes[i].olig[j:probe - 1 - j]
                    else:
                        if final_result[-j:] == nodes[i].olig[:j]:
                            index = i
                            found = True
                            final_result += nodes[i].olig[j:probe - 1 - j]
                if found:
                    break
            if found:
                break

        if found:
            Hamilton(nodes, list_of_visited, probe, length, nodes[index], partial_result)
            final_result += "".join(partial_result)
            partial_result.clear()
        else:
            break
    print(final_result)


if __name__ == "__main__":
    main()

