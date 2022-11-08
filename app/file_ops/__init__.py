"""File operations """
import os
import pandas


class FileOperations:
    """File operations"""
    @staticmethod
    def get_project_root_directory():
        """Get root project directory"""
        return os.getcwd()

    @staticmethod
    def get_calculate_file_path(data_directory, data_file_name):
        """Calculate File path"""
        return os.path.join(FileOperations.get_project_root_directory(), data_directory, data_file_name)

    @staticmethod
    def get_csv(data_frame: pandas.DataFrame, file_name: str):
        """Export csv files"""
        data_frame.to_csv(file_name, header=False, index=False)
