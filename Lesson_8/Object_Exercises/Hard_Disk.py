class Hard_Disk:
    def __init__(self,size:int):
        self.size=size
        self.files={}

    def __str__(self):
        return f"Hard Disk size: {self.size} Files {self.files} Free Space: {self.free_space()}"

# size: 200
# files: {"aa":25,"bb":110}
# free space: 200 - 135

    def used_space(self):
        sum_files = sum(self.files.values())
        return sum_files

    def free_space(self):
        return self.size-self.used_space()

    def add_file(self,file_name:str,file_size:int):
        if type(file_size)!=int:
            raise TypeError("Invalid file size type. Must be int")

        if file_name in self.files:
            print(f"File {file_name} already exists")

        if self.free_space()>=file_size:
            self.files[file_name]=file_size
            return True
        else:
            print(f"No space for {file_name}")
            return False

    def del_file(self,file_name):
        if file_name not in self.files:
            print(f"File {file_name} doesn't exist")
            return False
        del self.files[file_name]
        return True

    def update_file(self,file_name,file_new_size):
        if file_name not in self.files:
            print(f"File {file_name} doesn't exist")
            return False
        current_file_size = self.files[file_name]
        if self.free_space()+current_file_size < file_new_size:
            print(f"No space for {file_name} size {file_new_size}")
            return False

        self.files[file_name] = file_new_size
        return True

hd = Hard_Disk (200)
hd.type = "SSD"
hd.add_file("aaa",20)
hd.add_file("bbb",100)
hd.add_file("ccc",30)

print(hd)

hd.del_file("aaa")
print(hd)

hd.update_file("ccc",80)
print(hd)

