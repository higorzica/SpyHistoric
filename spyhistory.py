import os
import sqlite3

def main():
    userPath = 'C:\\Users\\' + os.getlogin()
    historyPath = userPath + '\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'
    desktopPath = userPath + '\\Desktop\\'

    connection = sqlite3.connect(historyPath)
    cursor = connection.cursor()

    cursor.execute("SELECT title, url, last_visit_time FROM urls ORDER BY last_visit_time DESC LIMIT 5")
    data = cursor.fetchall()

    with open(desktopPath + 'HistoricoEspiao.txt', 'w', encoding='utf-8') as myFile:
        for i in data:
            for j in i:
                # print(j)
                myFile.write(str(j) + '\n')
            myFile.write('\n')


if __name__ == '__main__':
    main()