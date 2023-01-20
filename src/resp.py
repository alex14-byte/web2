import requests


if __name__ == '__main__':
    HOST ="localhost"
    PORT = 8080
    token = open("notes/tokens.txt","r").read().split('\n')[0]

    a = int(input("1 - create_note\n2 - note_info\n3 - edit_note\n4 - delete_note\n"))
    while a > -1 | a < 5:

        if a == 1:
            id1 = int(input('id:'))
            response = requests.post(f"http://{HOST}:{PORT}/{token}/create_note", params={"id": int(id1)})
            print(f"Status : {response.status_code}")
            print(f"Response : {response.text}")
        elif a == 2:
            id1 = int(input('id:'))
            response = requests.get(f"http://{HOST}:{PORT}/{token}/note_info", params={"id": int(id1)})
            print(f"Status : {response.status_code}")
            print(f"Response : {response.text}")
        elif a == 3:
            id1 = int(input('id:\n'))
            s = str(input('text: '))
            response = requests.patch(f"http://{HOST}:{PORT}/{token}/edit_note", params={"id": int(id1), "text": s})
            print(f"Status : {response.status_code}")
            print(f"Response : {response.text}")
        elif a == 4:
            id1 = int(input('id:'))
            response = requests.delete(f"http://{HOST}:{PORT}/{token}/delete_note", params={"id": int(id1)})
            print(f"Status : {response.status_code}")
            print(f"Response : {response.text}")
        else:
            print("end")
        a = int(input("1 - create_note\n2 - note_info\n3 - edit_note\n4 - delete_note\n"))