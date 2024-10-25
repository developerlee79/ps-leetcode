class Solution(object):
    def removeSubfolders(self, folder):
        n = len(folder)

        folder.sort()

        root_folders = [folder[0]]

        for i in range(1, n):
            last_folder = root_folders[-1] + "/"
            if not folder[i].startswith(last_folder):
                root_folders.append(folder[i])

        return root_folders
