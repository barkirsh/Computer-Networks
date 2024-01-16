#ייבוא ספריית סוקט
import socket
# הגדרות הסוקט - כתובת בצורה IPV4 
# פרוטוקל UDP
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# עושים חיבור שמיעה לפורט 12345
s.bind(('', 12345))
# לולאה אינסופית של:
while True:
    # מקבלים כטאפל חסום בגודל של 1024 בתים דאטא וכתובת
    data, addr = s.recvfrom(1024)
    # מדפיסים מה שריבלנו
    print(str(data), addr)
    # שולחים את מה שקיבלנו באותיות גדולות חזרה לשולח
    s.sendto(data.upper(), addr)