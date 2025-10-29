import csv
from faker import Faker
import os

output_directory = "data"
output_filename = "fake_emails.csv.csv"
number_of_emails = 1000
random_seed = 42
fake = Faker()
fake.seed(random_seed)
