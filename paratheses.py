import stackClass


def balanced_delimiter(string):
    st = stackClass.Stack()

    opener_dict = {")": "(", "]": "[", "}": "{"}

    for char in string:
        if char in "([{":
            st.put(char)
        elif char in ")]}" and st.isEmpty() == False:
            opener = st.remove()
            if opener != opener_dict[char]:
                return False

    return st.isEmpty()

print("this should be True", balanced_delimiter("hell(o)"))
print("this should be True", balanced_delimiter("he[l]l{(o)}"))
print("this should be False", balanced_delimiter("hell(o}"))
print("this should be False", balanced_delimiter("hell(o})"))
print("this should be False", balanced_delimiter("hell(o})("))
print("this should be False", balanced_delimiter("hell{(o})"))
print("this should be False", balanced_delimiter("{}(hello!"))