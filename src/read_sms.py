import time
from ipaddress import IPv4Address  # for your IP address
from pyairmore.request import AirmoreSession  # to create an AirmoreSession
from pyairmore.services.messaging import MessagingService  # to send messages


def get_old_otp():
    with open("otp.txt", 'r') as otpfile:
        old_otp = otpfile.read()
    return old_otp


def write_otp(otp):
    with open("otp.txt", 'w') as otpfile:
        otpfile.write(otp)


def get_otp():
    OTP = None
    session = None
    while not session:
        ip = IPv4Address("192.168.2.113")  # let's create an IP address object
        session = AirmoreSession(ip)

    session_run = False
    was_accepted = False
    print(session_run)
    print(was_accepted)
    while not session_run and not was_accepted:
        session_run = session.is_server_running
        was_accepted = session.request_authorization()
        time.sleep(5)
    print(session_run)
    print(was_accepted)
    service = MessagingService(session)
    messages = service.fetch_message_history()
    for idx, message in enumerate(messages, start=1):
        name = message.name
        if "NHPSMS" in name:
            chat = list(service.fetch_chat_history(message, limit=1))[0]
            content = chat.content
            print("OTP SMS is: {}".format(content))
            OTP = content.replace('Your OTP to register/access CoWIN is ', '')
            OTP = OTP.replace('. It will be valid for 3 minutes. - CoWIN', '')
            print("OTP: {}".format(OTP))
            if OTP:
                old_otp = get_old_otp()
                if old_otp == OTP:
                    time.sleep(10)
                else:
                    write_otp(OTP)
                break
            else:
                time.sleep(10)
    return OTP
    # except Exception as e:
    #     print(str(e))
