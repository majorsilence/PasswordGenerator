#!/usr/bin/env python

# Copyright (C) 2008  Peter Gill
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import sys
import time
import pygtk
if not sys.platform == 'win32':
	pygtk.require('2.0')
import gtk
import gtk.glade

import password_rand

class PasswordGui(object):
    def __init__(self):
        self.gladefile = gtk.glade.XML("password.glade")
        self.gladefile.signal_autoconnect(self)
        
        self.key_value=self.gladefile.get_widget("cmbKey")
        self.key_value.set_active(0)
        
        self.statusbar = self.gladefile.get_widget("statusbar1")
        self.statusbar_context_id = self.statusbar.get_context_id("display info")
        
        #setup password textview
        self.passwords=self.gladefile.get_widget("passwords")
        self.passwords.set_editable(False)
        self.password_buffer = self.passwords.get_buffer()
        
        self.password_quantity=self.gladefile.get_widget("quantity")
        self.password_length=self.gladefile.get_widget("password_length")
        
        #0-3
        self.key_type=self.gladefile.get_widget("cmbKey")
        
        self.about_dialog = self.gladefile.get_widget("aboutdialog1")
        
        self.savefile=None
        
    def on_mainwindow_delete_event(self, w=None, e=None):
        gtk.main_quit()
    
    def on_start_clicked(self, w=None):
        print "start your engines"
        self.clear_text()
        self.statusbar.push(self.statusbar_context_id, "Creating...")
        quantity=self.password_quantity.get_value_as_int()
        length=self.password_length.get_value_as_int()
        key_type = self.key_type.get_active()
        time_a=time.time()
        
        # display 200 passwords at a time
        if quantity>200: 
            q2=quantity/200 
            q2=quantity/q2
        else: q2=quantity
        print q2
        password_out=""
        count=0
        while count<quantity:
            password_list = password_rand.randword(q2, length, key_type)
            for x in password_list:
                self.password_buffer.insert(self.password_buffer.get_end_iter(), x+"\n")
            while gtk.events_pending():
                gtk.main_iteration()
            count += q2
        time_b=time.time()
        print "Time elapsed: ", time_b - time_a
        self.statusbar.push(self.statusbar_context_id, "Finished...")
    
    """    
    def clipboard_text_received(self, clipboard, text, data):
        if not text or text=="":
            return
        print text
        cbi = ClipboardInfo()
        cbi.text = text
        
    def on_menu_copy_activate(self, w=None):
        print "Menu item Copy"
        # http://www.pygtk.org/pygtk2tutorial/ch-NewInPyGTK2.2.html
        clipboard = self.passwords.get_clipboard(gtk.gdk.SELECTION_CLIPBOARD)
        clipboard.request_text(self.clipboard_text_received)
        clipboard.clear()
        #print clipboard
        #begin=self.password_buffer.get_insert()
        #end=self.password_buffer.get_selection_bound()
        self.password_buffer.copy_clipboard(clipboard)
        # print a
    """    
    def on_saveas_activate(self, w=None):
        print "save as"
        self.display_filechooser()
    
    def on_save_activate(self, w=None):
        if self.savefile==None:
            self.display_filechooser()
            return
        data=self.get_output()
        self.save_output(self.savefile, data)
    
    def on_new_activate(self, w=None):
        print "new"
        self.clear_text()
    
    def on_about_activate(self, w=None):
        print "about"
        self.about_dialog.run()
        self.about_dialog.destroy()
    
    def display_filechooser(self):
        data=self.get_output()
        
        dialog = gtk.FileChooserDialog(title="Save Passwords",
                action=gtk.FILE_CHOOSER_ACTION_SAVE,
                buttons=(gtk.STOCK_CANCEL, gtk.RESPONSE_CANCEL, gtk.STOCK_SAVE, gtk.RESPONSE_OK))
        
        response=dialog.run()
        if response==gtk.RESPONSE_OK:
            filename=dialog.get_filename()
            self.save_output(filename, data)
        dialog.destroy()
     
    def get_output(self):
        start = self.password_buffer.get_start_iter()
        end = self.password_buffer.get_end_iter()
        output=self.password_buffer.get_text(start, end, True)
        return output
    
    def save_output(self, filename, data):
        self.savefile=filename
        file=open(self.savefile, "w")
        file.write(data)
        file.close()
    
    def clear_text(self):
        start = self.password_buffer.get_start_iter()
        end = self.password_buffer.get_end_iter()
        self.password_buffer.delete(start, end)
        
if __name__ == "__main__":
    gui = PasswordGui()
    gtk.main()
