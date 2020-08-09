import random
import uuid

tasks = []

user = {
    "email": "test@test.com",
    "password": "qwer1234",
    "firstname": "foo",
    "lastname": "bar",
    "accessToken": str(uuid.uuid4())
}


def check_user(user_data):
    if user_data.email == user["email"] and user_data.password == user["password"]:
        return user
    return None


def create_mock_data():
    status = ["in-backlog", "in-progress", "ready-to-test", "done"]
    assignee = ["Aaran", "Aaren", "Aarez", "Aarman", "Aaron", "Aaron-James", "Aarron", "Aaryan", "Aaryn", "Aayan",
                "Aazaan", "Abaan", "Abbas", "Abdallah", "Abdalroof", "Abdihakim", "Abdirahman", "Abdisalam", "Abdul",
                "Abdul-Aziz", "Abdulbasir", "Abdulkadir", "Abdulkarem", "Abdulkhader", "Abdullah", "Abdul-Majeed",
                "Abdulmalik", "Abdul-Rehman", "Abdur", "Abdurraheem", "Abdur-Rahman", "Abdur-Rehmaan", "Abel",
                "Abhinav",
                "Abhisumant", "Abid", "Abir", "Abraham", "Abu", "Abubakar", "Ace", "Adain", "Adam", "Adam-James",
                "Addison", "Addisson", "Adegbola", "Adegbolahan", "Aden", "Adenn", "Adie", "Adil", "Aditya", "Adnan",
                "Adrian", "Adrien", "Aedan", "Aedin", "Aedyn", "Aeron", "Afonso", "Ahmad", "Ahmed", "Ahmed-Aziz",
                "Ahoua",
                "Ahtasham", "Aiadan", "Aidan", "Aiden", "Aiden-Jack", "Aiden-Vee", "Aidian", "Aidy", "Ailin", "Aiman",
                "Ainsley", "Ainslie", "Airen", "Airidas", "Airlie", "AJ", "Ajay", "A-Jay", "Ajayraj", "Akan", "Akram",
                "Al", "Ala", "Alan", "Alanas", "Alasdair", "Alastair", "Alber", "Albert", "Albie", "Aldred", "Alec",
                "Aled", "Aleem", "Aleksandar", "Aleksander", "Aleksandr", "Aleksandrs", "Alekzander", "Alessandro",
                "Alessio", "Alex", "Alexander", "Alexei", "Alexx", "Alexzander", "Alf", "Alfee", "Alfie", "Alfred",
                "Alfy",
                "Alhaji", "Al-Hassan", "Ali", "Aliekber", "Alieu", "Alihaider", "Alisdair", "Alishan", "Alistair",
                "Alistar", "Alister", "Aliyaan", "Allan", "Allan-Laiton", "Allen", "Allesandro", "Allister", "Ally",
                "Alphonse", "Altyiab", "Alum", "Alvern", "Alvin", "Alyas", "Amaan", "Aman", "Amani", "Ambanimoh",
                "Ameer",
                "Amgad", "Ami", "Amin", "Amir", "Ammaar", "Ammar", "Ammer", "Amolpreet", "Amos", "Amrinder", "Amrit",
                "Amro", "Anay", "Andrea", "Andreas", "Andrei", "Andrejs", "Andrew", "Andy", "Anees", "Anesu", "Angel",
                "Angelo", "Angus", "Anir", "Anis", "Anish", "Anmolpreet", "Annan", "Anndra", "Anselm", "Anthony",
                "Anthony-John", "Antoine", "Anton", "Antoni", "Antonio", "Antony", "Antonyo", "Anubhav", "Aodhan",
                "Aon",
                "Aonghus", "Apisai", "Arafat", "Aran", "Arandeep", "Arann", "Aray", "Arayan", "Archibald", "Archie",
                "Arda", "Ardal", "Ardeshir", "Areeb", "Areez", "Aref", "Arfin", "Argyle", "Argyll", "Ari", "Aria",
                "Arian",
                "Arihant", "Aristomenis", "Aristotelis", "Arjuna", "Arlo", "Armaan", "Arman", "Armen", "Arnab", "Arnav",
                "Arnold", "Aron", "Aronas", "Arran", "Arrham", "Arron", "Arryn", "Arsalan", "Artem", "Arthur", "Artur"]

    titles = [
        "Nulla Corporation", "Vitae Corp", "Varius Et Corp", "Odio Sagittis Semper Limited",
        "Mollis Nec Cursus Limited", "Ante Corporation", "Integer Eu Corporation", "Cursus Nunc Foundation",
        "Ac Incorporated", "Accumsan Neque Foundation", "Purus Ltd", "Amet Company", "Morbi Neque Company",
        "Quis Turpis Vitae Limited", "In Sodales Elit PC", "Bibendum Donec Felis Corp", "Sit Amet Institute",
        "Mi Pede Nonummy LLP", "Consequat Institute", "Mi Fringilla Institute", "At Associates",
        "Placerat Orci Company", "Lectus Ltd", "Ornare Elit Limited", "Penatibus Et Magnis Ltd", "Cursus Luctus Ltd",
        "Justo Eu Arcu Institute", "Eu Sem Pellentesque Limited", "Adipiscing Non LLC", "Ac Corp", "Euismod Corp",
        "Ac Risus Morbi Limited", "Enim Mauris Quis Institute", "Pharetra Nibh Aliquam Institute", "Facilisis Eget Ltd",
        "Netus Company", "Erat Incorporated", "Nullam Lobortis Ltd", "Semper Institute", "Elit Corp",
        "Dolor Corporation", "Laoreet Posuere Incorporated", "Aliquam Nec Enim Corp", "A Tortor Nunc Associates",
        "Non Quam Consulting", "Ipsum Nunc Id Associates", "Justo Praesent Luctus LLC", "Morbi Tristique Institute",
        "Dolor Corp", "Nonummy Fusce Industries", "In Limited", "Eget Foundation", "Sit Foundation", "Sem Foundation",
        "Sit Ltd", "Ut Erat Sed Corporation", "Nam Ligula Elit LLC", "Eu Company", "Primis Industries",
        "Accumsan Convallis Ante Corp", "Ante Blandit Viverra Incorporated", "Congue Turpis Associates",
        "Enim Diam Vel Corp", "Egestas Nunc Sed Institute", "Elit Pretium Institute", "Velit Inc", "Aliquet Consulting",
        "Et Industries", "Mauris Blandit Company", "Nullam Scelerisque Corporation", "Gravida Sagittis Limited",
        "Aliquam Eu Accumsan PC", "Parturient Foundation", "Molestie Sodales Mauris Inc", "Ut Odio Vel Foundation",
        "Ac Facilisis Facilisis Incorporated", "Metus Aenean Sed Ltd", "Eget Institute", "Tincidunt Nunc Industries",
        "Cursus Integer Mollis PC", "Nulla Incorporated", "Eu LLP", "Semper Cursus LLC", "Ut Dolor Ltd",
        "Placerat Incorporated", "Dis Parturient PC", "Cursus Industries", "At Industries",
        "Malesuada Fringilla Est Associates", "Bibendum Inc", "Consequat Lectus Sit Consulting",
        "Tristique Pharetra Quisque Corporation", "Pellentesque Inc", "Vulputate Corp", "Quis Tristique Institute",
        "Phasellus Nulla Integer Ltd", "Magna Ltd", "Ipsum Nunc Id Foundation", "Nam Corp", "At Auctor Company"
    ]

    for i in range(55):
        tasks.append({
            "id": str(uuid.uuid4()),
            "title": random.choice(titles),
            "sprint": "spring-" + str(random.randint(1, 3)),
            "estimate": str(random.randint(1, 10)),
            "status": random.choice(status),
            "assignee": random.choice(assignee),
        })


def get_task(task_uuid):
    for task in tasks:
        if task["id"] == task_uuid:
            return task
    return None


def add_task(task_data):
    new_task = {
        "id": str(uuid.uuid4()),
        "title": task_data.title,
        "sprint": task_data.sprint,
        "estimate": task_data.estimate,
        "status": task_data.status,
        "assignee": task_data.assignee,
    }
    tasks.append(new_task)
    return new_task


def remove_task(task_uuid):
    tasks.remove(get_task(task_uuid))
    return {"message": "task removed"}


def update_task(task_uuid, task_data):

    task = get_task(task_uuid)
    tasks.remove(task)
    new_task = {
        "id": task_uuid,
        "title": task_data.title,
        "sprint": task_data.sprint,
        "estimate": task_data.estimate,
        "status": task_data.status,
        "assignee": task_data.assignee,
    }
    tasks.append(new_task)
    return new_task
