"""This is the main startup of the app"""
from app.file_ops import FileOperations
from app.pandas_ops import *


def main():
    """This is the main function that is run"""
    abs_path = FileOperations.get_calculate_file_path(Config.data_directory, Config.file_name)
    out_path = FileOperations.get_calculate_file_path(Config.sample_files_output, "")
    data_frame = PandasCsvRead.get_data_frame(abs_path)
    count = PandasCount.get_count(data_frame)
    file_names = FileNameGenerator.get_file_names(Config.z_scores, Config.margin_of_error, data_frame)
    sample_sizes = []

    for z in Config.z_scores.values():
        for e in Config.margin_of_error:
            sample_sizes.append(SampleSizeGenerator.get_sample_size(z, e, count))

    for n in sample_sizes:
        for file_name in file_names:
            sample = SampleGenerator.get_sample(data_frame, n)
            FileOperations.get_csv(sample, out_path+file_name)

    if __name__ == '__main__':
        """This causes the hello world function to be called if this is the __main__ top level of code"""
        main()
