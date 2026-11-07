import math

C_ACTIVE: float = 1.0 #активная нагрузка
C_IND: float = 0.85 #индуктивная 
C_SM: float = 0.75 #смешанная

U_MIN: float = 12.0   #напряжение В
U_MAX: float = 1000.0
I_MIN: float = 0.1   #ток А
I_MAX: float = 500.0

U_SMALL_LIMIT: float = 220.0 #малое напряжение
U_LARGE_LIMIT: float = 400.0 #высокое напряжение

LOG_FILE: str = 'input_errors_log' #вывод логов ошибок