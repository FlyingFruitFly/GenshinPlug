from tools.get_attributes import get_character_attributes

character_attributes = {}


def add_attributes(paimon):
    attributes = get_character_attributes()
    character_attributes.update(attributes)
    paimon.update_attribute()


def del_attributes(paimon):
    global character_attributes
    character_attributes = {}


def get_element(paimon):
    print("学习新的工作技术，只要教过AI一次，就会了，以后的工作都可以交给他")
