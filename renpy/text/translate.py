import httplib, urllib2, urllib, os, subprocess, re, sys
import traceback
import json

class TranslationCache:

    filename_cache = 'translation-cache.csv'
    cache = {}
    run_msbuild = True

    def __init__(self):
        self.load_cache()
        if sys.platform.startswith('linux') and TranslationCache.run_msbuild:
            subprocess.call("msbuild translator/RenpyTranslate/", shell=True)

    def load_cache(self):
        if os.path.isfile(TranslationCache.filename_cache):
            with open(TranslationCache.filename_cache) as f:
                lines = f.readlines()
                for l in lines:
                    a = json.loads(l)
                    if len(a) == 2:
                        TranslationCache.cache[a[0]] = a[1]
        
        if sys.platform.startswith('linux'):
            print "loaded cache:"
            print json.dumps(TranslationCache.cache)

    def save_cache(self):
        with open(TranslationCache.filename_cache, 'w') as f:
            for key, value in TranslationCache.cache.iteritems():
                f.write(json.dumps([key, value]) + "\n")

    def get_translation(self, t):
        t2 = t
        if re.search(ur"[\u0400-\u04FF]", t, flags=re.U):
            t = t.strip()
            try:
                t2 = TranslationCache.cache[t]
            except:
                if sys.platform.startswith('linux'):
                    t2 = urllib.unquote(subprocess.check_output("translator/RenpyTranslate/bin/Debug/RenpyTranslate.exe \"" +urllib.quote(t.replace("\n", " ").replace("\"", "'").encode('utf8')) + "\"", shell=True))
                    print "translate:", t, "=>", t2
                else:
                    t2 = urllib.unquote(subprocess.check_output("translator/RenpyTranslate/bin/Debug/RenpyTranslate.exe \"" +urllib.quote(t.replace("\n", " ").replace("\"", "'").encode('utf8')) + "\"", shell=False))
                TranslationCache.cache[t] = t2
                self.save_cache()
        return t2
