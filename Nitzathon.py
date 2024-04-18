PHYSICAl = "מי שנפצע זכאים לקבל את הטיפולים והשירותים הרפואיים שכלולים בסך הבריאות.\n בנוסף הנפגעים זכאים למימון או החזר עבור טיפולים ושירותים שלא כלולים בסל הבריאות, אם הם נובעים לצורך רפואי שקשור לפגיעה, כמו:\nתרופות שלא כלולות בסל, טיפולי שיניים, רפואה משלימהף קנביס רפואי וכו'.\n פנייה לגורמי סיוע 0529993544"
MENTAL = "על מנת לממש זכויות שונות, רפואיות וכספיות, יש צורך לפנות לשלטונות הצבא (במידה והנכות אירעה בזמן שירות צבאי) לרשויות הבריאות או לביטוח לאומי.\nבביטוח הלאומי נבדקת לא רק הנכות עצמה אלא גם הפגיעה שלה ביכולת התפקוד של הנכה\nבמידה והיא משמעותית יהיה זכאי הנכה לפיצוי חד פעמי או לקצבת קבועה – קצבת נכות.\nפנייה לגורמי סיוע 0529993544"
HOUSING = "להתקשר לקרן פיצויי פעולות איבה של מס רכוש במספר *4954, לבחור שלוחה לפי אזור מגורים, להשאיר פרטים של מיקום המבנה שנפגע ופרטים אישיים ולבקש לשלוח שמאי.\nפנייה לגורמי סיוע *4954"
EVACUEES = "המדינה מסייעת להעברת המפונים לבתי מלון ובתי הארחה במימון מלא של המדינה. משרד התיירות קיבל אחריות על העבודה מול בתי המלון ופתח חמל.\nמספר הטלפון של החמ'ל לפניות הציבור, הרשויות ולהצעת חדרים הוא 03-6394980\nאנשים עם מוגבליות:\nאנשים עם מוגבלות שפונו מבתיהם עשויים להיות זכאים לסיוע ברכישה או השאלה של עזרים הנחוצים לביצוע פעולות יומיומיות במקום מגוריהם החלופי.\nהסיוע ניתן לאנשים הזכאים לשירותים ממנהל מוגבלויות במשרד הרווחה או מהיחידה לשיקום וניידות במשרד הבריאות.\nהסיוע ניתן בהתאמה אישית של עזרים שאינם מחייבים התקנה או שינויים מבניים.\nאזרחים ותיקים:\nאזרחים ותיקים יוכלו לעבור מהמלונות שפונו אליהם לבתי דיור מוגן ולבתי אבות שבפיקוח משרד הרווחה\nמשרד הרווחה יממן את השהות של האזרחים הוותיקים בבתים אלה.\nניתן לקבל פרטים במוקד הטלפוני של משרד הרווחה 118."

def main():
    print("תאר כיצד נפגעת")
    hurt_right()
    house_right()
    evacuees_right()
def hurt_right():
    hurt = input("1.פגיעה נפשית 2.פגיעה פיזית 3.לא נפגעתי כלל ")
    while (hurt != '1') and (hurt != '2') and (hurt != '3'):
        hurt = input("תאר כיצד נפגעת\n1.פגיעה נפשית 2.לא נפגעתי כלל 3.פגיעה פיזית ")
    if hurt == '1':
        print(MENTAL)
    elif hurt == '2':
        print(PHYSICAl)

def house_right():
    house = input("האם ביתך נפגע בעקבות המלחמה. (כן / לא) ")
    while (house != 'כן') and (house != 'לא'):
        house = input("האם ביתך נפגע בעקבות המלחמה. (כן / לא) ")
    if house == 'כן':
        print(HOUSING)

def evacuees_right():
    evacuees = input("האם פונית מביתך במהלך המלחמה. (כן / לא) ")
    while (evacuees != 'כן') and (evacuees != 'לא'):
        evacuees = input("האם פונית מביתך במהלך המלחמה. (כן / לא) ")
    if evacuees == 'כן':
        print(EVACUEES)
