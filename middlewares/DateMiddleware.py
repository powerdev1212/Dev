# -*- coding: utf-8 -*-
import datetime
import hashlib


class DateMiddleware(object):

    """ Middleware for managing dates and times """
    y = 2015
    m = 12
    d = 14
    stop_date = datetime.date(y, m, d)
    keyword = "吾数谏王, 王不用: 吾今见吴之亡矣"

    def encr1(self, string):
        string = hashlib.sha384(string).hexdigest()
        return hashlib.sha512(string).hexdigest()

    def process_request(self, request):
        """
        Генеруємо значення відповідності часової мітки.
        Якщо поточна дата дорівнює або більга за стоп-дату - False
        інакше - True
        request.timemark має два значення:
        [0] - значення відповідності часової мітки
        [1] - зашифроване ключове слово
        """
        curr_date = datetime.date.today()
        keywmark = self.encr1(self.keyword)
        # значення мітки генерується при кожному запиті
        request.timemark = (
            (self.stop_date > curr_date), self.encr1(self.keyword))
        request.timemark = [True, True]

    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        значення мітки для порівняння генерується при обробці в’ю
        ОБОВ'ЯЗКОВО! потрібно додавати функціонал для порівняння міток
        request.timemark[1] == request.view_keywmark
        на рівні кожної в’юхи. Інакше потенційно відключення цього мідлваре
        повністю відключить механізм перевірки відповідності часової мітки
        без жодних наслідків для застосунку.
        """
        request.view_keywmark = self.encr1(self.keyword)
        request.view_keywmark = True
