from pybit.unified_trading import HTTP
from dotenv import load_dotenv
import os
import json

# Загружаем ключи из .env
load_dotenv()
# Подключаемся к ByBit
session = HTTP(
    api_key=os.getenv("BYBIT_API_KEY"),
    api_secret=os.getenv("BYBIT_SECRET_KEY")
)

# 1. Получаем текущую цену BTC
ticker = session.get_tickers(category="spot", symbol="BTCUSDT")
current_price = float(ticker["result"]["list"][0]["lastPrice"])
print(f"Текущая цена BTC: {current_price} USDT")

# 2. Новые минимальные лимиты (из правил ByBit)
MIN_BTC = 0.000011  # 0.000011 BTC
MIN_USDT = 1.0      # 1 USDT

# 3. Рассчитываем сумму ордера
available_usdt = 17.00  # Ваш доступный баланс
btc_amount = round(available_usdt / current_price / 1.1, 6)
print(btc_amount)

# Проверяем оба лимита:
if btc_amount < MIN_BTC or available_usdt < MIN_USDT:
    print(f"Ошибка: Ордер слишком мал. Минимум: {MIN_BTC} BTC или {MIN_USDT} USDT")
    # Автоматически увеличиваем до минималки
    btc_amount = max(MIN_BTC, MIN_USDT/current_price)
    print(f"Скорректированный объём: {btc_amount:.8f} BTC")

# 4. Отправляем ордер
try:
    response = session.place_order(
        category="spot",
        symbol="BTCUSDT",
        side="Buy",
        orderType="Market",
        #qty=str(btc_amount)
        qty=f"{btc_amount:.8f}".rstrip('0').rstrip('.') if '.' in f"{btc_amount:.8f}" else f"{btc_amount:.8f}",
        marketUnit="baseCoin"
    )
    print("✅ Ордер успешно исполнен!")
    print("Детали:", response)
except Exception as e:
    print("❌ Ошибка:", e)
    print("Проверьте:")
    print("1. Достаточно ли USDT для комиссии")
    print("2. Актуальные лимиты в Rules → https://www.bybit.com/en/announcement-info/spot-trading-rules/")
