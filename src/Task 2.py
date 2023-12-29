# v26


class LinkedList_element:
    prev_el_id = None
    next_el_id = None
    value = None

    def __init__(self, value):
        self.value = value

    def add_prev(self, prev_id):
        self.prev_el_id = prev_id

    def add_next(self, next_id):
        self.next_el_id = next_id


class LinkedList:
    first = None
    elements = {}
    prev = None
    last = None

    def add_next_el(self, el: LinkedList_element):
        el.add_prev(self.prev)
        curr_id = id(el)
        if self.first == None and self.prev == None:
            self.first = curr_id
        if self.prev:
            self.elements[self.prev].add_next(curr_id)
        self.elements[curr_id] = el
        self.prev = curr_id
        self.last = curr_id

    def insert_el(self, el: LinkedList_element, insertion_value):
        curr_id = id(el)
        for key, list_el in self.elements.items():
            if list_el.value == insertion_value:
                old_next = self.elements[key].next_el_id
                if old_next == None:
                    self.last = curr_id
                else:
                    self.elements[old_next].add_prev(curr_id)
                self.elements[key].add_next(curr_id)
                el.add_prev(key)
                el.add_next(old_next)
                self.elements[curr_id] = el
                return
        print("Insertion value not found.")

    def toPrint(self):
        for key, el in self.elements.items():
            print(
                f"el_id: {key}; el_value: {el.value}; prev_el_id: {el.prev_el_id}; next_el_id: {el.next_el_id};")

    def stringInOrder(self, next_id="first"):
        if next_id == "first":
            curr_el = self.elements[self.first]
        elif next_id == None:
            return ""
        else:
            curr_el = self.elements[next_id]
        return curr_el.value + " " + self.stringInOrder(curr_el.next_el_id)


if __name__ == "__main__":
    string = "Lorem ipsum dolor sit amet cadet org prot let srut nex wreght lokd prold."
    arr = string.split()
    linkList = LinkedList()
    for el in arr:
        el = LinkedList_element(el)
        linkList.add_next_el(el)

    linkList.toPrint()
    print(linkList.stringInOrder())

    add_str = "HAPPY NEW YEAR!"
    add_arr = add_str.split()
    insert = "snowman"
    for add_el in add_arr:
        add_el = LinkedList_element(add_el)
        linkList.insert_el(add_el, insert)
        insert = add_el.value

    print(linkList.stringInOrder())
