import Lab03.Stack as Stack


def list_stack(st):
    """
    Prints all of the nested elements of a list. empties st.

    :param st: Stack
    :return: None

    >>> list_stack([1,2,[4,3],5])
    5
    3
    4
    2
    1

    """
    while not st.is_empty():
        current_val = st.remove()
        if type(current_val) == type([]):
            for element in current_val:
                st.add(element)
        else:
            print(current_val)

def new_st():
    st = Stack.Stack()
    new_text = input("add something: ")
    while new_text != "end":
        st.add(new_text)
        new_text = input("add something: ")

    while not st.is_empty():
        print(st.remove())


if __name__ == "__main__":
    st = Stack.Stack()
    new_text = input("add something: ")
    while new_text != "end":
        st.add(new_text)
        new_text = input("add something: ")

    st.add([1,2,[4,3],5])

    print(st.is_empty())
    list_stack(st)

    # while not st.is_empty():
    #    print(st.remove())



class implement queue