#Boa:Dialog:loaddialog

import wx
import wx.lib.filebrowsebutton
import os

def create(parent):
    return loaddialog(parent)

[wxID_LOADDIALOG, wxID_LOADDIALOGLOADINGDIR, wxID_LOADDIALOGLOADPROJ, 
] = [wx.NewId() for _init_ctrls in range(3)]

projName=""

class loaddialog(wx.Dialog):
   
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        
        wx.Dialog.__init__(self, id=wxID_LOADDIALOG, name=u'loaddialog',
              parent=prnt, pos=wx.Point(481, 284), size=wx.Size(473, 215),
              style=wx.DEFAULT_DIALOG_STYLE, title=u'Load Project')
        self.SetClientSize(wx.Size(457, 177))
        
        self.Loadproj = wx.Button(id=wxID_LOADDIALOGLOADPROJ,
              label=u'Load Project', name=u'Loadproj', parent=self,
              pos=wx.Point(160, 120), size=wx.Size(131, 31), style=0)
        self.Loadproj.Bind(wx.EVT_BUTTON, self.OnLoadprojButton,
              id=wxID_LOADDIALOGLOADPROJ)

        self.loadingdir = wx.lib.filebrowsebutton.DirBrowseButton(buttonText='Browse',
              dialogTitle='', id=wxID_LOADDIALOGLOADINGDIR,
              labelText='Select a directory:', newDirectory=False, parent=self,
              pos=wx.Point(40, 24), size=wx.Size(360, 48), startDirectory=u'C:\\3d-Model\\projects',
              style=wx.TAB_TRAVERSAL,
              toolTip='Type directory name or browse to select')

        self.loadingdir.SetValue("C:\\3d-Model\\projects")

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnLoadprojButton(self, event):
        global projName
        projName = self.loadingdir.GetValue()
        self.Close()
        event.Skip()

    def OnProjNameTextEnter(self, event):
        event.Skip()
    
    @staticmethod
    def GetValues():
        global projName            
        return projName     
