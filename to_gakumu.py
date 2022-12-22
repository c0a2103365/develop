# 参考サイト:https://gakushikiweblog.com/python-email
# エラーが発生したときの参考サイト:https://www.gocca.work/python-mailerror/
# 必要なモジュール・ライブラリをインポート
import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

# SMTPサーバーに接続
smtp_server = "smtp.gmail.com" # SMTPサーバー名
port = 587 # ポート番号
server = smtplib.SMTP(smtp_server, port)

# TLS暗号化の設定
server.starttls()

# SMTPサーバーにログイン
login_address = "c0a2103365@edu.teu.ac.jp"
## 自分のメールアドレスのパスワードだとエラーが発生する。2行目のコメントを参考
login_password = "juddblthwcffjnwg"
server.login(login_address, login_password)

# メールの作成
message = MIMEMultipart()
message["Subject"] = "体温結果"
message["From"] = "c0a2103365@edu.teu.ac.jp"
message["To"] = "c0a2103365@edu.teu.ac.jp"
## 本文追加
text = MIMEText("テスト送信です。")
message.attach(text)

with open(r"student_data.csv", "rb") as f:
    attachment = MIMEApplication(f.read())
    
attachment.add_header("Content-Disposition", "attachment", filename="student_data.csv")
message.attach(attachment)

# メールの送信
server.send_message(message)

# SMTPサーバーの切断
server.quit()


