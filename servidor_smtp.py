import smtplib

servidor_email = smtplib.SMTP('smtp.gmail.com',587)
print(servidor_email.starttls())
servidor_email.login("guilhermessantosribeiro@gmail.com", ''
 )
remetente = 'guilhermessantosribeiro@gmail.com'
destinatarios = ['gleison.batista@prozeducacao.com.br','vmarques2372@gmail.com']

conteudo = 'oi! Eu sou foda pra jrai vei:) Humildade sempre rs'

servidor_email.sendmail(remetente, destinatarios,conteudo)

servidor_email.quit()