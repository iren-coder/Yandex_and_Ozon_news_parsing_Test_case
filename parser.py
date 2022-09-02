import time
import datetime
import requests
from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium_stealth import stealth

# Вывод логов в консоль
def log_msg(msg=""):
    print(datetime.datetime.now().strftime("[INFO][%H:%M:%S]"), msg)

# Парсер новостей для озона
def ozon_parser():
    try:
        url = "https://seller.ozon.ru"  # Ссылка на основной сайт


        # Подключение опций для обхода анти-бота Озона
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--disable-blink-features")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_experimental_option("excludeSwitches", ["enable-automation"])
        options.add_experimental_option('useAutomationExtension', False)
        options.add_argument("start-maximized")

        # Драйвер для работы с браузером
        driver = webdriver.Chrome(options=options)

        driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

        stealth(driver,
                languages=["en-US", "en"],
                vendor="Google Inc.",
                platform="Win32",
                webgl_vendor="Intel Inc.",
                renderer="Intel Iris OpenGL Engine",
                fix_hairline=True,
        )

        driver.get(url+"/news/")  # Переход на новостной блок
        time.sleep(3)
        driver.implicitly_wait(10)  # Ожидание загрузки страница
        time.sleep(2)
        # Поиск элемента кнопки "Ещё новости" и нажатие на неё
        driver.find_element(By.XPATH, "//*[@id='__layout']/div/div[1]/div/div[2]/div/button/span").click()
        time.sleep(2)
        # Предоставление страница для парсинга
        soup = bs(driver.page_source, "html.parser")
        log_msg("Successful connection to \"ozon.ru\"!")

        # Берём десять блоков с новостями
        news_card = soup.find_all("div", class_="news-card")[:10]
        links = []  # Будем хранить ссылки новостных блоков
        dates = []  # Будем хранить даты публикаций новостных блоков
        titles = []  # Будем хранить заголовки новостных блоков
        contents = []  # Будем хранить содержимое новостных блоков
        tags = []  # Будем хранить теги новостных блоков

        # Работаем с каждым новостным блоком, перебирая его в цикле
        for new in news_card:
            links.append(url+new.find("a", class_="news-card__link")["href"])
            dates.append(new.find("span", class_="news-card__date").text)
            titles.append(new.find("h3", class_="news-card__title").text[9:-7])
            # Контейнер с тегами
            mark_container = new.find("div", class_="news-card__mark-container")

            # Проверка на существование контейнера с тегами
            if mark_container:
                tags_in_container = []  # Собранные теги в новостном блоке
                for tag in mark_container.find_all("div", class_="news-card__mark"):
                    tags_in_container.append(tag.text)
                tags.append(tags_in_container)
            else:
                tags.append(None)

        # Переходим в каждый новостной блок для извлечения содержимого
        for link in links:
            driver.get(link)
            time.sleep(2)
            soup = bs(driver.page_source, "html.parser")
            content = ""
            # Перебираем все элементы в секции содержимого и соединяем их в единое
            for element in soup.find("section", class_="new-section"):
                content += element.text
            contents.append(content)
        log_msg("Parser \"ozon.ru\" was finished!")
        return {"titles": titles, "contents": contents, "dates": dates, "tags": tags}
    except:
        log_msg("Failed connection to \"ozon.ru\"!")


def yandex_parser():
    url = "https://market.yandex.ru"  # Ссылка на основной сайт

    # Отправляем запрос на новостной блок
    r = requests.get(url+"/partners/news")

    if r.status_code == 200:
        soup = bs(r.text, "html.parser")
        log_msg("Successful connection to \"yandex.ru\"!")
        # Берём десять блоков с новостями
        news_card = soup.find_all("div", class_="news-list__item")[:10]
        links = []  # Будем хранить ссылки новостных блоков
        dates = []  # Будем хранить даты публикаций новостных блоков
        titles = []  # Будем хранить заголовки новостных блоков
        contents = []  # Будем хранить содержимое новостных блоков
        tags = []  # Будем хранить теги новостных блоков

        # Работаем с каждым новостным блоком, перебирая его в цикле
        for new in news_card:
            links.append(url + new.find("a")["href"])
            dates.append(new.find("time", class_="news-list__item-date").text)
            titles.append(new.find("div", class_="news-list__item-header").text.replace("\xa0", " "))

        # Переходим в каждый новостной блок для извлечения содержимого
        for link in links:
            r = requests.get(link)
            soup = bs(r.text, "html.parser")
            content = ""
            # Перебираем все элементы в секции содержимого и соединяем их в единое
            for element in soup.find("div", class_="news-info__post-body html-content page-content"):
                content += element.text.replace("\xa0", " ") + "\n"
            contents.append(content)

            # Контейнер с тегами
            mark_container = soup.find("div", class_="news-info__tags")
            # Проверка на существование контейнера с тегами
            if mark_container:
                tags_in_container = []  # Собранные теги в новостном блоке
                for tag in mark_container.find_all("a"):
                    tags_in_container.append(tag.text[1:])
                tags.append(tags_in_container)
            else:
                tags.append(None)
        log_msg("Parser \"yandex.ru\" was finished!")
        return {"titles": titles, "contents": contents, "dates": dates, "tags": tags}

    else:
        log_msg("Failed to connect to \"yandex.ru\"!")

# Сохранение данных в csv
def save_data_to_csv(data, filename="data.csv"):
    import pandas
    for row in range(0, len(data["titles"])):
        # Берём старые данные записанные в файл csv
        df = pandas.read_csv(filename,
                             header=0,
                             names=["titles", "contents", "dates", "tags"])
        # Создаём новые данные, которые приняли на входе
        df2 = pandas.DataFrame({"titles": [data["titles"][row]], "contents": [data["contents"][row]], "dates": [data["dates"][row]], "tags": [", ".join(data["tags"][row]) if data["tags"][row] else ""]})
        # Соединяем данные
        df = pandas.concat([df, df2], ignore_index=True)
        # Сохраняем данные
        df.to_csv(filename)
    log_msg(f"Data is saved in \"{filename}\"")


def main():
    log_msg("Parser started!")
    ozon_data = ozon_parser()
    yandex_data = yandex_parser()
    save_data_to_csv(yandex_data, filename="yandex_data.csv")
    save_data_to_csv(ozon_data, filename="ozon_data.csv")


if __name__ == '__main__':
    main()
