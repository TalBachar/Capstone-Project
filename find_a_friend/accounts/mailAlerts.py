from django.core.mail import send_mail


class sendMail:
    def sendMail(first_name, email):
        email_message = (" Hello " + first_name + "! Thank you for using our alert service! \n\n"
                         "We at Find-a-Friend NYC are dedicated to helping pets in NYC find their forever home "
                         "And we promise to do whatever we can to help you find a friend - for life!\n\n"
                         "\n\nBe sure to check out site regularly, as our database of pets updates daily!"
                         "\n\nKind Regards,\n Find-a-Friend ")

        send_mail('Alerts from Find-a-Friend NYC Activated!',
                  email_message,
                  'findafriendnyc@gmail.com',
                  [email],
                  fail_silently=False,
                  )
