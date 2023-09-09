
import re

try:
    def email_extractor(file):
        output_file = open("Emails_Extracted_from_" + file, "w")
        output_file1 = open("Contact_Extracted_from_" + file, "w")
        email_count = 0
        phone_count = 0
        with open(file) as f:
            lines = f.readlines()
            for line in lines:
                pattern = re.compile(r'([a-zA-Z0-9_.+%$-]+@[a-zA-Z0-9_.-]+\.[a-zA-Z]+)')
                phone_pattern = re.compile(r'\d{3}[-\.\s]\d{3}[-\.\s]\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]\d{4}|\d{3}[-\.\s]\d{4}')
                matches = pattern.finditer(line)
                phones = phone_pattern.finditer(line)
                for match in matches:    
                    email_count += 1
                    output_file.write("Email_"+ str(email_count) + ": " + match.group() + "\n")

                for match in phones:    
                    phone_count += 1
                    output_file1.write("Contact_"+ str(phone_count) + ": " + match.group() + "\n")
        output_file.close()
        output_file1.close()
        print(email_count, "emails found !!!")
        print(phone_count, "contacts found !!!")

except Exception as e:
    print("Invalid contents in file. Please check text file.")


if __name__ == "__main__":
    email_extractor("data.txt")