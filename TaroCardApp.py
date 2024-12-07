import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton
from PyQt6.QtGui import QPixmap, QFont
from PyQt6.QtCore import Qt

# Tarot dictionary
tarot_dictionary = {
    0: {"name": "The Fool", "meaning": "คนโง่เง่าย์, การผจญภัย, การมุ่งมั่น, การเริ่มต้นใหม่"},
    1: {"name": "The Magician", "meaning": "นักมายากล, การสร้างสรรค์, การใช้ทักษะ, ความสามารถในการสร้างสรรค์"},
    2: {"name": "The High Priestess", "meaning": "นางสมเด็จพระราชินี, ความลึกซึ้ง, ความลับ, การเชื่อมต่อกับความลึกซึ้งในใจ"},
    3: {"name": "The Empress", "meaning": "จักรพรรดินี, ความอุดมสมบูรณ์, ความรัก, ความเป็นแม่"},
    4: {"name": "The Emperor", "meaning": "จักรพรรดิ, ความมั่นคง, ความเข้มแข็ง, ความเป็นผู้บังคับบัญชา"},
    5: {"name": "The Hierophant", "meaning": "เจ้าอาวาส, ความเชื่อ, การเรียนรู้, ความเชื่อมั่นในความเป็นที่ยอมรับ"},
    6: {"name": "The Lovers", "meaning": "คู่รัก, ความรัก, ความสัมพันธ์, การเลือกของชีวิต"},
    7: {"name": "The Chariot", "meaning": "รถบรรทุก, ความก้าวหน้า, การควบคุม, การเคลื่อนไหว"},
    8: {"name": "Strength", "meaning": "ความแข็งแกร่ง, การต่อสู้, การควบคุมอารมณ์, ความเข้มงวด"},
    9: {"name": "The Hermit", "meaning": "นักอพยพ, ความเงียบสงบ, การค้นพบตนเอง, การปฏิบัติตามความเชื่อ"},
    10: {"name": "Wheel of Fortune", "meaning": "วงล้อของโชคลาภ, โชคชะตา, การเปลี่ยนแปลง, โอกาสที่กำลังจะมา"},
    11: {"name": "Justice", "meaning": "ความยุติธรรม, ความเท่าเทียม, การตัดสิน, การมีความรับผิดชอบ"},
    12: {"name": "The Hanged Man", "meaning": "คนติดขัด, การสละสิทธิ์, การเสียสละ, การพิสูจน์ความเชื่อ"},
    13: {"name": "Death", "meaning": "ความตาย, การเปลี่ยนแปลง, การสิ้นสุด, การให้การตัดสินใจ"},
    14: {"name": "Temperance", "meaning": "ความสงบสติ, ความสมดุล, ความอ่อนโยน, การรวมกันของสิ่งตรงข้าม"},
    15: {"name": "The Devil", "meaning": "ปีศาจ, ความหลงลืม, การขัดแย้ง, การต่อสู้กับความจริง"},
    16: {"name": "The Tower", "meaning": "หอคอยทรุดโทรม, การทดลอง, การทดสอบ, การทำลายและการสร้างใหม่"},
    17: {"name": "The Star", "meaning": "ดาว, ความหวัง, ความสดใส, ความสุข"},
    18: {"name": "The Moon", "meaning": "ดวงจันทร์, ความสับสน, ความกลัว, การมุ่งหน้าไปที่ความรู้สึก"},
    19: {"name": "The Sun", "meaning": "ดวงอาทิตย์, ความสุข, ความเจริญรุ่งเรือง, ความมั่นคง"},
    20: {"name": "Judgement", "meaning": "การตัดสิน, การประกาศ, การเปลี่ยนแปลง, การตื่นตัว"},
    21: {"name": "The World", "meaning": "โลก, ความสมบูรณ์, ความสำเร็จ, การเชื่อมต่อทั่วโลก"},
    22: {"name": "Ace of Wands", "meaning": "ใบหนึ่งของไม้เท้า, การเริ่มต้นใหม่, ความคิดสร้างสรรค์, การกระตุ้น"},
    23: {"name": "Two of Wands", "meaning": "ใบสองของไม้เท้า, การตัดสินใจ, การวางแผน, การมองไปสู่อนาคต"},
    24: {"name": "Three of Wands", "meaning": "ใบสามของไม้เท้า, ความสำเร็จ, การขยายออกไป, การคาดการณ์"},
    25: {"name": "Four of Wands", "meaning": "ใบสี่ของไม้เท้า, ความสงบ, ความสุข, การเฉลิมฉลอง"},
    26: {"name": "Five of Wands", "meaning": "ใบห้าของไม้เท้า, การปะทะ, การปั่นป่วน, การป้องกัน"},
    27: {"name": "Six of Wands", "meaning": "ใบหกของไม้เท้า, ความชัยชนะ, ความสำเร็จ, การได้รับความยินดี"},
    28: {"name": "Seven of Wands", "meaning": "ใบเจ็ดของไม้เท้า, การป้องกัน, การต่อสู้กับความเป็นอันตราย, การก้าวขึ้นมา"},
    29: {"name": "Eight of Wands", "meaning": "ใบแปดของไม้เท้า, การเคลื่อนไหว, ความรวดเร็ว, ความก้าวหน้า"},
    30: {"name": "Nine of Wands", "meaning": "ใบเก้าของไม้เท้า, ความคลั่งไคล้, การป้องกัน, การคงไว้"},
    31: {"name": "Ten of Wands", "meaning": "ใบสิบของไม้เท้า, การฝ่าฝืน, ความมีภาระหนัก, การรับผิดชอบมากเกินไป"},
    32: {"name": "Page of Wands", "meaning": "หน้าใบของไม้เท้า, การประชด, การค้นพบความคิดใหม่, ความคิดสร้างสรรค์"},
    33: {"name": "Knight of Wands", "meaning": "อัศวินของไม้เท้า, การตื่นตัว, ความกระตือรือร้น, การเร่งรีบ"},
    34: {"name": "Queen of Wands", "meaning": "ราชินีของไม้เท้า, การเป็นผู้นำ, ความมั่นคง, ความอ่อนโยน"},
    35: {"name": "King of Wands", "meaning": "กษัตริย์ของไม้เท้า, การมีสมาธิ, ความมั่นคง, การมีพลัง"},
    36: {"name": "Ace of Cups", "meaning": "ใบหนึ่งของถ้วย, ความรัก, ความสุข, ความอารมณ์"},
    37: {"name": "Two of Cups", "meaning": "ใบสองของถ้วย, ความรักแท้, ความสัมพันธ์, ความร่วมมือ"},
    38: {"name": "Three of Cups", "meaning": "ใบสามของถ้วย, ความเป็นมิตร, ความสุข, การเฉลิมฉลอง"},
    39: {"name": "Four of Cups", "meaning": "ใบสี่ของถ้วย, ความไม่พอใจ, การมองหาความสุข, การหลบหนี"},
    40: {"name": "Five of Cups", "meaning": "ใบห้าของถ้วย, ความเสียใจ, ความสูญเสีย, การตัดสินใจ"},
    41: {"name": "Six of Cups", "meaning": "ใบหกของถ้วย, ความทรงจำ, ความรักในอดีต, ความสุขในวัยเด็ก"},
    42: {"name": "Seven of Cups", "meaning": "ใบเจ็ดของถ้วย, ความฝัน, ความเหมือนจริง, ความสับสน"},
    43: {"name": "Eight of Cups", "meaning": "ใบแปดของถ้วย, การละทิ้ง, การก้าวออกไป, การมองหาความหมายใหม่"},
    44: {"name": "Nine of Cups", "meaning": "ใบเก้าของถ้วย, ความพอใจ, ความสุข, ความสำเร็จ"},
    45: {"name": "Ten of Cups", "meaning": "ใบสิบของถ้วย, ความสุข, ความพอใจ, ความสมหวัง"},
    46: {"name": "Page of Cups", "meaning": "หน้าใบของถ้วย, ความเพ้อเจ้อ, ความรักในวัยเด็ก, ความสร้างสรรค์"},
    47: {"name": "Knight of Cups", "meaning": "อัศวินของถ้วย, ความโรแมนติก, ความอ่อนโยน, การตื่นเต้น"},
    48: {"name": "Queen of Cups", "meaning": "ราชินีของถ้วย, ความสง่างาม, ความเป็นมารตี, ความอบอุ่น"},
    49: {"name": "King of Cups", "meaning": "กษัตริย์ของถ้วย, ความอ่อนโยน, ความเข้มงวด, ความสง่างาม"},
    50: {"name": "Ace of Pentacles", "meaning": "ใบหนึ่งของเหรียญ, ความมั่นคง, ความเจริญรุ่งเรือง, โอกาสทางการเงิน"},
    51: {"name": "Two of Pentacles", "meaning": "ใบสองของเหรียญ, ความสมดุล, การจัดการเงิน, การปรับตัว"},
    52: {"name": "Three of Pentacles", "meaning": "ใบสามของเหรียญ, การทำงานร่วมกัน, ความสามารถในการสร้างสรรค์, ความสำเร็จในงาน"},
    53: {"name": "Four of Pentacles", "meaning": "ใบสี่ของเหรียญ, การควบคุม, ความมั่นคง, ความขี้หวง"},
    54: {"name": "Five of Pentacles", "meaning": "ใบห้าของเหรียญ, ความขัดแย้ง, ความยากจน, ความสูญเสีย"},
    55: {"name": "Six of Pentacles", "meaning": "ใบหกของเหรียญ, การให้, ความกรุณา, ความสามารถในการส่งเสริม"},
    56: {"name": "Seven of Pentacles", "meaning": "ใบเจ็ดของเหรียญ, ความรอคอย, การประเมิน, การเติบโต"},
    57: {"name": "Eight of Pentacles", "meaning": "ใบแปดของเหรียญ, การทำงานหนัก, การพัฒนาทักษะ, การพัฒนาด้านการงาน"},
    58: {"name": "Nine of Pentacles", "meaning": "ใบเก้าของเหรียญ, ความสง่างาม, ความเรียบง่าย, ความเป็นอิสระ"},
    59: {"name": "Ten of Pentacles", "meaning": "ใบสิบของเหรียญ, ความมั่งคั่ง, ความสุข, ความเป็นสมบูรณ์"},
    60: {"name": "Page of Pentacles", "meaning": "หน้าใบของเหรียญ, ความพยายาม, การเรียนรู้, การพัฒนาทักษะ"},
    61: {"name": "Knight of Pentacles", "meaning": "อัศวินของเหรียญ, ความมุ่งมั่น, ความเสถียร, การทำงานหนัก"},
    62: {"name": "Queen of Pentacles", "meaning": "ราชินีของเหรียญ, ความเข้มแข็ง, ความมั่นคง, ความเมตตา"},
    63: {"name": "King of Pentacles", "meaning": "กษัตริย์ของเหรียญ, ความเจริญรุ่งเรือง, ความมั่นคง, การมีอิสระ"},
    64: {"name": "Ace of Swords", "meaning": "ใบหนึ่งของดาบ, ความจริง, การตัดสินใจ, ความรู้สึก"},
    65: {"name": "Two of Swords", "meaning": "ใบสองของดาบ, ความตัดสินใจ, การต่อสู้ในใจ, ความปิติยินดี"},
    66: {"name": "Three of Swords", "meaning": "ใบสามของดาบ, ความเศร้าโศก, การบาดเจ็บใจ, ความทุกข์"},
    67: {"name": "Four of Swords", "meaning": "ใบสี่ของดาบ, การพักผ่อน, การฟื้นฟู, การสงบใจ"},
    68: {"name": "Five of Swords", "meaning": "ใบห้าของดาบ, การแพ้, การเสียใจ, การถูกหลอกลวง"},
    69: {"name": "Six of Swords", "meaning": "ใบหกของดาบ, การเดินทาง, การย้ายที่อยู่, การเคลื่อนย้าย"},
    70: {"name": "Seven of Swords", "meaning": "ใบเจ็ดของดาบ, การขโมย, การหลบหนี, การฉ้อโกง"},
    71: {"name": "Eight of Swords", "meaning": "ใบแปดของดาบ, ความโดดเดี่ยว, ความขัดข้อง, การจำกัด"},
    72: {"name": "Nine of Swords", "meaning": "ใบเก้าของดาบ, ความกังวล, ความหวังสุดท้าย, ความกดดัน"},
    73: {"name": "Ten of Swords", "meaning": "ใบสิบของดาบ, การล่มสลาย, ความเสียหาย, การสิ้นสุด"},
    74: {"name": "Page of Swords", "meaning": "หน้าใบของดาบ, การสื่อสาร, ความขยัน, ความคิดสร้างสรรค์"},
    75: {"name": "Knight of Swords", "meaning": "อัศวินของดาบ, การเร่งรีบ, ความกล้าหาญ, การต่อสู้"},
    76: {"name": "Queen of Swords", "meaning": "ราชินีของดาบ, ความชาญฉลาด, ความเจริญ, ความตัดสินใจ"},
    77: {"name": "King of Swords", "meaning": "กษัตริย์ของดาบ, ความรู้สึก, ความเจริญรุ่งเรือง, ความตัดสินใจ"},
}

class TarotApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Tarot Card Reader')
        self.mainLayout = QVBoxLayout()
        self.cardLayout = QHBoxLayout()

        # ปุ่มเสี่ยงทาย
        self.drawButton = QPushButton('เสี่ยงทาย')
        self.drawButton.setFont(QFont('Arial', 14, QFont.Weight.Bold))
        self.drawButton.setStyleSheet("background-color: #8A2BE2; color: white; border-radius: 10px; padding: 10px;")
        self.drawButton.clicked.connect(self.drawCards)

        self.mainLayout.addWidget(self.drawButton)
        self.mainLayout.addLayout(self.cardLayout)

        self.setLayout(self.mainLayout)
        self.resize(800, 350)

    def drawCards(self):
        # ล้างการ์ดเก่าออกก่อนหากมี
        self.clearLayout(self.cardLayout)

        # เสี่ยงทายการ์ดใหม่
        picked_cards = random.sample(list(tarot_dictionary.keys()), min(3, len(tarot_dictionary)))
        print(picked_cards)
        for card_number in picked_cards:
            card_info = tarot_dictionary[card_number]

            # Image label
            img_label = QLabel()
            pixmap = QPixmap(f'tarotimages/{card_number}.jpg').scaled(200, 300, Qt.AspectRatioMode.KeepAspectRatio)
            img_label.setPixmap(pixmap)

            # Text label for name and meaning
            text_label = QLabel(f"{card_info['name']}\n{card_info['meaning']}")
            text_label.setFont(QFont('Arial', 10))
            text_label.setStyleSheet("color: #000005;")
            text_label.setWordWrap(True)

            # สร้าง layout ใหม่สำหรับแต่ละการ์ดและเพิ่มใน cardLayout
            cardLayout = QVBoxLayout()
            cardLayout.addWidget(img_label)
            cardLayout.addWidget(text_label)

            self.cardLayout.addLayout(cardLayout)

    def clearLayout(self, layout):
        while layout.count():
            item = layout.takeAt(0)      
            if item.widget():
                item.widget().deleteLater()
           
            elif item.layout():
                self.clearLayout(item.layout())  
                item.layout().deleteLater()  


def main():
    app = QApplication(sys.argv)
    ex = TarotApp()
    ex.show()
    sys.exit(app.exec())

if __name__ == '__main__':
    main()