from colorama import Fore # type: ignore
from lang.labels import labels

class MarkTypeEnum:
    FA = 0
    SA = 1
    CSAQ = 2

class PropertyEnum:
    MARK = 0
    MAX_PERCENT = 1
    COMMENT = 2
    COLOR = 3
    COST = 4

class Mark:
    properties_variants = [
    	[0, 100.1, labels.error_mark_comment, Fore.RED, 0],
    	[5, 100.0, labels.wow_mark_comment, Fore.MAGENTA, 2000],
    	[5, 86.0, labels.cool_mark_comment, Fore.BLUE, 2000],
    	[4, 66.0, labels.nice_mark_comment, Fore.GREEN, 1000],
    	[3, 30.0, labels.okay_mark_comment, Fore.YELLOW, 500],
    	[2, 0.0, labels.wow_mark_comment, Fore.RED, -1000],
	]
    def __init__(self, value, max_value=10, type=MarkTypeEnum.FA):
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
            case MarkTypeEnum.FA | MarkTypeEnum.SA:
                return cost
            case MarkTypeEnum.CSAQ:
                return cost*2

    def get_info(self) -> str:
        return self.color+f"{self.comment}! {labels.mark} - {self.mark}. {labels.percent} - {self.percent}%, {labels.cost} - {self.cost}."+Fore.WHITE
