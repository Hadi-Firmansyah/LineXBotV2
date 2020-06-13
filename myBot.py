import telebot
import mysql.connector

import myToken

from datetime import datetime
TOKEN = myToken.TOKEN
MyBot = telebot.TeleBot(TOKEN)
myDb = mysql.connector.connect(host='localhost',user='root',database='db_belajarbot')
sql = myDb.cursor()
from telebot import apihelper
waktuSekarang=datetime.now()

class myBot:
    def __init__(self):
        self.message

    @MyBot.message_handler(commands=['start'])
    def start(message):
        photo = open('img/tb.jpg','rb')
        MyBot.send_photo(message.from_user.id,photo)
        teks = myToken.SAPA + "\nAdmin & Developer Hadi Firmansyah" + "\n"\
                              "Smk Taruna Bhakti" + "\n"\
                              "" + "\n"\
                              "/help Untuk Melihat Fitur Yang Ada" + "\n"\
                              "Tanggal/Jam Sekarang : " + str(waktuSekarang)
        MyBot.reply_to(message,teks)

    @MyBot.message_handler(commands=['help'])
    def help(message):
        teksnya = "I'm Bot T_T" + "\n" \
                  "/start Untuk Memulai Perintah" + "\n" \
                  "/help Untuk Menghubungi Bot" + "\n" \
                  "/datasiswa Untuk Melihat Data Siswa"
        MyBot.reply_to(message, teksnya)

    @MyBot.message_handler(commands=['datasiswa'])
    def menu_data_siswa(message):
        query = "select nipd,nama,kelas from tabel_siswa"
        sql.execute(query)
        data = sql.fetchall()
        jmldata = sql.rowcount
        kumpuldata = ''
        if(jmldata>0):
            no = 0
            for x in data:
                no += 1
                kumpuldata = kumpuldata + str(x)
                print(kumpuldata)
                kumpuldata = kumpuldata.replace('(','' +"\n")
                kumpuldata = kumpuldata.replace(')','' +"\n")
                kumpuldata = kumpuldata.replace("'",'')
                kumpuldata = kumpuldata.replace(',','')
        else:
            print('data kosong')
        # MyBot.send_message(message.from_user.id,str(kumpuldata))
        MyBot.reply_to(message,str(kumpuldata))

print(myDb)
print("-- Running --")
MyBot.polling(none_stop=True)