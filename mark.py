from colorama import Fore # type: ignore

class MarkTypeEnum:
    FO = 0
    SO = 1
    CSOCH = 2

class PropertyEnum:
    MARK = 0
    MAX_PERCENT = 1
    COMMENT = 2
    COLOR = 3
    COST = 4

class Mark:
    properties_variants = [
    	[0, 100.1, "А вот врать не надо", Fore.RED, 0],
    	[5, 100.0, "Офигеть", Fore.MAGENTA, 2000],
    	[5, 86.0, "Круто", Fore.BLUE, 2000],
    	[4, 66.0, "Хорошо", Fore.GREEN, 1000],
    	[3, 30.0, "Так себе", Fore.YELLOW, 500],
    	[2, 0.0, "Офигеть", Fore.RED, -1000],
	]
    def __init__(self, value, max_value=10, type=MarkTypeEnum.FO):
        self.value = value
        self.max_value = value
        self.type = type
        self.percent = self.get_percent(value, max_value)
        self.properties = self.get_properties(self.percent)
        self.mark = self.properties[PropertyEnum.MARK]
        self.comment = self.properties[PropertyEnum.COMMENT]
        self.color = self.properties[PropertyEnum.COLOR]
        self.cost = self.get_cost(self.type)
        self.info = self.get_info()

    def get_percent(self, value, max_value) -> float:
        return round(float(value*100/max_value), 2)

    def get_properties(self, percent) -> list:
        for variant in Mark.properties_variants:
            if variant[PropertyEnum.MAX_PERCENT] <= percent:
                return variant

    def get_cost(self, type) -> float:
        # шедеврокостыль
        if self.value != 7:
            cost = self.properties[PropertyEnum.COST]
        else:
            cost = 500
        match type:
            case MarkTypeEnum.FO | MarkTypeEnum.SO:
                return cost
            case MarkTypeEnum.CSOCH:
                return cost*2

    def get_info(self) -> str:
        return self.color+f"{self.comment}! Оценка - {self.mark}. Процент - {self.percent}%, стоимость - {self.cost}."+Fore.WHITE
