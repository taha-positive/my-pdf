class TxtTools:
    def __init__(self,txt_path):
        self.path = txt_path;

    def add_pdf_file_to_txt(self,pdf_filenames):
        with open(self.path,"a",encoding="utf-8") as file:
            for filename in pdf_filenames:
                file.write(filename)
                file.write("\n")

    def delete_duplicate_lines_from_txt(self):
        with open(self.path, 'r+', encoding='utf-8') as file:
            lines = file.readlines()
            unique_lines = list(set(lines))
            file.seek(0)
            file.writelines(unique_lines)
            file.truncate()
