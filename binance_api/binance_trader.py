from binance.client import Client
from dotenv import load_dotenv
import os

# Загрузка переменных окружения из .env
load_dotenv()

# Получение API-ключей из переменных окружения
api_key = os.getenv("BINANCE_API_KEY")
api_secret = os.getenv("BINANCE_SECRET_KEY")

# Подключение к клиенту Binance
client = Client(api_key, api_secret)

# Пример использования: получение текущей цены BTC/USDT
btc_price = client.get_symbol_ticker(symbol="BTCUSDT")
print(f"Текущая цена BTC/USDT: {btc_price['price']}")


# # Получение исторических данных (например, за последние 24 часа)
# klines = client.get_historical_klines("BTCUSDT", Client.KLINE_INTERVAL_1HOUR, "24 hours ago UTC")
# for kline in klines:
#     print(kline)

# # Получение исторических данных за последние 3 часа с интервалом в 1 минуту
# symbol = "BTCUSDT"
# interval = Client.KLINE_INTERVAL_1MINUTE
# klines = client.get_historical_klines(symbol, interval, "3 hours ago UTC")

# # Извлечение времени и цен закрытия
# times = []
# prices = []

# for kline in klines:
#     timestamp = int(kline[0]) / 1000  # Время открытия свечи (в секундах)
#     time_str = datetime.datetime.fromtimestamp(timestamp)  # Преобразуем в читаемый формат
#     close_price = float(kline[4])  # Цена закрытия

#     times.append(time_str)
#     prices.append(close_price)

# # Построение графика
# plt.figure(figsize=(10, 6))  # Размер графика
# plt.plot(times, prices, label=f"{symbol} Price", color='blue')  # Линия графика
# plt.title(f"{symbol} Price Over Last 3 Hours")  # Заголовок
# plt.xlabel("Time")  # Ось X: Время
# plt.ylabel("BTC Price (USDT)")  # Ось Y: Цена
# plt.xticks(rotation=45)  # Поворот меток времени для удобства чтения
# plt.grid(True)  # Сетка
# plt.legend()  # Легенда
# plt.tight_layout()  # Улучшение отображения
# plt.show()  # Показать график

# # Создание тестового ордера (не реального)
# try:
#     order = client.create_test_order(
#         symbol="BTCUSDT",
#         side=Client.SIDE_BUY,
#         type=Client.ORDER_TYPE_MARKET,
#         quantity=0.01
#     )
#     print("Тестовый ордер создан!")
# except Exception as e:
#     print(f"Ошибка: {e}")

# Получение информации об аккаунте
account_info = client.get_account()

# # Вывод всех активов и их балансов
# print("Твои активы:")
# for asset in account_info['balances']:
#     asset_name = asset['asset']  # Название актива (например, BTC, USDT)
#     free_balance = float(asset['free'])  # Доступный баланс
#     locked_balance = float(asset['locked'])  # Замороженный баланс (например, для ордеров)
#     total_balance = free_balance + locked_balance  # Общий баланс

#     if total_balance > 0:  # Показываем только активы с ненулевым балансом
#         print(f"{asset_name}:")
#         print(f"  Доступно: {free_balance}")
#         print(f"  Заморожено: {locked_balance}")
#         print(f"  Всего: {total_balance}")
#         print("-" * 30)

# # Получение информации о торговой паре ETH/USDT
# symbol_info = client.get_symbol_info(symbol="ETHUSDT")

# # Вывод всей информации
# # print(symbol_info)

# # Поиск фильтра NOTIONAL
# for filter in symbol_info['filters']:
#     if filter['filterType'] == 'NOTIONAL':
#         min_notional = float(filter['minNotional'])
#         print(f"Минимальная стоимость ордера для ETH/USDT: {min_notional} USDT")
#         break

# # Поиск фильтра LOT_SIZE
# for filter in symbol_info['filters']:
#     if filter['filterType'] == 'LOT_SIZE':
#         min_qty = float(filter['minQty'])  # Минимальное количество
#         step_size = float(filter['stepSize'])  # Шаг количества
#         print(f"Минимальное количество ETH: {min_qty}")
#         print(f"Шаг количества ETH: {step_size}")
#         break


# # Округление до шага
# def round_step_size(quantity, step_size):
#     return math.floor(quantity / step_size) * step_size

# # Получение цены ETH/USDT
# eth_price = client.get_symbol_ticker(symbol="ETHUSDT")
# print(f"Текущая цена ETH/USDT: {eth_price['price']}")
# min_order = round(min_notional * 1.1 / float(eth_price['price']), 6)
# print(min_order)

# # Округление min_order
# min_order_rounded = round_step_size(min_order, step_size)
# print(f"Округлённое количество ETH: {min_order_rounded}")

# if min_order_rounded < min_qty:
#     min_order_rounded = min_qty
# print(f"Итоговое количество ETH: {min_order_rounded}")

# # Получение баланса ETH
# eth_balance = client.get_asset_balance(asset='ETH')
# free_eth = float(eth_balance['free'])  # Доступный баланс
# locked_eth = float(eth_balance['locked'])  # Замороженный баланс
# print(f"Доступный баланс ETH: {free_eth}")
# print(f"Замороженный баланс ETH: {locked_eth}")

# # Создание реального ордера
# try:
#     order = client.create_order(
#         symbol="ETHUSDT",
#         side=Client.SIDE_BUY,
#         type=Client.ORDER_TYPE_MARKET,
#         quantity=min_order_rounded
#     )
#     print("Тестовый ордер создан!")
# except Exception as e:
#     print(f"Ошибка: {e}")
