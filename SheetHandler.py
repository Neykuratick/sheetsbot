import gspread
from ConnectSheet import ConnectSheet


class SheetHandler:
    def __init__(self):
        workingSpreadsheetId = '1vnJX2rVhxHyvWecD7hgi1naDUD4nfbgg3-_B1u39J8A'

        self.gc = gspread.service_account(filename='credentials.json')
        self.sh = self.gc.open_by_key(workingSpreadsheetId)
        self.worksheet = self.sh.get_worksheet(1)

    def deleteWorksheet(self):
        try:
            self.sh.del_worksheet(self.worksheet)
        except:
            return False
        return True

    def copySheet(self):
        ConnectSheet.createCopy()
