# -*- coding: utf-8 -*-

import PyV8
import base64

params = [
    'NC19FwABclwtGQ5VEEYOVBMFPFEVD3ZYdTh7TSIhBSEYXhZ+DlpRGCAEOEsOFGE9AS4eGQZMAAIrAmYBFjN8FlAAHngOBCkBdwpKRTFXEzsqNRtTHycccD06BEAHPwwmHTgYEDkLbSFoe3UIHhF5LTQGKT0iGWU3MwEAU1AQGUASejBJG3U4PRtEVScqJlBK',
    'de3adY86wJL/s+CmY7TaqG7n9AC5mubTU4COB06alnS3BmXIbjOcJ6Mxex+3YpIb3DOWm7x88Ls/UdEaxXJ+PpVAnoI4HhBSSBpGlX7M8/09Pk8UyRpJls0YzIRf3WLyXIj9A2nKWvdP'
]


repr(params[0].decode('base64'))


class A:
    def aencode(self, input, key):
        input = input.decode('base64')
        _len = len(key)

        code = ''
        for i in range(_len):
            _key = i % _len

            code += chr(ord(input[i]) ^ ord(key[_key]))


        return code.decode('base64')
    def aa(self):
        return self.__aa();

    def __aa(self):
        return 1;


class B:
    import A

    def a(self):
        A.

a = A()
print(a.aa())
print(params[0])
c = a.aencode(params[0], params[1])
print(c)



#
# print('--------')
#
# js = u"""
#
#             function strencode(input, key)
#             {
#                 //input = windows.atob(input);
#
#                 len = key.length;
#                 code = '';
#                 for (i = 0; i < input.length; i++) {
#                     k = i %% len;
#                     code += String.fromCharCode(input.charCodeAt(i) ^ key.charCodeAt(k));
#                 }
#                 console.log(String)
#                 return code
#                 //return windows.atob(code);
#             }
#
#             var source = strencode(%s, %s)
#         """ % (params[0], params[1])
#
#
#
# ctxt = PyV8.JSContext()
# ctxt.enter()
#
# print(js)
#
# ctxt.eval(js)
# vars = ctxt.locals
# print("===========")
# print(vars.source)
# print("===========")