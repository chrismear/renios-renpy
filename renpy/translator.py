# Translator class forward-ported from Ren'Py 6.14, for backwards
# compatibility with games that access this class directly.

import renpy
import renpy.object
import os

class Translator(renpy.object.Object):
    
    def unquote(self, s):
        s = s.replace("\\n", "\n")
        s = s.replace("\\\\", "\\")
        return s
    
    def quote(self, s):
        s = s.replace("\\", "\\\\")
        s = s.replace("\n", "\\n")
        return s
    
    def __init__(self, language):
        """
        Loads the translation from the file `language`.rpt
        """

        self.language = language
        self.translations = { }
        
        f = renpy.loader.load(language + ".rpt")
        
        old = None
        
        for l in f:
            l = l.decode("utf-8")
            l = l.rstrip()
            
            if not l:
                continue
            
            if l[0] == '#':
                continue
            
            s = self.unquote(l[2:])
            
            if l[0] == '<':
                if old:
                    raise Exception("String {0!r} does not have a translation.".format(old))
                
                old = s
                
            if l[0] == ">":
                if old is None:
                    raise Exception("Translation {0!r} doesn't belong to a string.".format(s))
                
                if old in self.translations:
                    raise Exception("Multiple translations for {0!r}.".format(old))

                self.translations[old] = s        
                old = None
        
        f.close()
        
        if old is not None:
            raise Exception("String {0!r} does not have a translation.".format(old))
         
    def update_translations(self, s):
        """
        Update the translations file.
        """
        
        f = file(os.path.join(renpy.config.gamedir, self.language + ".rpt"), "ab")
        
        encoded = self.quote(s).encode("utf-8")
        
        f.write("\r\n")
        f.write("< " + encoded + "\r\n")
        f.write("> " + encoded + "\r\n")
        f.close()
        
        self.translations[s] = s
                
    def translate(self, s):
        """
        Looks up `s` in the translation database. Returns the translation, or
        `s` if no translation is found.
        """
        
        old = s.rstrip()
        
        if not old:
            return s
        
        new = self.translations.get(old, None)
        
        if new is not None:
            return new
        
        if update_translations:        
            self.update_translations(old)
        
        return s

renpy.Translator = Translator