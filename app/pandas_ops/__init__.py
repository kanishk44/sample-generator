"""Pandas operations"""
import math
import pandas
from app.math_ops import *


class PandasCsvRead:
    """Pandas csv read"""
    @staticmethod
    def get_df(absolute_path: str):
        """Read csv from pandas and return data frame"""
        return pandas.read_csv(absolute_path)


class PandasMin:
    """Pandas min"""
    @staticmethod
    def get_min(data_frame: pandas.DataFrame, field_name: str):
        """Minimum value"""
        return data_frame[field_name].min()


class PandasCount:
    """Pandas count"""
    @staticmethod
    def get_count(data_frame: pandas.DataFrame):
        """Count of population"""
        return data_frame.shape[0]


class PandasMax:
    """Pandas max"""
    @staticmethod
    def get_max(data_frame: pandas.DataFrame, field_name: str):
        """Maximum value"""
        return data_frame[field_name].max()


class PandasStd:
    """Pandas standard deviation"""
    @staticmethod
    def get_std(data_frame: pandas.DataFrame, field_name: str):
        """Standard deviation"""
        return data_frame[field_name].std()


class PandasMean:
    """Pandas mean"""
    @staticmethod
    def get_mean(data_frame: pandas.DataFrame, field_name: str):
        """Mean"""
        return data_frame[field_name].mean()


class PandasMode:
    """Pandas mode"""
    @staticmethod
    def get_mode(data_frame: pandas.DataFrame, field_name: str):
        """Mean"""
        return data_frame[field_name].mode()


class PandasMedian:
    """Pandas median"""
    @staticmethod
    def get_median(data_frame: pandas.DataFrame, field_name: str):
        """Median"""
        return data_frame[field_name].median()


class SampleSizeGenerator:
    """Sample size generator"""
    @staticmethod
    def get_sample_size(z_score: float, margin_of_error: float, population: int, std=.5):
        numerator = (SquareNum.get_square(z_score) * std * (1 - std)) / SquareNum.get_square(margin_of_error)
        denominator = 1 + (numerator / population)
        res = RoundingToAppConfig.get_result(math.trunc(numerator / denominator))
        return res


class FileNameGenerator:
    """File name generator"""
    @staticmethod
    def get_file_names(z_scores, margin_of_errors, data_frame: pandas.DataFrame):
        file_names = []
        population = PandasCount.get_count(data_frame)
        for z_score in z_scores.values():
            for margin_of_error in margin_of_errors:
                sample_size = SampleSizeGenerator.get_sample_size(z_score, margin_of_error, population)
                file_names.append("sample_data_number_{}_{}_{}.csv".format(z_score, margin_of_error, sample_size))
        return file_names


class SampleGenerator:
    """Sample generator"""
    @staticmethod
    def get_sample(data_frame: pandas.DataFrame, sample_size: int):
        df = data_frame.sample(n=sample_size - 2)
        min_val = PandasMin.get_min(data_frame, 'pop')
        max_val = PandasMax.get_max(data_frame, 'pop')
        min_rec = df.loc[df['pop'] == min_val]
        max_rec = df.loc[df['pop'] == max_val]
        df.append(min_rec, ignore_index=True)
        df.append(max_rec, ignore_index=True)
        return df
