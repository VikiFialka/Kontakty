contacts = [
    {
        "name": "Anička",
        "email": "anicka@email.com",
        "phone": "777 777 777"
    },
    {
        "name": "Nikol",
        "email": "nikol@email.com",
        "phone": "777 777 777"
    }
]
#Vypsat cely kontakt
print (contacts[0])
print (contacts[1])

#vypsat hodnotu klíče "name"
print(contacts[0]["name"])

# přidáme kontakt
name = "Anička"
email = "anicka_2@mail.com"
phone = ""

contact = {
    "name": name,
    "email": email,
    "phone": phone
}

# přidat contact do contacts
contacts.append(contact)

print(contacts)