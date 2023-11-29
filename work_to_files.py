import json
import os
import ast


class Meridian:
    def __init__(self):
        self.__file = ""

    @property
    def file(self):
        """
        Возвращает путь к файлу.
        :return:
        """
        return self.__file

    @file.setter
    def file(self, file):
        """
        Сохраняет путь к файлу.
        :param file:
        :return:
        """
        self.__file = file

    def file_job(self) -> None:
        """
        Формирует тхт-файл на рабочем столе из файла задания.
        """
        file_name = os.path.splitext(os.path.basename(self.__file))[0]
        home_dir = os.path.expanduser('~')
        with (open(f"{self.__file}", encoding="UTF-8") as file_load,
              open(f"{home_dir}/Desktop/full_{file_name}.txt", "w", encoding="UTF-8") as file_save):
            code_list = []
            for element in json.load(file_load)["Packs"]:
                code_list.append("01" + element["ai"]["01"] + "21" + element["ai"]["21"] +
                                 "93" + element["ai"]["93"] + "\n")
            for row in code_list:
                file_save.write(row)


    def file_defect(self) -> None:
        """
        Формирует тхт-файл на рабочем столе из файла брака.
        """
        file_name = os.path.splitext(os.path.basename(self.__file))[0]
        home_dir = os.path.expanduser('~')
        with (open(f"{self.__file}", encoding="UTF-8") as file_load,
              open(f"{home_dir}/Desktop/full_{file_name}.txt", "w", encoding="UTF-8") as file_save):
            code_list = []
            for element in file_load.readlines():
                temp_dict = ast.literal_eval(element.replace("\n", ""))
                code_list.append("01" + temp_dict["01"] + "21" + temp_dict["21"] + "93" + temp_dict["93"] + "\n")
            for row in code_list:
                file_save.write(row)
