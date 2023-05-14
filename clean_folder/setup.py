from setuptools import setup, find_namespace_packages

setup (name = "clean_folder",
       version = "0.0.1",
       description = "Script to clean file garbage",
       url = "",
       author = "Sergiy S",
       author_email = "test@test.com",
       license = "",
       packages = find_namespace_packages(),
       install_requires = ["asgiref", "sqlparse", "markdown"],
       entry_points = {"console_scripts" : ['clean-folder=clean_folder.clean:clean_folders']}
       )
