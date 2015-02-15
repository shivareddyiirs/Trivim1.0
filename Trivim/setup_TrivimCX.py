from cx_Freeze import setup, Executable as cxExecutable
import matplotlib

includefiles = ['camera_calibration/','3d-modelling/','osmcmvs/','osmpmvs/',
                'point_cloud/','segmentation_files/','software/','curr_proj.txt',
                'osmbundler/','resources/','InstallationandUserManuals/',
                'trivim1.jpg','isro1.jpg','iirs.jpg']
excludes = []
packages = ['matplotlib']

WIN_Target = cxExecutable(
    script='NewApplication.py',
    targetName='Trivim.exe',
    compress=True,
    appendScriptToLibrary=True,
    appendScriptToExe=True
    )

setup(
    name='NewApplication',
    description="Script to test pubsub for packaging with cxfreeze",
    version='0.1',
    
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles,}}, 
    executables=[WIN_Target]
    )
