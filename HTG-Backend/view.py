def view(model):
    for wing, rooms in model.rooms.items():
        print(f"Wing: {wing}")
        for code, room in rooms.items():
            status = room.status.name
            print(f"Room {code}: {status}")
