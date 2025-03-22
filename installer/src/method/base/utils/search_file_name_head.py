# coding: utf-8
# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# import
import os
import pandas as pd
from typing import List

# 自作モジュール
from method.base.utils.logger import Logger
from method.base.utils.path import BaseToPath


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# **********************************************************************************


class SearchFileNameHead:
    def __init__(self):
        # logger
        self.getLogger = Logger()
        self.logger = self.getLogger.getLogger()

        # インスタンス
        self.path = BaseToPath()


    ####################################################################################
    # 指定のPathにファイル名の頭部分を指定して検索

    def get_search_file_name_head(self, search_folder_path: str, file_name_head: str, extension: str):
        try:
            search_file_name_parts = f"{file_name_head}*{extension}"
            self.logger.debug(f'search_file_name_parts: {search_file_name_parts}')

            matching_files = list(search_folder_path.glob(search_file_name_parts))

            if not matching_files:
                self.logger.warning(f'{self.__class__.__name__} 指定されているパターンのファイルがありませんでした: {file_name_head}*.{extension}')
                return None

            elif matching_files[1]:
                self.logger.warning(f'{self.__class__.__name__} 指定のファイルが複数あるためエラー: {file_name_head}*.{extension}')
                return None

            searched_file = matching_files[0]
            self.logger.debug(f'searched_file: {searched_file}')
            return searched_file

        except Exception as e:
            self.logger.error(f'{self.__class__.__name__} 指定のPathにファイル名の頭部分を指定して検索の処理中にエラーが発生: {e}')

    ####################################################################################

    # ----------------------------------------------------------------------------------



    # ----------------------------------------------------------------------------------



    # ----------------------------------------------------------------------------------
