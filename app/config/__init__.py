"""This is my program config"""


class Config:
    """Program Configure"""
    data_directory = "data"
    file_name = "state_population.csv"
    data_field = "pop"
    sample_files_output = "sample_files_output"
    margin_of_error = [.01, .05, .10]
    z_scores = {"80": 1.28, "85": 1.44, "90": 1.65, "95": 1.96, "99": 2.58}
    rounding_precision = 2
    std = .5

