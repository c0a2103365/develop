# 参考サイト:https://gakushikiweblog.com/python-email
# エラーが発生したときの参考サイト:https://www.gocca.work/python-mailerror/
# 必要なモジュール・ライブラリをインポート
import csv # CSVモジュール
import smtplib
from email.mime.multipart import  MIMEMultipart
from email.mime.text import MIMEText

# SMTPサーバーに接続
smtp_server = "smtp.gmail.com" # SMTPサーバー名
port = 587 # ポート番号
server = smtplib.SMTP(smtp_server, port)

# TLS暗号化の設定
server.starttls()

# SMTPサーバーにログイン
login_address = "自分のメアド"
## 自分のメールアドレスのパスワードだとエラーが発生する。2行目のコメントを参考
login_password = "XXXXXX"
server.login(login_address, login_password)

# メールの作成
message = MIMEMultipart()
message["Subject"] = "先進情報専門演習テーマIT2のテストです"
message["From"] = "自分のメアド"
message["To"] = "送信先"
## 本文追加
text = MIMEText("テスト送信です。")
message.attach(text)

# メールの送信
server.send_message(message)

# SMTPサーバーの切断
server.quit()
