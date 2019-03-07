#!/usr/bin/python
import shutil
import os
import logging
import getpass
import asyncio

user = getpass.getuser()
src = f'/home/{user}/Загрузки/'
telegramdir = '/home/pavel/Загрузки/Telegram Desktop/'
destination = f'/home/{user}/'
dirDict = {'images': 'Изображения/', 'docs': 'Документы/', "archive":'Archives/', 'forall': 'Общедоступные/'}


logging.basicConfig(filename='/home/pavel/todaemon/filemover.log', level=logging.INFO)


async def automated_mover():
    logging.info("auto mover started")
    files = os.listdir(src)
    try:
        if files:
            for file in files:
                if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                    shutil.move(src + file, destination + dirDict['images'])
                    logging.info(f"{file} moved from {src} to {destination + dirDict['images']}")
                elif file.endswith('.txt') or file.endswith('.pdf') or file.endswith('.djvu') or file.endswith('.docx') or file.endswith('.doc') or file.endswith('.xml'):
                    shutil.move(src + file, destination + dirDict['docs'])
                    logging.info(f"{file} moved from {src} to {destination + dirDict['docs']}")
                elif file.endswith('.tar') or file.endswith('.tar.gz') or file.endswith('.zip') or file.endswith('.tgz'):
                    shutil.move(src + file, destination + dirDict['docs'] + dirDict['archive'])
                    logging.info(f"{file} moved from {src} to {destination + dirDict['docs'] + dirDict['archive']}")
                elif file.startswith('Telegram'):
                    pass
                else:
                    shutil.move(src + file, destination + dirDict['forall'])
        else:
            logging.info('Nothing to do, empty dir')
    except Exception as e:
        logging.info(e)
    await asyncio.sleep(1800)
    await automated_mover()

mover = automated_mover()


async def telegram_files_mover():
    logging.info("Telegram mover started")
    files = os.listdir(telegramdir)
    try:
        if files:
            for file in files:
                if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                    shutil.move(telegramdir + file, destination + dirDict['images'])
                    logging.info(f"{file} moved from {telegramdir} to {destination + dirDict['images']}")
                elif file.endswith('.txt') or file.endswith('.pdf') or file.endswith('.djvu') or file.endswith('.docx') or file.endswith('.doc') or file.endswith('.xml'):
                    shutil.move(telegramdir + file, destination + dirDict['docs'])
                    logging.info(f"{file} moved from {telegramdir} to {destination + dirDict['docs']}")
                elif file.endswith('.tar') or file.endswith('.tar.gz') or file.endswith('.zip') or file.endswith('.tgz'):
                    shutil.move(telegramdir + file, destination + dirDict['docs'] + dirDict['archive'])
                    logging.info(f"{file} moved from {telegramdir} to {destination + dirDict['docs'] + dirDict['archive']}")
                elif file.startswith('Telegram'):
                    pass
                else:
                    shutil.move(telegramdir + file, destination + dirDict['forall'])
        else:
            logging.info('Nothing to do, empty dir')
    except Exception as e:
        logging.info(e)
    await asyncio.sleep(1800)
    await telegram_files_mover()


tg_mover = telegram_files_mover()


ioloop = asyncio.get_event_loop()
tasks = [ioloop.create_task(automated_mover()), ioloop.create_task(telegram_files_mover())]
wait_tasks = asyncio.wait(tasks)
ioloop.run_until_complete(wait_tasks)
ioloop.close()