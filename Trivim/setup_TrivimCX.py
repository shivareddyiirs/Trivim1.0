from cx_Freeze import setup, Executable as cxExecutable
import matplotlib
import os
wrk_drr=os.path.dirname(os.path.realpath(__file__))
os.chdir(wrk_drr)

includefiles = ['camera_calibration/','3d-modelling/','osmcmvs/','osmpmvs/',
                'point_cloud/','software/','curr_proj.txt',
                'osmbundler/','InstallationandUserManuals/',
                'trivim1.jpg','isro1.jpg','iirs.jpg']
excludes = []
packages = ['numpy','matplotlib','collada','PIL']

WIN_Target = cxExecutable(
    script='NewApplication.py',
    targetName='Trivim.exe'
    )

setup(
    name='NewApplication',
    description="Script to test pubsub for packaging with cxfreeze",
    version='0.1',
    
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles,}}, 
    executables=[WIN_Target]
    )
