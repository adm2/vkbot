import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
from config import vk_api_token
from newsapi import NewsApiClient
import json

def write_msg(user_id, message):
    vk.messages.send(user_id=user_id,
                     message=message,
                     random_id=get_random_id()
                     )

def register(user_id): #регистрация по id
    write_msg(user_id, 'Вы зарегались')

def category(user_id):
    write_msg(user_id, 'Основные новостные категории для подписки:'
                    '\n business, entertainment, general, health, science, sports, technology'
                    )

def add_cat(user_id,user_text): #Добавить категорию в подписку
    write_msg(user_id, 'Вы добавили категорию')

def view_cat(user_id): #Просмотреть подписки на категории
    write_msg(user_id, 'Список категорий')

def del_cat(user_id,user_text): #Удалить категорию из подписки
    write_msg(user_id, 'Вы удалили категорию')

def add_key(user_id,user_text): #Добавить подписку по ключевым словам
    write_msg(user_id, 'Вы что-то сделали 1')

def view_key(user_id): #Просмотреть ключеве слова для подписки
    write_msg(user_id, 'Вы что-то сделали 2')

def del_key(user_id,user_text): #Удалить ключевые слова для подписки
    write_msg(user_id, 'Вы что-то сделали 3')

def open_cat(user_id): #Получить 10 последних новостей по категориям
    write_msg(user_id, 'Вы что-то сделали 4')

def open_key(user_id): #Получить 10 последних новостей по ключевым словам
    write_msg(user_id, 'Вы что-то сделали 5')

def menu():
    for event in longpoll.listen():
        if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
            if event.text in {'help', '?', None}:
                write_msg(event.user_id, 'Список команд для новостного бота'
                            '\n \n 1 - регистрация по id'
                            '\n 2 - Доступные категории для подписки'
                            '\n 3 - Добавить категорию в подписку'
                            '\n 4 - Просмотреть подписки на категории'
                            '\n 5 - Удалить категорию из подписки'
                            '\n 6 - Добавить подписку по ключевым словам'
                            '\n 7 - Просмотреть ключеве слова для подписки'
                            '\n 8 - Удалить ключевые слова для подписки'
                            '\n 9 - Получить 10 последних новостей по категориям'
                            '\n 10 - Получить 10 последних новостей по ключевым словам'
                            )
            elif '1' in event.text:
                register(event.user_id)
            elif '2' in event.text:
                category(event.user_id)
            elif '3' in event.text:
                add_cat(event.user_id,event.text)
            elif '4' in event.text:
                del_cat(event.user_id,event.text)
            elif '5' in event.text:
                view_cat(event.user_id)
            elif '6' in event.text:
                add_key(event.user_id,event.text)
            elif '7' in event.text:
                del_key(event.user_id,event.text)
            elif '8' in event.text:
                view_key(event.user_id)
            elif '9' in event.text:
                open_cat(event.user_id)
            elif '10' in event.text:
                open_key(event.user_id)

session = vk_api.VkApi(token = vk_api_token)
longpoll = VkLongPoll(session)
vk = session.get_api()
menu()