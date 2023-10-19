

rooms = [[1, 3], [3, 0, 1], [], [2]]


def roomvisit(rooms):
    vist = set()
    st = [0]
    while st:
        room = st.pop()
        vist.add(room)
        for key in rooms[room]:
            if key in vist:
                st.append(key)
    return len(vist) == len(rooms)


print(roomvisit(rooms))
