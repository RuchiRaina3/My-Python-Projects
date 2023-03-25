#To use this program you have to move it to the folder which you want to organise and then run it from there.

import os

def makeDir(folder, parent=''):
    try:
        os.makedirs(os.path.join(parent,folder))
    except:
        pass

def folderList(files, file_extensions):
    return [file for file in files if os.path.splitext(file)[1].lower() in file_extensions]

def moveFiles(files, folder, p=''):
    if p=='':
        [os.replace(file,f'{folder}/{file}') for file in files]
    else:
        [os.replace(f'{p}/{file}',f'{p}/{folder}/{file}') for file in files]

if __name__ == "__main__":

    all_files = os.listdir()
    all_files.remove('AutomaticFolderOrganiser.py')
    folders = ['Images', 'Documents', 'Music', 'Videos', 'Applications', 'Zipped']
    [makeDir(folder) for folder in folders]

    file_extensions = {'Images': ['.jpg', '.jpeg', '.png', '.gif', '.webp'], 'Documents': ['.doc', '.docx', '.txt',
                       '.xls', '.xlsx', '.csv', '.htm', '.html', '.ppt', '.pptx', '.pdf'],
                       'Music': ['.mp3', '.m4a', '.flac', 'wma', '.wav', '.aac'],
                       'Videos': ['.mp4', '.mov', '.wmv', '.avi', ',mpeg-2'],
                       'Applications': ['.app', '.applictaion', '.exe'], 'Zipped': ['.zip'] }

    files_list = {k:folderList(all_files,file_extensions[k]) for k in folders}

    [moveFiles(files_list[folder],folder) for folder in folders]

    #Make difefrent folders within document folders
    parent = 'Documents'
    document_files = os.listdir(parent)
    document_folders = ['Word', 'Presentation', 'Pdf', 'Text', 'Excel', 'CSV', 'Web Pages']
    [makeDir(folder,parent) for folder in document_folders]

    document_extensions = {'Word': ['.doc', '.docx'], 'Presentation': ['.pptx', '.ppt'], 'Pdf': ['.pdf'], 'Text': ['.txt'],
                           'Excel': ['.xls', '.xlsx'], 'CSV': ['.csv'], 'Web Pages': ['.htm', '.html']}
    document_list = {k:folderList(document_files, document_extensions[k]) for k in document_folders}

    [moveFiles(document_list[folder], folder, parent) for folder in document_folders]
