import csv
from faker import Faker
import os


output_directory = "data"
output_filename = "fake_emails.csv.csv"
number_of_emails = 1000
random_seed = 1234

# Output path
os.makedirs(output_directory, exist_ok=True)
output_file_path = os.path.join(output_directory, output_filename)

# Init Faker
fake_gen = Faker()
Faker.seed(random_seed)


# functions to create emails

def make_fake_subject(fake_instance):
    return fake_instance.sentence(nb_words=6).rstrip('.')

def make_fake_body(fake_instance, num_sentences=4):
    return fake_instance.paragraph(nb_sentences=num_sentences)


# Create CSV
with open(output_file_path, 'w', newline='') as csvfile:
    fieldnames = ["sender", "subject", "body", "date"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for i in range(number_of_emails):
        row = {
            "sender": fake_gen.email(),
            "subject": make_fake_subject(),
            "body": make_fake_body(),
            "date": fake_gen.date()
        }
        writer.writerow(row)

print(f"Generated {number_of_emails} emails -> {output_file_path}")