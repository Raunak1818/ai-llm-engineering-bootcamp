class ChaiUtils:

    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
        

    
raw = "milk  ,   water ,  ginger , honey "

cleaned = ChaiUtils.clean_ingredients(raw)
print(cleaned)
