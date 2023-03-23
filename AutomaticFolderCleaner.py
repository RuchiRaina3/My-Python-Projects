import os

def makeDir(folder, parent=''):
    try:
        os.makedirs(os.path.join(parent,folder))
    except:
        pass

def folderList(files, file_extensions):
    # os.path.splitext(filePath) returns (fileName, extension)
    # print(files)
    # print(file_extensions)
    # for file in files:
    #     print(os.path.splitext(file)[1])
    #     if os.path.splitext(file)[1].lower() in file_extensions and os.path.isfile(file):
    #         print(os.path.splitext(file))
    # print("*************************")
    return [file for file in files if os.path.splitext(file)[1].lower() in file_extensions]

def moveFiles(files, folder, p=''):
    if p=='':
        [os.replace(file,f'{folder}/{file}') for file in files]
    else:
        # p for documents because by default it will check Clutter/ but we want Clutter/Documents
        [os.replace(f'{p}/{file}',f'{p}/{folder}/{file}') for file in files]

if __name__ == "__main__":

    all_files = os.listdir()
    all_files.remove('AutomaticFolderCleaner.py')
    folders = ['Images', 'Documents', 'Music', 'Videos', 'Applications', 'Zipped']
    #Call makeDir() for all folders
    [makeDir(folder) for folder in folders]

    file_extensions = {'Images': ['.jpg', '.jpeg', '.png', '.gif', '.webp'], 'Documents': ['.doc', '.docx', '.txt',
                       '.xls', '.xlsx', '.csv', '.htm', '.html', '.ppt', '.pptx', '.pdf'],
                       'Music': ['.mp3', '.m4a', '.flac', 'wma', '.wav', '.aac'],
                       'Videos': ['.mp4', '.mov', '.wmv', '.avi', ',mpeg-2'],
                       'Applications': ['.app', '.applictaion', '.exe'], 'Zipped': ['.zip'] }

    # Make dictionary with key="Images" and value=file_extensions['Images']
    files_list = {k:folderList(all_files,file_extensions[k]) for k in folders}

    [moveFiles(files_list[folder],folder) for folder in folders]

    parent = 'Documents'
    document_files = os.listdir(parent)
    document_folders = ['Word', 'Presentation', 'Pdf', 'Text', 'Excel', 'CSV', 'Web Pages']
    [makeDir(folder,parent) for folder in document_folders]

    document_extensions = {'Word': ['.doc', '.docx'], 'Presentation': ['.pptx', '.ppt'], 'Pdf': ['.pdf'], 'Text': ['.txt'],
                           'Excel': ['.xls', '.xlsx'], 'CSV': ['.csv'], 'Web Pages': ['.htm', '.html']}
    document_list = {k:folderList(document_files, document_extensions[k]) for k in document_folders}

    [moveFiles(document_list[folder], folder, parent) for folder in document_folders]
