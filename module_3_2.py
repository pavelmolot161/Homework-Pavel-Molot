

def send_email(message, recipient, *, sender = "university.help@gmail.com"):
    blok = ["@", ".com", ".ru", ".net"]
    # for i in blok:
    if "@" in sender and "@" in recipient:
        pass
    else:
        print("Невозможно отправить письмо с адреса", (sender), "на адрес", (recipient), ".")
        # print("Нельзя отправить письмо самому себе!")
        return
    if (".com" in sender or ".ru" in sender or ".net" in sender) and (".com" in recipient or ".ru" in recipient or ".net" in recipient):
        pass
    else:
        print("Невозможно отправить письмо с адреса", (sender), "на адрес", (recipient), ".")
            # print("Нельзя отправить письмо самому себе!")
        return
        # return
    if recipient == sender:
        print("Нельзя отправить письмо самому себе!")
        return
    if sender == "university.help@gmail.com":

        print("Письмо успешно отправлено с адреса,", (sender), "на адрес,", (recipient), ".")
        return
    elif sender != "university.help@gmail.com":
        print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса", (sender), "на адрес",(recipient), ".")
    # break
send_email('Я письмо адресату', "university.help@gmail.ru", sender = "university.help@gmail.net")
















