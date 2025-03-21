# coding: utf-8
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# export PYTHONPATH="/Users/nyanyacyan/Desktop/project_file/multi_site_post_flow/installer/src"

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import
from typing import Dict
from datetime import datetime
from selenium.webdriver.chrome.webdriver import WebDriver

# 自作モジュール
from method.base.utils.logger import Logger
from method.base.selenium.chrome import ChromeManager
from method.base.selenium.loginWithId import SingleSiteIDLogin
from method.base.selenium.seleniumBase import SeleniumBasicOperations
from method.base.spreadsheet.spreadsheetRead import GetDataGSSAPI
from method.base.selenium.get_element import GetElement
from method.base.decorators.decorators import Decorators
from method.base.utils.time_manager import TimeManager
from method.base.selenium.google_drive_download import GoogleDriveDownload
from method.base.spreadsheet.spreadsheetWrite import GssWrite
from method.base.spreadsheet.select_cell import GssSelectCell
from method.base.spreadsheet.err_checker_write import GssCheckerErrWrite
from method.base.utils.popup import Popup

# const
from method.const_element import GssInfo, LoginInfo, ErrCommentInfo, PopUpComment

deco = Decorators()

# ----------------------------------------------------------------------------------
# **********************************************************************************
# 一連の流れ

class PrepareFlow:
    def __init__(self, chrome: WebDriver):
        # logger
        self.getLogger = Logger()
        self.logger = self.getLogger.getLogger()

        # chrome
        self.chrome = chrome

        # 必要info
        self.gss_info = GssInfo.LGRAM.value

        # インスタンス
        self.login = SingleSiteIDLogin(chrome=self.chrome)
        self.random_sleep = SeleniumBasicOperations(chrome=self.chrome)
        self.get_element = GetElement(chrome=self.chrome)
        self.time_manager = TimeManager()
        self.selenium = SeleniumBasicOperations(chrome=self.chrome)
        self.gss_read = GetDataGSSAPI()
        self.gss_write = GssWrite()
        self.drive_download = GoogleDriveDownload()
        self.select_cell = GssSelectCell()
        self.gss_check_err_write = GssCheckerErrWrite()
        self.popup = Popup()

        # const
        self.const_gss_info = GssInfo.LGRAM.value
        self.const_login_info = LoginInfo.LGRAM.value
        self.const_err_cmt_dict = ErrCommentInfo.LGRAM.value
        self.popup_cmt = PopUpComment.LGRAM.value



        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")

    ####################################################################################
    # 準備工程 スプシチェッカー > 写真のダウンロード > 動画のダウンロード

    def prepare_process( self, gss_row_data: Dict, gss_info: Dict, err_datetime_cell: str, err_cmt_cell: str, ):
        try:
            pass
            # 対象の分析をクリック

            # 一括ダウンロードをクリック

            # Zipファイルの移動

            # zipの解凍

            # 対象ファイルのPathを取得

            # アップロードファイルに移動


        except Exception as e:
            self.logger.error(f"{self.__class__.__name__}処理中にエラーが発生: {e}")

        self.logger.info(f'【{gss_row_data[self.const_gss_info["NAME"]]}】準備完了')
        self.logger.info(f'image_path: {image_path}\nmovie_path: {movie_path}')
        return image_path, movie_path

# ----------------------------------------------------------------------------------
