﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.IO;
using System.Net;
using System.Net.Http;
using Newtonsoft.Json;
using System.Text;
using System.Threading;
using System.Text.RegularExpressions;

namespace RenpyTranslate
{
    class MainClass
    {
        static string LOGFILE = "translation.log";

        public static void Main(string[] args)
        {
            try
            {
                var appdata = Environment.GetFolderPath(Environment.SpecialFolder.ApplicationData);
                var dir = Path.Combine(appdata, "HHS-Renpy");
                if (!Directory.Exists(dir))
                    Directory.CreateDirectory(dir);
                var fileCache = Path.Combine(dir, "cache.json");

                Dictionary<string,string> translationCache = new Dictionary<string, string>();
                if (File.Exists(fileCache))
                {
                    translationCache = JsonConvert.DeserializeObject< Dictionary<string,string>>(File.ReadAllText(fileCache));
                }
                args[0] = WebUtility.UrlDecode(args[0]);
                var textRussian = string.Join(" ", args);
                File.AppendAllText(LOGFILE, DateTime.Now.ToString("yyyyMMdd HHmmss") + ": \"" + textRussian + "\"\n");

                if (translationCache.ContainsKey(textRussian))
                {
                    Console.Write(translationCache[textRussian]?.Trim());
                }
                else
                {
                    var textEnglish = TranslateString(textRussian);
                    translationCache[textRussian] = textEnglish;
                    Console.Write(WebUtility.UrlEncode(textEnglish?.Trim()));
                }
                File.WriteAllText(fileCache, JsonConvert.SerializeObject(translationCache, Formatting.Indented));
            }
            catch (Exception ex)
            {
                File.AppendAllText(LOGFILE, ex + "\n");
            }
        }

        static Dictionary<string, string> preTranslate = new Dictionary<string, string>() {
            [ "\\\"" ] = "\"",
        };

        static Dictionary<string, string> postTranslate = new Dictionary<string, string>() {
            [ "\\ n" ] = "\n",
            [ "preyakulyatom" ] = "preejaculation",
            [ "patronymic" ] = "last name",
            [ "{U}" ] = "{u}",
            [ "{/ u}" ] = "{/u}",
            [ "\"" ] = "\\\"",
        };

        public static string TranslateString(string ru)
        {
            foreach (var kv in preTranslate) {
                ru = ru.Replace(kv.Key, kv.Value);
            }

            var url = "https://translate.googleapis.com/translate_a/single?client=gtx&sl=ru&tl=en&dt=t";
            WebClient client = new WebClient();
            Thread.Sleep(500);
            client.Headers.Add("user-agent", "Mozilla/5.0 (Windows NT 6.2; WOW64; rv:19.0) Gecko/20100101 Firefox/19.0");
            var json = client.UploadString(url, "q=" + WebUtility.UrlEncode(ru));
            //Console.WriteLine("url: " + url);
            var english = new List<string>();
            foreach (var y in JsonConvert.DeserializeObject<dynamic>(json)[0])
            {
                english.Add(y[0].ToString());
            }
            var result = string.Join(" ", english);

            foreach (var kv in postTranslate) {
                result = result.Replace(kv.Key, kv.Value);
            }

            if (result.Contains("{"))
            {
                result = new Regex(@"{(.+?)}").Replace(result, match => match.Captures[0].Value.Replace(" ", "").ToLower());
            }

            return result;
        }
    }
}
