from exception import CustomException

def crash():
    try:
        a = 10 / 0   # 💥 intentional error
    except Exception as e:
        raise CustomException(e)

crash()
