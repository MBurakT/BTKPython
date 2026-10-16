def check_password(psw):
    import re

    if len(psw) < 8:
        raise Exception("Parola en az 8 karakter olmalıdır.")
    
    elif not re.search("[a-z]", psw):
        raise Exception("parola küçük harf içermelidir.")

    elif not re.search("[A-Z]", psw):
            raise Exception("parola büyük harf içermelidir.")

    elif not re.search("[A-Z]", psw):
                raise Exception("parola büyük harf içermelidir.")

    elif not re.search("[0-9]", psw):
                raise Exception("parola rakam içermelidir.")

    elif not re.search("[_@$]", psw):
                raise Exception("parola alpha numeric karakter içermelidir.")

    elif re.search("\s", psw):
                raise Exception("parola boşluk içermemelidir.")

password = "12345@aA"

try:
    check_password(password)

except Exception as ex:
        print(ex)

else:
    print("Geçerli parola girildi.")

finally:
    print("Validation tamamlandi.")
